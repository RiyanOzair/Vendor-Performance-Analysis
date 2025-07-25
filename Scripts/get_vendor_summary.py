import pandas as pd
import sqlite3
import logging
from ingestion1_db import ingest_db

logging.basicConfig(
    filename='Logs/get_vendor_summary.log',
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='a'
)

def create_final_vendor_summary(conn):
    ''' This function will merge the different tables to get the final summary table '''
    
    final_summary_table = pd.read_sql_query("""
        WITH 
        FreightSummary AS (
            SELECT 
                VendorNumber, 
                SUM(Freight) AS FreightCost
            FROM vendor_invoice
            GROUP BY VendorNumber
        ),
            
        PurchaseSummary AS (
            SELECT 
                p.VendorNumber,
                p.VendorName,
                p.Brand,
                p.Description,
                pp.Price AS ActualPrice,
                p.PurchasePrice,
                pp.Volume,
                SUM(p.Quantity) AS TotalPurchaseQuantity,
                SUM(p.Dollars) AS TotalPurchaseDollars        
            FROM purchases p
            JOIN purchase_prices pp
                ON p.Brand = pp.Brand
            WHERE p.PurchasePrice > 0 
            GROUP BY 
                p.VendorNumber,
                p.VendorName,
                p.Brand,
                p.Description,
                pp.Price,
                p.PurchasePrice,
                pp.Volume
        ),
            
        SalesSummary AS (
            SELECT 
               VendorNo,
               Brand,
               SUM(SalesPrice) AS TotalSalesPrice,
               SUM(SalesQuantity) AS TotalSalesQuantity,
               SUM(SalesDollars) AS TotalSalesDollars,
               SUM(ExciseTax) AS TotalExciseTax
            FROM sales
            WHERE SalesPrice > 0
            GROUP BY VendorNo, Brand
        )
        
        SELECT 
            ps.VendorNumber,
            ps.VendorName,
            ps.Brand,
            ps.Description,
            ps.ActualPrice,
            ps.PurchasePrice,
            ps.Volume,
            ps.TotalPurchaseQuantity,
            ps.TotalPurchaseDollars, 
            ss.TotalSalesPrice,
            ss.TotalSalesQuantity,
            ss.TotalSalesDollars,
            ss.TotalExciseTax,
            fs.FreightCost
        FROM PurchaseSummary ps
        LEFT JOIN SalesSummary ss
            ON ps.VendorNumber = ss.VendorNo AND ps.Brand = ss.Brand
        LEFT JOIN FreightSummary fs
            ON ps.VendorNumber = fs.VendorNumber
        ORDER BY ps.TotalPurchaseDollars DESC

    """, conn)

    return final_summary_table


def clean_data(df):
    '''This function will clean the data'''
    
    # changing datatype to float
    df['Volume'] = df['Volume'].astype('float')
    
    # filling missing value with 0
    df.fillna(0, inplace=True)
    
    # removing spaces from categorical columns
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()
    
    # creating new columns for better analysis
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = (df['GrossProfit'] / df['TotalSalesDollars']) * 100
    df['StockTurnover'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
    df['SalesToPurchaseRatio'] = df['TotalSalesDollars'] / df['TotalPurchaseDollars']
    
    return df


if __name__ == '__main__':
    ''' Creating Database connection '''
    conn = sqlite3.connect('inventory1.db')

    logging.info('Creating Vendor Summary Table.....')
    summary_df = create_final_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info('Cleaning Data.....')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingesting data.....')
    ingest_db(clean_df, 'final_summary_table', conn)
    logging.info('Completed')

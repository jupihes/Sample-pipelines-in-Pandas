'''python
# -*- coding: utf-8 -*-

""" 
    Name:           bulk_insert.py
    Author:         Mehdi and Hesam
    Date:           July 17, 2022
    Description:    Inspiraed by post of Randy Runtsch, [](https://towardsdatascience.com/use-python-and-bulk-insert-to-quickly-load-data-from-csv-files-into-sql-server-tables-ba381670d376)
                     
                    This module contains the c_bulk_insert class that connect to a SQL Server database
                    and executes the BULK INSERT utility to insert data from a CSV file into a table.
    Prerequisites:  1. Create the database data table.
                    2. Create the database update_csv_log table.
                    we develop it to handle 
                    
"""
from pyodbc import connect
from sqlalchemy import create_engine
import datetime
from os import listdir, chdir


csv_file_nm1=r'\\t1w022\Datascience\Cashback\DIRECT_CHANNEL_CASHBACK_20220612.csv'
sql_server_nm1='T1w022'
db_nm1='DataScience'
db_table_nm1='eng.load_cashback_posted_bolton_MSISDN_Daily_2022_temp2'

class c_bulk_insert:
    def __init__(self, csv_file_nm="\\t1w022\Datascience\Cashback\marketplace_cashback_20perc_20220708.csv"
                 , sql_server_nm='T1w022', db_nm='DataScience'
                 , db_table_nm='[eng].[load_cashback_posted_Marketplace_MSISDN_Daily_2022_temp2]'):
    # Connect to the database, perform the insert, and update the log table.
        """conn = self.connect_db(T1w022, DataScience)
                self.insert_data(conn, csv_file_nm, db_table_nm)
                conn.close
        """
    def connect_db(self, sql_server_nm, db_nm):
    # Connect to the server and database with Windows authentication.
        conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + sql_server_nm + ';DATABASE=' + db_nm + ';Trusted_Connection=yes;'
        conn = connect(conn_string)# pyodbc.connect(conn_string)
        return conn

    def connect_db_alchemy(self):
        db_con = create_engine('mssql+pyodbc://T1W022/DataScience?driver=SQL+Server+Native+Client+11.0')
        #conn = db_con.connect()
        conn = db_con.raw_connection() #https://stackoverflow.com/questions/49797786/how-to-get-cursor-in-sqlalchamy
        return conn

    def insert_data(self, conn, csv_file_nm, db_table_nm):
    # Insert the data from the CSV file into the database table.
    # Assemble the BULK INSERT query. Be sure to skip the header row by specifying FIRSTROW = 2.
        # qry = "BULK INSERT " + db_table_nm + " FROM '" + csv_file_nm + "' WITH (FORMAT = 'CSV', FIRSTROW = 2)"
        qry = "BULK INSERT " + db_table_nm + " FROM '" + csv_file_nm + "' WITH (FIRSTROW = 2, FIELDTERMINATOR = ',' , ROWTERMINATOR = '\r\n')" # '0x0a'
        #https://stackoverflow.com/questions/10851065/bulk-insert-with-identity-auto-increment-column
        #https://stackoverflow.com/questions/13056929/bulk-load-data-conversion-error-type-mismatch-or-invalid-character-for-the-spec
        # Execute the query
        cursor = conn.cursor()
        success = cursor.execute(qry)
        conn.commit()
        cursor.close

    def insert_folder_date(self, conn, db_table_nm, folder_add='//t1w022/Datascience/Cashback/',
                           file_name_pattern='DIRECT_CHANNEL_CASHBACK',
                           from_day = -32, to_day =-1):
        # Insert the data from CSV files in specified folder and in date range mentioned into the database table.
        
        # file_list = [i for i in listdir(folder_add) if i.startswith(file_name_pattern)]
        # chdir(folder_add)
        # file_list = []
        for temp_date in range(from_day,to_day+1, 1):
            temp_date = (datetime.date.today() - datetime.timedelta(days=(temp_date * -1))).strftime('%Y%m%d')
            temp_file = file_name_pattern + '_' + temp_date + '.csv'
            #file_list.append(temp_file)
            # print(temp_file)
            qry = "BULK INSERT " + db_table_nm + " FROM '" + folder_add + temp_file + "' WITH (FIRSTROW = 2, FIELDTERMINATOR = ',' , ROWTERMINATOR = '\r\n')" # '0x0a'
            print(qry)
            ## https://stackoverflow.com/questions/10851065/bulk-insert-with-identity-auto-increment-column
            ## https://stackoverflow.com/questions/13056929/bulk-load-data-conversion-error-type-mismatch-or-invalid-character-for-the-spec
            ### Execute the query
            cursor = conn.cursor()
            success = cursor.execute(qry)
            conn.commit()
            print('Bulk instert file {} finished'.format(temp_file))
            cursor.close

        # return file_list


# =============================================================================
# ####### csv file cleaning - pandas or other ##########
# import pandas as pd
# 
# def csv_cleaning(csv):
#     return df_Marketplace = (read_file(name_pat='marketplace_cashback_20perc_',
#                            date=yesterday, date_cols=['date']))\
#                        .assign(date=lambda x: x['date'].dt.strftime('%Y%m%d'))\
#                        .rename(columns= {'date':'date_key', 'customer_msisdn':'msisdn_nsk'})
# with open(‘million_users.csv’, ‘r’) as csv_file:
#     csv_reader = csv.reader(csv_file)
# ###############################
# =============================================================================
connection_try = c_bulk_insert()
# conn1 = connection_try.connect_db(sql_server_nm = sql_server_nm1, db_nm = db_nm1)
conn1 = connection_try.connect_db_alchemy()#sql_server_nm = sql_server_nm1, db_nm = db_nm1)
#### inserting one file ######
# connection_try.insert_data(conn=conn1, csv_file_nm=csv_file_nm1, db_table_nm=db_table_nm1)
#### inserting bunch of files ######
connection_try.insert_folder_date(conn=conn1, db_table_nm=db_table_nm1
                                  ,from_day = -32, to_day =-1)
'''

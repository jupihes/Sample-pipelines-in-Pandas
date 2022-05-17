# Sample-pipelines-in-Pandas




### General tasks
|    |   Action 1    |Action 2|
|----------|:-------------:|------:|
| FTP | Read | Write| 
| SQL | Read | Write| 

### OS related
|    |   Action 1    |Action 2|
|----------|:-------------:|------:|
| File | Make | delete |
| Folder| Make | delete  |



### Python Database ![Python MySQL database Guide](https://pynative.com/python/databases/)

Learn how to perform Database operations from Python.

![Python SQLite](https://pynative.com/python-sqlite/): Develop Python applications with the SQLite database to perform SQLite operations.

Python MySQL: Perform all MySQL database operations from Python using MySQL Connector Python.

    - Python MySQL Connection Guide
    - Python MySQL Insert
    - Python MySQL Select
    - Python MySQL Update
    - Python MySQL Delete
    - Call MySQL Stored Procedure
    - Python MySQL Parameterized Query
    - Python MySQL Transactions
    - Python MySQL Connection Pooling
    - Python MySQL BLOB

Python PostgreSQL: Develop Python applications with the PostgreSQL server to perform PostgreSQL database operations using psycopg2.


```python

import mysql.connector
from sqlalchemy import create_engine

cnx = mysql.connector.connect(user='...',password='...', database='...')
cursor = cnx.cursor()

# ==================         Table creation         ===========================
## table 1 : cleaned English records
query_divar_clean_car = ("CREATE TABLE `Divarcar` ("
    "  `id` int(10) NOT NULL AUTO_INCREMENT,"
    "  `Year` int(4) NOT NULL,"
    "  `Km` int(10) NOT NULL,"
    "  `Price` int(16) NOT NULL,"
    "  `Modelid` varchar(2), "
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

cursor.execute(query_divar_clean_car)

## table 2: mapping URL to items details by indexas unique key
# "index", "url", "hash url"
'''To make it possibble to write Persian utf8 (4 bytes) to  MYSQL DB
ALTER DATABASE learndb
  CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
'''

query_car_urls = ("CREATE TABLE `carurls` ("
    "  `id` int(10) NOT NULL AUTO_INCREMENT,"
    "  `url`     varchar(100) , "
    "  `hashurl`      varchar(64), "
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")
#char(20) character set utf8 set colates utf8_persian_ci
cursor.execute(query_car_urls)

## table 3 : car mapping Persian to English to modelID
query_car_mapping = ("CREATE TABLE `carmapping` ("
    "  `name` varchar(15) ,"
    "  `persian_name`     varchar(20), "
    "  `car_typeid`      varchar(3), "
    "  PRIMARY KEY (`name`)"
    ") ENGINE=InnoDB")
    
cursor.execute(query_car_mapping)

###################### Writing to Mysql with Pandas to_sql ####################

database_username = '...'
database_password = '...'
database_ip       = '...'
database_name     = '...'
database_connection = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                      format(database_username, database_password, 
                      database_ip, database_name), pool_recycle=1,
                            encoding='utf8', pool_timeout=57600).connect()
#https://datatofish.com/pandas-dataframe-to-sql/

df_clean_ml.to_sql(name='divarcar', con=database_connection, if_exists='replace', index_label= False)
### solving problem of Persian text 
# https://sebhastian.com/mysql-incorrect-string-value/

df_url.to_sql(name='carurls', con=database_connection, if_exists='replace', index_label= False)
car_mapping_table.to_sql(name='carurls', con=database_connection, if_exists='replace', index_label= False)

database_connection.close()
```


```python
def read(fp):
    df = (pd.read_csv(fp, usecols= [])   # basic read file. It is highly recommended to use `read_csv` features.  
            .rename(columns=str.lower) # rename columns or change all to lower or upper
            .rename(columns= {'server ip':'ip', 'total traffic':'traffic'}) # rename columns or change all to lower or upper
            .drop('unnamed: 36', axis=1) # drop column or drop row  
            .pipe(extract_city_name) # sample pipe operation on dataframe - explanation = f(g(x)
            .pipe(time_to_datetime, ['dep_time', 'arr_time', 'crs_arr_time', 'crs_dep_time'])
            .assign(fl_date=lambda x: pd.to_datetime(x['fl_date']),  # make new columns from existintg - useful for calculation, data_time, change to categorical
                    dest=lambda x: pd.Categorical(x['dest']),
                    origin=lambda x: pd.Categorical(x['origin']),
                    tail_num=lambda x: pd.Categorical(x['tail_num']),
                    unique_carrier=lambda x: pd.Categorical(x['unique_carrier']),
                    cancellation_code=lambda x: pd.Categorical(x['cancellation_code'])))
    return df

# sample functions to be used with df.pipe()
def extract_city_name(df):
    '''
    Chicago, IL -> Chicago for origin_city_name and dest_city_name
    '''
    cols = ['origin_city_name', 'dest_city_name']
    city = df[cols].apply(lambda x: x.str.extract("(.*), \w{2}", expand=False))
    df = df.copy()
    df[['origin_city_name', 'dest_city_name']] = city
    return df

def time_to_datetime(df, columns):
    '''
    Combine all time items into datetimes.

    2014-01-01,0914 -> 2014-01-01 09:14:00
    '''
    df = df.copy()
    def converter(col):
        timepart = (col.astype(str)
                       .str.replace('\.0$', '')  # NaNs force float dtype
                       .str.pad(4, fillchar='0'))
        return pd.to_datetime(df['fl_date'] + ' ' +
                               timepart.str.slice(0, 2) + ':' +
                               timepart.str.slice(2, 4),
                               errors='coerce')
    df[columns] = df[columns].apply(converter)
    return df
```

```python


https://colab.research.google.com/github/gardnmi/blog/blob/master/_notebooks/2021-08-22-chaining-in-pandas.ipynb#scrollTo=HJKjYCTtSOyw
# CHAINING
df = raw_df.copy()
df = (
    df
    .set_index('PassengerId')
    .assign(
        Title=df.Name.str.extract('([A-Za-z]+)\.')
    )
    .assign(Title=lambda df:
            np.select(
                condlist=(df.Title.isin(['Mlle', 'Ms']),
                          df.Title.isin(['Mme', 'Mrs']),
                          df.Title.isin(['Mr'])),
                choicelist=('Miss', 'Mrs', 'Mr'),
                default='Rare'),

            Age_bin=pd.cut(
                df['Age'],
                bins=[0, 12, 20, 40, 120],
                labels=['Children', 'Teenage', 'Adult', 'Elder']),

            Fare_bin=pd.cut(
                df['Fare'],
                bins=[0, 7.91, 14.45, 31, 120],
                labels=['Low_fare', 'median_fare', 'Average_fare', 'high_fare'])
            )
    .assign(
        Age_bin=lambda df: df.Age_bin.astype('category'),
        Fare_bin=lambda df: df.Fare_bin.astype('category')
    )
    .drop(['Age', 'Fare', 'Name', 'Ticket', 'Cabin'], axis=1)
    .query('Survived == 0')

    ## NEW SECTION ##
    .pipe(lambda df: pd.get_dummies(df, columns=["Sex", "Title", "Age_bin", "Embarked", "Fare_bin"]))

)

df.head()
```


```python
https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html 

## read files – part 1
import pandas as pd
import numpy as np

file1_add = r"D:\TEST\relation_file.xlsx"
df1 = pd.read_excel(file_add1)

file2_add = r"D:\TEST\Carrier Level - Number of 4G Cells.xlsx"
df2 = pd.read_excel(file_add2)

## Join part – part 2
https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html# 
#do join based on your need and save result in 'summary' 

## Pivot part – part 3
https://pbpython.com/pandas-pivot-table-explained.html 
d = pd.pivot_table(summary, index=['BTS','4G LTE CELL'], values=["Carrier"], aggfunc = np.unique)

## writing result – part 4 
writer = pd.ExcelWriter(r'D:\ Output.xlsx', engine= 'xlsxwriter')
d.to_excel(writer, 'Sheet1', index = False)
writer.save()

```

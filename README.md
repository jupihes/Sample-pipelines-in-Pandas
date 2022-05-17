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

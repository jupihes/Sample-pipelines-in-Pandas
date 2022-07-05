
# Mehdi Sample 1 - "Market Place" Cleaning
import pandas as pd
from os import chdir

chdir('D:/.../Sample pipeline')

def data_cleaning(input_csv):
    df = (pd.read_csv(input_csv, parse_dates=['date', 'tansaction_rdate'])   # basic read file. It is highly recommended to use `read_csv` features.  
            .rename(columns=str.lower) # rename columns or change all to lower or upper
            .rename(columns= {'date':'date_key', 'customer_msisdn':'msisdn_nsk'}) # rename columns or change all to lower or upper
            .drop('payment_id', axis=1) # drop column or drop row
            .assign(date_key=lambda x: x['date_key'].dt.strftime('%Y%m%d'),  # make new columns from existintg - useful for calculation, data_time, change to categorical
                    msisdn_nsk_clean=lambda x: x['msisdn_nsk'].astype(str).str[2:],  # get rid of the first 2 digits - substr in SQL
                    msisdn_lastdigit=lambda x: x['msisdn_nsk'].astype(str).str[-1],  # extract last digit to be used
                    msisdn_nsk_extended=lambda x: '935' + x['msisdn_nsk'].astype(str).str[2:] + '935',  # add text - Concatenate in SQL
                    msisdn_check=lambda x: x['msisdn_nsk'].str.contains(r'\d{11}'),  # regex usecase sample: check if columns contains pattern of 11 decimal digit
                    tansaction=lambda x: x['tansaction'].replace({'%':''}, regex=True).astype('float'),  # remove '%' character from 'tansaction' column and convert to float
                    temp_hour=lambda x: x['transaction_date'].dt.hour)  # extract hour 
            .query('delearname in ("SNAPCAB", "SNAPFOOD", "SNAPMARKET")')   # filtering on column with `in`
            #.sort_values(by = ['granted_gift_irr'], ascending=False)
            .assign(rank=lambda x: x.sort_values(['granted_gift_irr', 'msisdn_lastdigit','temp_hour'], #  make rank based on 3 columns; similar to `SQL` partition by
                                                 ascending=(False, True, True)
                                                 )
                    .groupby(['date_key', 'msisdn_lastdigit'])
                    .cumcount()
                    + 1    
                    )
            #.query("rank < 3")
            .sort_values(["date_key", "rank"])  # sort values
          )
    return df
    
df = data_cleaning('marketplace_cashback_20perc_20220517.csv')


###################################################################
sample_list = ['432355850033E505E', '432355850033E505E',
'43235A678029F2217', '43235A678029F2217',
'43235521F878F','43235521F878F',
'43235A7747072','43235591C2FBE']
df = pd.DataFrame(sample_list, columns=['CellID'])

df['CellID']=  df.CellID.str[5:] # remove first 5 characters 
df['Lenght'] = df.CellID.str.len() # extract length 

df.loc[df['Lenght'] == 8,'TECH'] = '2G/3G'
df.loc[df['Lenght'] == 12,'TECH'] = '4G'
df.loc[df['TECH'].isna(),'TECH'] = 'Wrong input!'

df.loc[df['TECH'] == '2G/3G', 'LAC'] =  df['CellID'].str[:4].apply(lambda x: int(x, 16)).astype(str)
df.loc[df['TECH'] == '2G/3G', 'CI'] =  df['CellID'].str[4:].apply(lambda x: int(x, 16)).astype(str)


df.loc[df['TECH'] == '4G', 'TAC'] =  df['CellID'].str[:4].apply(lambda x: int(x, 16)).astype(str)
df.loc[df['TECH'] == '4G', 'ECI'] =  df['CellID'].str[4:].apply(lambda x: int(x, 16)).astype(str)


df.loc[df['Lenght'] == 12,'TECH'] = '4G'


A='318088A3'
'{}{}'.format(int(A[:4], 16), int(A[-4:], 16))


B='5850033E505E'
'{}{}'.format(int(B[:4], 16), int(B[4:], 16))

###################################################################
# remove english hidden characters https://pbpython.com/pandas-html-table.html
# The issue here is that we have a hidden character, xa0 that is causing some errors. This is a “non-breaking Latin1 (ISO 8859-1) space”.
from unicodedata import normalize

def clean_normalize_whitespace(x):
    if isinstance(x, str):
        return normalize('NFKC', x).strip()
    else:
        return x

# To check and make similar functionality for Persian 
###################################################################
# Reordering, reindexing, and sorting data
df[df.datatype == 'TAVG']. nlargest(n=10, columns='temp_C')

.sort_index()

'''Both sort_index()  and sort_values()  return new DataFrame
objects. We must pass in inplace=True to update the dataframe we are
working with.
'''

# sample for filtering output using `isin` amd `query`
df[df.ENODEBID.isin(duplicate_ENB.query('ENODEBID > 1')['index'])].to_excel('duplicate ENB list.xlsx')


### Reshaping data
Transposing 
Pivoting 
##############################################

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


column_names = {'Date': 'date', 'Start (ET)': 'start',
                'Unamed: 2': 'box', 'Visitor/Neutral': 'away_team', 
                'PTS': 'away_points', 'Home/Neutral': 'home_team',
                'PTS.1': 'home_points', 'Unamed: 7': 'n_ot'}

games = (games.rename(columns=column_names)
    .dropna(thresh=4)
    [['date', 'away_team', 'away_points', 'home_team', 'home_points']]   # column selection
    .assign(date=lambda x: pd.to_datetime(x['date'], format='%a, %b %d, %Y'))
    .set_index('date', append=True)                                      # set index
    .rename_axis(["game_id", "date"])                                    # rename axis
    .sort_index()                                                        # sort index
    )


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


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

 
### 1 - Data cleaning
 
- Renaming
- Sorting and reordering
- Data type conversions
- Handling duplicate data
- Addressing missing or invalid data
- Filtering to the desired subset of data

```python
def read(input_csv):
    df = (pd.read_csv(input_csv, usecols= [])   # basic read file. It is highly recommended to use `read_csv` features.  
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
    
    
import datetime
import jdatetime 

def p_to_g(d):
    # d = jdatetime.datetime.now(d).strftime("%Y/%m/%d").split('/')
    d = d.split('/')
    # pd.to_datetime(jdatetime.date(int(d[0]), int(d[1]),int(d[2])).togregorian(),format="%Y/%m/%d")
    # jdatetime.date(int(d[0]), int(d[1]),int(d[2])).togregorian()
    return pd.to_datetime(jdatetime.date(int(d[0]), int(d[1]),int(d[2])).togregorian(),\
         utc=True, format="%Y/%m/%d") #tzinfo= 'Iran Standard Time',

df['gdate'] = df.apply(lambda x: p_to_g(x['pdate']), axis =1)
```

### 2 - Data enrichment
 
- Adding new columns: Using functions on the data from existing columns to create
new values.

- Binning: Turning continuous data or discrete data with many distinct values into
buckets, which makes the column discrete while letting us control the number of
possible values in the column.
- Aggregating: Rolling up the data and summarizing it.
- Resampling: Aggregating time series data at specifi intervals

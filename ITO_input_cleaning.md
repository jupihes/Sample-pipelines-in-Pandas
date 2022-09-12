

```python
import pandas as pd
import datetime
import jdatetime

from os import chdir
chdir(r'F:\Hesam\ITO half rating list\Mordad 1401')

df_ito = pd.read_excel('ITO whole list.xlsx', names = ['URL', 'IPV4', 'pdate','target for Operator'])
del df_ito['target for Operator']

def p_to_g(d, splitter='/', date_out_format="%Y%m%d"):
    import jdatetime
    d = d.split(splitter)

    return jdatetime.date(int(d[0]), int(d[1]),int(d[2])).togregorian().strftime(date_out_format)

df_ito['gdate'] = df_ito.apply(lambda x: p_to_g(x['pdate']), axis=1)

# df_ito = df_ito.drop_duplicates(sub = ['URL', 'IPV4'], inplace  =True)

# df_ito.drop_duplicates(sub = ['URL', 'IPV4'])

df_ito[df_ito.gdate < '20220823'].\
    drop_duplicates(subset = ['URL', 'IPV4'], keep = 'first').\
    to_excel('whole_ITO_Mordad_DB_insertion_new.xlsx',index=False)
```

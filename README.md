
<div align="right" style="text-align:middle"><i>Hesam, Mehdi and Farzaneh
<br><a href="">?</a><br>2022</i>
</div>

# Data pipeline managment samples with Python



# Who is this for?
Those looking for *automate repetitve Data Eng tasks with programming*. 

> Very good to read [Teach Yourself Programming in Ten Years](https://norvig.com/21-days.html) by [Peter Norvig](https://norvig.com)


# Data pipeline management with coding 

1. [Data cleaning in read](https://github.com/jupihes/Sample-pipelines-in-Pandas/blob/main/pandas%20sample%20pipeline.py)
2. Data transform – in progress : Hesam & Farzaneh & Mehdi 

   1. Pivot - Farzaneh 
   2. Binning - Hesam & Mehdi 
    
3. Data visualization and reporting - ?  
    1. Email  
    2. Make Excel, PDF attachment 
    3. Add table to body of email 
    4. Make plot as part of email HTML content 
    5. Make HTML content 
        . Rich content 
    6. Visualization  
        . Plotly or Bokeh 
4. SQL – to be finished  

    1. Read 
    2. Write 
    3. [Bulk insert](https://github.com/jupihes/Sample-pipelines-in-Pandas/blob/main/bulk_insert.md)
   
        - SQL Bulk insert with Python 
        - Make abstract function with parameters to handle these 
        - 
5. FTP – in progress : Mehdi 

    . [Read](https://github.com/jupihes/Sample-pipelines-in-Pandas/blob/main/ftp_read.py) 
    
    . Write 
    
    . [Class for FTP actions]() 
    
6. Log file generation

8. What else?  
9. 
    1. Multithread sample 
    2. Subprocess sample 

  

# Index of codes



|Run|Year|Code address|




![]()




# Sample-pipelines-in-Pandas

In this repository, we aim to provide sample for different tasks like those mention in below table.

different


### General tasks
|    |   Action 1    |Action 2|
|----------|:-------------:|------:|
| FTP | [Read](https://github.com/jupihes/Sample-pipelines-in-Pandas/blob/main/ftp%20actions.md#read-files-from-ftp) | [Write](https://github.com/jupihes/Sample-pipelines-in-Pandas/blob/main/ftp%20actions.md#write-file-to-ftp)| 
| SFTP | Read | Write| 
| [SQL](https://github.com/jupihes/Sample-pipelines-in-Pandas/blob/main/SQL%20via%20python.py) 
|[SQL Bulk Insert]()
|[SQL Bulk Insert with Logging]()
[Read]() | [Write]()| 
|Pandas| [Pipline for read & clean](https://github.com/jupihes/Sample-pipelines-in-Pandas/blob/main/pandas%20sample%20pipeline.py)
[sample data cleaning](https://github.com/jupihes/Sample-pipelines-in-Pandas/blob/main/pandas%20sample%20pipeline.py)
[]()
|
|Pandas| [Pipline for transform]()|
|Pandas| [Pipline for write]()|




```python

import pysftp

with pysftp.Connection('hostname', username='me', password='secret') as sftp:

    with sftp.cd('/allcode'):           # temporarily chdir to allcode
        sftp.put('/pycode/filename')  	# upload file to allcode/pycode on remote
        sftp.get('remote_file')         # get a remote file
```

### OS related
|    |   Action 1    |Action 2|
|----------|:-------------:|------:|
| File | 
Make |
delete |
| Folder| Make | delete  |



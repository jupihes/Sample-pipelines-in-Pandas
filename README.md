# Sample-pipelines-in-Pandas

In this repository, we aim to provide sample for different tasks like those mention in below table.

different


### General tasks
|    |   Action 1    |Action 2|
|----------|:-------------:|------:|
| FTP | [Read](https://github.com/jupihes/Sample-pipelines-in-Pandas/blob/main/ftp%20actions.md#read-files-from-ftp) | [Write](https://github.com/jupihes/Sample-pipelines-in-Pandas/blob/main/ftp%20actions.md#write-file-to-ftp)| 
| SFTP | Read | Write| 
| ![SQL](https://github.com/jupihes/Sample-pipelines-in-Pandas/blob/main/SQL%20via%20python.py) | Read | Write| 
|Pandas| ![Pipline for read & clean](https://github.com/jupihes/Sample-pipelines-in-Pandas/blob/main/pandas%20sample%20pipeline.py)|
|Pandas| ![Pipline for transform]()|
|Pandas| ![Pipline for write]()|


https://github.com/jupihes/Sample-pipelines-in-Pandas/blob/main/pandas%20sample%20pipeline.py

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
| File | Make | delete |
| Folder| Make | delete  |



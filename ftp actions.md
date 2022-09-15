### Read files from FTP

- `from_date` and `to_date` to mention clear dates 
- or use `past_n_day` with n = 1 as yesterday
- Option for `remote path`, `local path`, `file deletion` at FTP-side
```
# based on what I saw at http://code.activestate.com/recipes/327141-simple-ftp-directory-synch/
def moveFTPFiles(remotePath = './CVMDS/Direct_Channel_Cashback_Recharge/', 
                 serverName = '10.132.57.198',
                 userName ='...' ,
                 passWord ='...', 
                 localPath =  'E:/Reports/Cashback/',
                 deleteRemoteFiles=False, 
                 onlyDiff=False, 
                 transFile_name_pattern='DC_cashback_Recharge_',
                 past_n_day = None, 
                 from_date = '20220905' ,
                 to_date = '20220913'
                 ):

    """Connect to an FTP server and bring down files to a local directory"""
    import os
    from datetime import date, timedelta, strptime
    #from sets import Set
    from ftplib import FTP 
    try:
        ftp = FTP(serverName)       # connect to host, default port
    except:
        print("Couldn't find server")
    ftp.login(userName,passWord)    # user login using user and pass
    ftp.cwd(remotePath)             # change into "remotePath" directory
# =============================================================================
#     
#     #### with file name containing date ####
# 
#     oneday = datetime.timedelta(days=1)     #create 1 day in datetime format
#     yesterday = (datetime.date.today() - oneday).strftime('%Y%m%d') # make yesterday in 20220618 format
#        
#     transfer_file = transFile_name_pattern + yesterday + '.csv'
#     
# 
# =============================================================================
    frmt = '%Y%m%d'   
    transferList = []
    
    try:
        print("Connecting...")
        
        if onlyDiff:
            lFileSet = set(os.listdir(localPath))
            rFileSet = set(ftp.nlst())
            transferList = list(rFileSet - lFileSet)
            print("Missing: " + str(len(transferList)))
        else:
            if transFile_name_pattern:
                if past_n_day == None:
                    b = strptime(from_date, '%Y%m%d')# datetime.strptime(from_date, '%Y%m%d')
                    a = strptime(to_date, '%Y%m%d')# datetime.strptime(to_date, '%Y%m%d')
                    n = (a-b).days
                    
                    transferList = []
                    for i in range(n):
                        temp_day = date.today() - timedelta(days = i)
                        transfer_file = f'{transFile_name_pattern}{temp_day:%Y%m%d}.csv'
                        transferList.append(transfer_file)

                elif past_n_day != None:
                    transferList = []
                    for i in range(past_n_day):
                        temp_day = date.today() - timedelta(days = i)
                        transfer_file = f'{transFile_name_pattern}{temp_day:%Y%m%d}.csv'
                        transferList.append(transfer_file)
            else:
                transferList = ftp.nlst()
        
        print('File to be transfered:', transfer_file)
        
        delMsg = ""	
        filesMoved = 0
        for fl in transferList:
            # create a full local filepath
            localFile = localPath + fl
            grabFile = True
            if grabFile:				
                #open a the local file
                fileObj = open(localFile, 'wb')
                # Download the file a chunk at a time using RETR
                ftp.retrbinary('RETR ' + fl, fileObj.write)
                # Close the file
                fileObj.close()
                filesMoved += 1
                
            # Delete the remote file if requested
            if deleteRemoteFiles:
                ftp.delete(fl)
                delMsg = " and Deleted"
            
        print("Files Moved" + delMsg + ": " + str(filesMoved) + " on " + timeStamp())
    except:
        print("Connection Error - " + timeStamp())
    ftp.close() # Close FTP connection
    ftp = None

def timeStamp():
    """returns a formatted current time/date"""
    import time
    return str(time.strftime("%Y%m%d")) #str(time.strftime("%a %d %b %Y %I:%M:%S %p"))


#.strftime("%F") # '2022-05-21'

# if __name__ == '__main__':
#     #--- constant connection values
#     ftpServerName = "ftpservername.com" # or IP address if Address Resulotion work on server 
#     ftpU = "ftpusername"
#     ftpP = "ftppassword"
#     remoteDirectoryPath = "remote/ftp/subdirectory"
#     localDirectoryPath = """local\sub\directory"""
    
#     print("\n-- Retreiving Files----\n")
    
#     deleteAfterCopy = False 	#set to true if you want to clean out the remote directory
#     onlyNewFiles = True			#set to true to grab & overwrite all files locally
#     moveFTPFiles(ftpServerName,ftpU,ftpP,remoteDirectoryPath,localDirectoryPath,deleteAfterCopy,onlyNewFiles)

# file transfer example
moveFTPFiles(remotePath = './CVMDS/Direct_Channel_Cashback_Recharge/', 
                 serverName = '10.132.57.198', userName ='....' ,
                 passWord ='....', localPath =  'D:/',
                 deleteRemoteFiles=False, onlyDiff=False, 
                 transFile_name_pattern='DIRECT_CHANNEL_CASHBACK_',
                 from_date = '20220905' ,
                 to_date = '20220913')
```


Option for `remote path`, `local path`, `file deletion` 
```python
# based on what I saw at http://code.activestate.com/recipes/327141-simple-ftp-directory-synch/
def moveFTPFiles(remotePath = './CV/', 
                 serverName = '10.132.57.???', userName ='...' ,
                 passWord ='...', localPath =  'E:/Reports/Cashback/',
                 deleteRemoteFiles=False, onlyDiff=False, 
                 transFile='marketplace_cashback_20perc_'):
    """Connect to an FTP server and bring down files to a local directory"""
    import os
    #from sets import Set
    from ftplib import FTP
    try:
        ftp = FTP(serverName)
    except:
        print("Couldn't find server")
    ftp.login(userName,passWord)
    ftp.cwd(remotePath)
    
    ## with file name containing date
    import datetime
    oneday = datetime.timedelta(days=1)
    yesterday = (datetime.date.today() - oneday).strftime('%Y%m%d') # 20220618
    
    transfer_file = transFile + yesterday + '.csv'
    
    try:
        print("Connecting...")
        
        if onlyDiff:
            lFileSet = set(os.listdir(localPath))
            rFileSet = set(ftp.nlst())
            transferList = list(rFileSet - lFileSet)
            print("Missing: " + str(len(transferList)))
        else:
            if transFile:
                transferList = [transfer_file]
            else:
                transferList = ftp.nlst()
        
        
        delMsg = ""	
        filesMoved = 0
        for fl in transferList:
            # create a full local filepath
            localFile = localPath + fl
            grabFile = True
            if grabFile:				
                #open a the local file
                fileObj = open(localFile, 'wb')
                # Download the file a chunk at a time using RETR
                ftp.retrbinary('RETR ' + fl, fileObj.write)
                # Close the file
                fileObj.close()
                filesMoved += 1
                
            # Delete the remote file if requested
            if deleteRemoteFiles:
                ftp.delete(fl)
                delMsg = " and Deleted"
            
        print("Files Moved" + delMsg + ": " + str(filesMoved) + " on " + timeStamp())
    except:
        print("Connection Error - " + timeStamp())
    ftp.close() # Close FTP connection
    ftp = None

def timeStamp():
    """returns a formatted current time/date"""
    import time
    return str(time.strftime("%Y%m%d")) #str(time.strftime("%a %d %b %Y %I:%M:%S %p"))


#.strftime("%F") # '2022-05-21'

# if __name__ == '__main__':
#     #--- constant connection values
#     ftpServerName = "ftpservername.com" # or IP address if Address Resulotion work on server 
#     ftpU = "ftpusername"
#     ftpP = "ftppassword"
#     remoteDirectoryPath = "remote/ftp/subdirectory"
#     localDirectoryPath = """local\sub\directory"""
    
#     print("\n-- Retreiving Files----\n")
    
#     deleteAfterCopy = False 	#set to true if you want to clean out the remote directory
#     onlyNewFiles = True			#set to true to grab & overwrite all files locally
#     moveFTPFiles(ftpServerName,ftpU,ftpP,remoteDirectoryPath,localDirectoryPath,deleteAfterCopy,onlyNewFiles)

# file transfer1
moveFTPFiles(remotePath = './CV/', 
                 serverName = '10.132.57.???', userName ='...' ,
                 passWord ='...', localPath =  'E:/Reports/Cashback/',
                 deleteRemoteFiles=False, onlyDiff=False, 
                 transFile='marketplace_cashback_20perc_')


moveFTPFiles(remotePath = './CV/', 
                 serverName = '10.132.57.???', userName ='...' ,
                 passWord ='...', localPath =  'E:/Reports/Cashback/',
                 deleteRemoteFiles=False, onlyDiff=False,  
                 transFile='DIRECT_CHANNEL_CASHBACK_')


moveFTPFiles(remotePath = './CV/', 
                 serverName = '10.132.57.???', userName ='...' ,
                 passWord ='...', localPath =  'E:/Reports/Cashback/',
                 deleteRemoteFiles=False, onlyDiff=False, 
                 transFile='DC_cashback_Recharge_Payam_')
```



### Extracting datetime related string from date time
reference for strftime : https://www.strfti.me/

## with file name containing date
```python 
oneday = datetime.timedelta(days=1)
yesterday = (datetime.date.today() - oneday).strftime('%Y%m%d') # 20220521

#.strftime("%F") # '2022-05-21'
```

### Write file to FTP
Move prepared file, 'CDM_List.xlsx', with adding date in YYYYMMDD to file name to FTP location

```python
from ftplib import FTP
from datetime import datetime

ftp = FTP('10.110.111.112') 
ftp.login(user = 'user1', passwd= '....') 
ftp.cwd('/home/defualt_reports/csv/CDM Daily Report')
# now = datetime.now() # current date and time
# month = now.strftime("%m")
# day = now.strftime("%d")
today_date = datetime.now().strftime("%Y%m%d") # make date as YYYYMMDD like '20220530'

filename = 'CDM_List-' + today_date + '.xlsx' # making file name to be 'CDM_List'
ftp.storbinary('STOR '+filename, open('CDM_List.xlsx', 'rb'))
ftp.quit()
```


```python
def writefile(ftp_add='10.110.111.112', username='user1', password='pass1', folder_add='/home/defualt_reports/csv/CDM Daily Report',file_name='CDM_List.xlsx', date_format="%Y%m%d"):
  from ftplib import FTP
  from datetime import datetime

  ftp = FTP(ftp_add) 
  ftp.login(user = username, passwd=password ) 
  ftp.cwd(folder_add)

  today_date = datetime.now().strftime(date_format) # make date as YYYYMMDD like '20220530'

  filename = file_name.split('.')[0] + '_' + today_date + file_name.split('.')[1] # adding '_YYYYMMDD' to file name
  ftp.storbinary('STOR '+filename, open(file_name, 'rb'))
  ftp.quit()
  return True

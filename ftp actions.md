### Read files from FTP
Option for `remote path`, `local path`, `file deletion` 
```python
# based on what I saw at http://code.activestate.com/recipes/327141-simple-ftp-directory-synch/
def moveFTPFiles(remotePath = '/.', serverName = '10.233.14.1',userName ='user1' ,\
                 passWord ='!QAZ',localPath =  r'D:/dump files
                 deleteRemoteFiles=False,onlyDiff= True):
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
    
    try:
        print("Connecting...")
        if onlyDiff:
            lFileSet = Set(os.listdir(localPath))
            rFileSet = Set(ftp.nlst())
            transferList = list(rFileSet - lFileSet)
            print("Missing: " + str(len(transferList)))
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
    return str(time.strftime("%a %d %b %Y %I:%M:%S %p"))

if __name__ == '__main__':
    #--- constant connection values
    ftpServerName = "ftpservername.com" # or IP address if Address Resulotion work on server 
    ftpU = "ftpusername"
    ftpP = "ftppassword"
    remoteDirectoryPath = "remote/ftp/subdirectory"
    localDirectoryPath = """local\sub\directory"""
    
    print("\n-- Retreiving Files----\n")
    
    deleteAfterCopy = False 	#set to true if you want to clean out the remote directory
    onlyNewFiles = True			#set to true to grab & overwrite all files locally
    moveFTPFiles(ftpServerName,ftpU,ftpP,remoteDirectoryPath,localDirectoryPath,deleteAfterCopy,onlyNewFiles)


moveFTPFiles()


## with file name containing date
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

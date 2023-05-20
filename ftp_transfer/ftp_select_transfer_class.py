# """ 
    # Name:           ftp_select_transfer_class.py
    # Author:         Hesam
    # Date:           April 15, 2023
    # Description:    
                     
                    # This module help us 
                    # 1. connect to remote ftp server and select files based on
                    #   criteria we want
                    # 2. transfer selected files from remote ftp to local address
                    # 

# """
def timeStamp():
    """returns a formatted current time/date"""
    import time
    return str(time.strftime("%a %d %b %Y %I:%M:%S %p")) #str(time.strftime("%a %d %b %Y %I:%M:%S %p"))


class FTP_Select_Transfer():

    def __init__(self, remotePath, serverName, userName, passWord,
                 localPath, deleteRemoteFiles, onlyDiff,
                 contains_pattern, transFile_name_pattern,
                 transFile_month_pattern, transFile_year_pattern,
                 past_n_day, from_date, to_date, file_extension):

                self.remotePath= remotePath
                self.serverName=serverName
                self.userName=userName
                self.passWord=passWord
                self.localPath=localPath
                self.deleteRemoteFiles=False
                self.onlyDiff=False
                self.contains_pattern=False
                self.transFile_name_pattern=transFile_name_pattern
                self.transFile_month_pattern=transFile_month_pattern
                self.transFile_year_pattern=transFile_year_pattern
                self.past_n_day=None
                self.from_date=from_date
                self.to_date=to_date
                self.file_extension=file_extension


    def FileSelection(self):
        import ftplib
        ftp = ftplib.FTP(self.serverName)
        ftp.login(self.userName, self.passWord)
        ftp.cwd(self.remotePath)

        # Filter the list to only include files that match the pattern
        files = ftp.nlst()
        if self.contains_pattern or self.transFile_name_pattern!='':
            transferList = [f for f in files   # os.listdir(folder_add) 
                             if f.split('-')[-1][:4] == self.transFile_year_pattern
                             and 
                             f.split('-')[-1][4:6] == self.transFile_month_pattern
                             # and
                             # f.endswith(self.file_extension) 
                             and 
                             f.find(self.transFile_name_pattern) > -1
                            ]
        else:
            transferList = [f for f in files   # os.listdir(folder_add) 
                             if f.split('-')[-1][:4] == self.transFile_year_pattern
                             and 
                             f.split('-')[-1][4:6] == self.transFile_month_pattern
                             and
                             f.endswith(self.file_extension) 
                            ]
        return transferList


    def moveFTPFiles(self, transferList):

        """Connect to an FTP server and bring down files to a local directory"""
        import os
        from datetime import date, timedelta, datetime
        #from sets import Set
        from ftplib import FTP 
        try:
            ftp = FTP(self.serverName)       # connect to host, default port
            print(ftp.getwelcome())
        except:
            print("Couldn't find server")
        ftp.login(self.userName, self.passWord)    # user login using user and pass
        # login_response = ftp.login(self.userName, self.passWord)
        # print(login_response)
        ftp.cwd(self.remotePath)             # change into "remotePath" directory
        print(ftp.pwd())
        frmt = '%Y%m%d'
        # transferList = []
        
        # try:
        print("Connecting...")
        ftp.login(self.userName, self.passWord)
        ftp.cwd(self.remotePath)
        print(f'Number of files to be transfered:{len(transferList)}')
        
        delMsg = ""	
        filesMoved = 0
        for fl in transferList:
            # create a full local filepath
            localFile = self.localPath + fl
            print(f'Working to write {localFile}  !')
            grabFile = True
            if grabFile:
                #open a the local file
                fileObj = open(localFile, 'wb')
                # Download the file a chunk at a time using RETR
                ftp.retrbinary('RETR ' + fl, fileObj.write)
                # Close the file
                fileObj.close()
                filesMoved += 1
                #print(filesMoved)
                print(f"    {localFile} moved on {timeStamp()}")
                
            # Delete the remote file if requested
            if self.deleteRemoteFiles:
                ftp.delete(fl)
                delMsg = " and Deleted"
            
                print(f"Files Moved {delMsg} : {filesMoved} on {timeStamp()}")#("Files Moved" + delMsg + ": " + str(filesMoved) + " on " + timeStamp())

        ftp.close() # Close FTP connection
        ftp = None

        # except:
        #     print("Connection Error - " + timeStamp())



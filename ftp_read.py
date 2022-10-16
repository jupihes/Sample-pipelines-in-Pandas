# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 19:21:53 2022
@author: mahdi.d
"""

# based on what I saw at http://code.activestate.com/recipes/327141-simple-ftp-directory-synch/
def moveFTPFiles(remotePath = './CVMDS/Direct_Channel_Cashback_Recharge/', 
                 serverName = '10.132.57.198',
                 userName ='' ,
                 passWord ='', 
                 localPath =  'E:/Reports/Cashback/',
                 deleteRemoteFiles=False, 
                 onlyDiff=False, 
                 transFile_name_pattern='DC_cashback_Recharge_Payam_',
                 past_n_day = None, 
                 from_date = '20220905' ,
                 to_date = '20220913'
                 ):

    """Connect to an FTP server and bring down files to a local directory"""
    import os
    #import datetime
    from datetime import date, timedelta, datetime
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
            if transFile_name_pattern:  #if transFile_name_pattern does not set, all the files in the directory will copy
                if past_n_day:
                    
                    for i in range(1, past_n_day+1):
                        temp_day = date.today() - timedelta(days = i)

                        # print(temp_day, transFile_name_pattern, sep='----\n')
                        transfer_file = f'{transFile_name_pattern}{temp_day:%Y%m%d}.csv'
                        transferList.append(transfer_file)
                else:
                   # i = 1
                    #temp_day = date.today() - timedelta(days = i)  
                    
                    from_date_formatisdate = datetime.strptime(from_date, '%Y%m%d')
                    to_date_formatisdate = datetime.strptime(to_date, '%Y%m%d')
                    daysbetween  = (to_date_formatisdate-from_date_formatisdate).days
                    
                    transferList = []
                    for i in range(daysbetween):
                        
                        formatted_temp_day = from_date_formatisdate + timedelta(days = i)
                        transfer_file = f'{transFile_name_pattern}{formatted_temp_day:%Y%m%d}.csv'
                        transferList.append(transfer_file)
                        i += 1
                        
# =============================================================================
#                         
#                         formatted_temp_day =  f'{temp_day:%Y%m%d}'
#                         #if int(from_date) <= int(formatted_temp_day) <= int(to_date):
#                         if from_date <= formatted_temp_day <= to_date:
#                             transfer_file = f'{transFile_name_pattern}{temp_day:%Y%m%d}.csv'
#                             transferList.append(transfer_file)
#                          
#                         elif formatted_temp_day == from_date:
#                             break
#                         i += 1
#                         temp_day = date.today() - timedelta(days = i)
#                         
# =============================================================================
                        
                
            else:
                transferList = ftp.nlst()
        
        print(f'File to be transfered:{transfer_file}')
        
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
            
        print(f"Files Moved {delMsg} : {filesMoved} on {timeStamp()}")#("Files Moved" + delMsg + ": " + str(filesMoved) + " on " + timeStamp())
    except:
        print("Connection Error - " + timeStamp())
    ftp.close() # Close FTP connection
    ftp = None

def timeStamp():
    """returns a formatted current time/date"""
    import time
    return str(time.strftime("%Y%m%d")) #str(time.strftime("%a %d %b %Y %I:%M:%S %p"))

#from pandas import to_datetime, Timedelta, Timestamp
from datetime import date, timedelta, datetime
def unix_day(date='20220917'):
    date = datetime.strptime( date, "%Y%m%d")# to_datetime([date])

    # calculate unix datetime
    return (date - datetime.strptime('19700101', "%Y%m%d")).days# // Timedelta('1D'))[0]

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

# moveFTPFiles(remotePath = './CVMDS/Direct_Channel_Cashback_Recharge/', 
#                  serverName = '10.132.57.198',
#                  userName ='mahdi.d' ,
#                  passWord ='_M112233$$QQWW', 
#                  localPath =  'E:/Reports/Cashback/',
#                  deleteRemoteFiles=False, 
#                  onlyDiff=False, 
#                  transFile_name_pattern='DC_cashback_Recharge_Payam_',
#                  past_n_day = None, 
#                  from_date = '20220905' ,
#                  to_date = '20220917')
                 
  # Prob Transfer
probe_file = 'ito_traffic_per_ip_'
probe_file += str(unix_day((date.today() - timedelta(days = 1)).strftime('%Y%m%d'))) + '_'

###############  sample without kwargs ###############
# moveFTPFiles(remotePath = './CVMDS/Huawei/ITO/', 
#                   serverName = '10.132.57.198',
#                   userName ='' ,
#                   passWord ='', 
#                   localPath = '//t1w022/Datascience/Prob/' ,#'//t1w022/Datascience/Prob',#'E:/Reports/Prob/',
#                   deleteRemoteFiles=False, 
#                   onlyDiff=False, 
#                   transFile_name_pattern= probe_file,
#                   past_n_day = 1, 
#                   from_date = '20220905' ,
#                   to_date = '20220917')
###############  sample with kwargs ###############
input_dict = {'remotePath' : './CVMDS/Huawei/ITO/', 
                  'serverName' : '10.132.57.198',
                  'userName' :'' ,
                  'passWord' :'', 
                  'localPath' : '//t1w022/Datascience/Prob/',
                  'deleteRemoteFiles':False, 
                  'onlyDiff': False, }


moveFTPFiles(transFile_name_pattern= probe_file,
              past_n_day = 1, **input_dict)

# moveFTPFiles(remotePath = './CVMDS/Direct_Channel_Cashback_Recharge/', 
#                  serverName = '10.132.57.198', userName ='' ,
#                  passWord ='', localPath =  'D:/',
#                  deleteRemoteFiles=False, onlyDiff=False, 
#                  transFile_name_pattern='DC_cashback_Recharge_Payam_')


# moveFTPFiles(remotePath = './CVMDS/Direct_Channel_cashback/', 
#                  serverName = '10.132.57.198', userName ='' ,
#                  passWord ='', localPath =  'D:/',
#                  deleteRemoteFiles=False, onlyDiff=False,  
#                  transFile_name_pattern='DIRECT_CHANNEL_CASHBACK_')


# moveFTPFiles(remotePath = './CVMDS/Marketplace_Cashback/', 
#                  serverName = '10.132.57.198', userName ='' ,
#                  passWord ='', localPath =  'D:/',
#                  deleteRemoteFiles=False, onlyDiff=False, 
#                  transFile_name_pattern='marketplace_cashback_20perc_')

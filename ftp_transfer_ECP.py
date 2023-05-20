# -*- coding: utf-8 -*-
"""
@author: Hesam - Created on April 4 2023
FTP read transfer modified for EPC
"""
from ftp_select_transfer_class import *

### sample 1 ###
# move '.csv' files where year='2023' and month='04'
transfer_obj = FTP_Select_Transfer(remotePath='/Marketing/ECPsharefolder/smart_com/',
                    serverName='10.132.57.198',
                    userName='hesam.mo' ,
                    passWord="_hedayatE5678",
                    localPath=r'\\t1w022\Datascience\Farzaneh\\',
                    deleteRemoteFiles=False, 
                    onlyDiff=False,
                    contains_pattern=False,
                    transFile_name_pattern='',
                    transFile_month_pattern='04',
                    transFile_year_pattern='2023',
                    past_n_day=None,
                    from_date='20230310',
                    to_date='20230315',
                    file_extension='.csv')

transfer_list=transfer_obj.FileSelection()
transfer_obj.moveFTPFiles(transfer_list)


### sample 2 ###
# identify canditated files for move with pattern='campdetails' 
# where year='2023' and month='04'
transfer_obj = FTP_Select_Transfer(remotePath='/Marketing/ECPsharefolder/smart_com/',
                    serverName='10.132.57.198',
                    userName='hesam.mo' ,
                    passWord="_hedayatE5678",
                    localPath=r'\\t1w022\Datascience\Farzaneh\\',
                    deleteRemoteFiles=False, 
                    onlyDiff=False,
                    contains_pattern=True,
                    transFile_name_pattern='campdetails',
                    transFile_month_pattern='04',
                    transFile_year_pattern='2023',
                    past_n_day=None,
                    from_date='20230310',
                    to_date='20230315',
                    file_extension='')


transfer_list1=transfer_obj.FileSelection()
# =============================================================================
# 
# def moveFTPFiles(remotePath = './CVMDS/Direct_Channel_Cashback_Recharge/', 
#                  serverName = '10.132.57.198',
#                  userName ='' ,
#                  passWord ='', 
#                  localPath =  'E:/Reports/Cashback/',
#                  deleteRemoteFiles=False, 
#                  onlyDiff=False,
#                  contains_pattern=True,
#                  transFile_name_pattern='DC_cashback_Recharge_Payam_',
#                  transFile_month_pattern='03',
#                  transFile_year_pattern='2023',
#                  past_n_day = None, 
#                  from_date = '20220905' ,
#                  to_date = '20220913'
#                  ):
# 
#     """Connect to an FTP server and bring down files to a local directory"""
#     import os
#     #import datetime
#     from datetime import date, timedelta, datetime
#     #from sets import Set
#     from ftplib import FTP 
#     try:
#         ftp = FTP(serverName)       # connect to host, default port
#         print(ftp.getwelcome())
#     except:
#         print("Couldn't find server")
#     ftp.login(userName,passWord)    # user login using user and pass
#     login_response = ftp.login(userName, passWord)
#     print(login_response)
#     ftp.cwd(remotePath)             # change into "remotePath" directory
#     print(f" We moved to {ftp.pwd()}")
# # =============================================================================   
# #     #### with file name containing date ####
# # 
# #     oneday = datetime.timedelta(days=1)     #create 1 day in datetime format
# #     yesterday = (datetime.date.today() - oneday).strftime('%Y%m%d') # make yesterday in 20220618 format
# #        
# #     transfer_file = transFile_name_pattern + yesterday + '.csv'
# # =============================================================================
#     frmt = '%Y%m%d'
#     transferList = []
#     
#     try:
#         print("Connecting...")
#         
#         if onlyDiff:
#             
#             lFileSet = set(os.listdir(localPath))
#             rFileSet = set(ftp.nlst())
#             transferList = list(rFileSet - lFileSet)
#             print("Missing: " + str(len(transferList)))
#         else:
#             
#             if transFile_name_pattern:  #if transFile_name_pattern does not set, all the files in the directory will copy
#                 if past_n_day:
#                     
#                     for i in range(1, past_n_day+1):
#                         temp_day = date.today() - timedelta(days = i)
# 
#                         # print(temp_day, transFile_name_pattern, sep='----\n')
#                         transfer_file = f'{transFile_name_pattern}{temp_day:%Y%m%d}.csv'
#                         transferList.append(transfer_file)
#             elif transFile_name_pattern == '':
#                 # i = 1
#                 #temp_day = date.today() - timedelta(days = i)  
#                  
#                 from_date_formatisdate = datetime.strptime(from_date, '%Y%m%d')
#                 to_date_formatisdate = datetime.strptime(to_date, '%Y%m%d')
#                 daysbetween  = (to_date_formatisdate-from_date_formatisdate).days
#                 
#                 transferList = []
#                 all_files = [ftp.nlst()]
# 
#                 for i in range(daysbetween+1):
#                      # pattern = "-20230314.csv"
#                      # matching_files1 = [file for file in files if pattern in file]
#                      # print (f'{i}, {formatted_temp_day},{transfer_file_pattern},{len(all_files)}')
#                      formatted_temp_day = from_date_formatisdate + timedelta(days = i)
#                      transfer_file_pattern = f'-{formatted_temp_day:%Y%m%d}.csv'
#                      matching_files = [temp_file for temp_file in all_files if temp_file.endswith(transfer_file_pattern)]
#                      transferList.append(matching_files)
#                      print (f'{i}, {formatted_temp_day},{transfer_file_pattern},{matching_files}')
#                      i += 1
# 
# 
# # =============================================================================
# #                         
# #                         formatted_temp_day =  f'{temp_day:%Y%m%d}'
# #                         #if int(from_date) <= int(formatted_temp_day) <= int(to_date):
# #                         if from_date <= formatted_temp_day <= to_date:
# #                             transfer_file = f'{transFile_name_pattern}{temp_day:%Y%m%d}.csv'
# #                             transferList.append(transfer_file)
# #                          
# #                         elif formatted_temp_day == from_date:
# #                             break
# #                         i += 1
# #                         temp_day = date.today() - timedelta(days = i)
# #                         
# # =============================================================================
#                         
# # =============================  if we do not have "transFile_name_pattern" =======================
#                 
#             #else:
#                 # if contains_pattern=False:
#                     # pass
#                 # if from_date = None and to_date =None:
#                     # transferList = ftp.nlst()
#             else: #if  transFile_name_pattern == '' and contains_pattern and (transFile_month_pattern!='' or transFile_year_pattern!=''):
#                 print('We are here!')
#                 transferList = []
#                 all_files = [ftp.nlst()] #           remotePath
#                 transferList = [f for f in all_files   # os.listdir(folder_add) 
#                                  if f.split('-')[-1][:4] == transFile_year_pattern and 
#                                  f.split('-')[-1][4:6] == transFile_month_pattern
#                                  f.endswith('.csv') # file_extension
#                                  ]
# # ====================================================
#         
#         print(f'File to be transfered:{transfer_file}')
#         print(f" number of files {len(transferList)}")
#         delMsg = ""	
#         filesMoved = 0
#         for fl in transferList:
#             # create a full local filepath
#             localFile = localPath + fl
#             grabFile = True
#             if grabFile:				
#                 #open a the local file
#                 fileObj = open(localFile, 'wb')
#                 # Download the file a chunk at a time using RETR
#                 ftp.retrbinary('RETR ' + fl, fileObj.write)
#                 # Close the file
#                 fileObj.close()
#                 filesMoved += 1
#                 
#             # Delete the remote file if requested
#             if deleteRemoteFiles:
#                 ftp.delete(fl)
#                 delMsg = " and Deleted"
#             
#         print(f"Files Moved {delMsg} : {filesMoved} on {timeStamp()}")#("Files Moved" + delMsg + ": " + str(filesMoved) + " on " + timeStamp())
#     except:
#         print("Connection Error - " + timeStamp())
#     ftp.close() # Close FTP connection
#     ftp = None
#     return True
# 
# def timeStamp():
#     """returns a formatted current time/date"""
#     import time
#     return str(time.strftime("%a %d %b %Y %I:%M:%S %p")) #str(time.strftime("%a %d %b %Y %I:%M:%S %p"))
# 
# #from pandas import to_datetime, Timedelta, Timestamp
# from datetime import date, timedelta, datetime
# def unix_day(date='20220917'):
#     date = datetime.strptime( date, "%Y%m%d")# to_datetime([date])
# 
#     # calculate unix datetime
#     return (date - datetime.strptime('19700101', "%Y%m%d")).days# // Timedelta('1D'))[0]
# 
# #.strftime("%F") # '2022-05-21'
# 
# moveFTPFiles(remotePath='/Marketing/ECPsharefolder/smart_com/',
#             serverName='10.132.57.198',
#             userName='hesam.mo' ,
#             passWord="_hedayatE5678",
#             localPath='//t1w022/Datascience/Farzaneh/',
#             deleteRemoteFiles=False, 
#             onlyDiff=False,
#             contains_pattern=True,
#             transFile_name_pattern='',
#             transFile_month_pattern='04',
#             transFile_year_pattern='2023',
#             past_n_day=None,
#             from_date='20230310' ,
#             to_date='20230315')
# 
# # =============================================================================
# # 
# # 
# # # userName='mahdi.d' ,
# # # passWord="@Mahdi112233$$",
# # 
# # # if __name__ == '__main__':
# # #     #--- constant connection values
# # #     ftpServerName = "ftpservername.com" # or IP address if Address Resulotion work on server 
# # #     ftpU = "ftpusername"
# # #     ftpP = "ftppassword"
# # #     remoteDirectoryPath = "remote/ftp/subdirectory"
# # #     localDirectoryPath = """local\sub\directory"""
# #     
# # #     print("\n-- Retreiving Files----\n")
# #     
# # #     deleteAfterCopy = False 	#set to true if you want to clean out the remote directory
# # #     onlyNewFiles = True			#set to true to grab & overwrite all files locally
# # #     moveFTPFiles(ftpServerName,ftpU,ftpP,remoteDirectoryPath,localDirectoryPath,deleteAfterCopy,onlyNewFiles)
# # 
# # # file transfer1
# # 
# # # moveFTPFiles(remotePath = './CVMDS/Direct_Channel_Cashback_Recharge/', 
# # #                  serverName = '10.132.57.198',
# # #                  userName ='mahdi.d' ,
# # #                  passWord ='_M112233$$QQWW', 
# # #                  localPath =  'E:/Reports/Cashback/',
# # #                  deleteRemoteFiles=False, 
# # #                  onlyDiff=False, 
# # #                  transFile_name_pattern='DC_cashback_Recharge_Payam_',
# # #                  past_n_day = None, 
# # #                  from_date = '20220905' ,
# # #                  to_date = '20220917')
# #                  
# # ####### Prob Transfer #######
# # # probe_file = 'ito_traffic_per_ip_'
# # # probe_file += str(unix_day((date.today() - timedelta(days = 1)).strftime('%Y%m%d'))) + '_'
# # 
# # 
# # 
# # 
# # ###############  sample without kwargs ###############
# # # moveFTPFiles(remotePath = './CVMDS/Huawei/ITO/', 
# # #                   serverName = '10.132.57.198',
# # #                   userName ='' ,
# # #                   passWord ='', 
# # #                   localPath = '//t1w022/Datascience/Prob/' ,#'//t1w022/Datascience/Prob',#'E:/Reports/Prob/',
# # #                   deleteRemoteFiles=False, 
# # #                   onlyDiff=False, 
# # #                   transFile_name_pattern= probe_file,
# # #                   past_n_day = 1, 
# # #                   from_date = '20220905' ,
# # #                   to_date = '20220917')
# # ###############  sample with kwargs ###############
# # 
# # 
# # 
# # # moveFTPFiles(remotePath = './Marketing/ECPsharefolder/smart_com/',
# # #                  serverName = '10.132.57.198', userName ='mahdi.d' ,
# # #                  passWord ='@Mahdi112233$$', localPath = '//t1w022/Datascience/Farzaneh/',
# # #                  deleteRemoteFiles=False, onlyDiff=False, 
# # #                  transFile_name_pattern='')
# # 
# # # moveFTPFiles(transFile_name_pattern= probe_file,
# # #               past_n_day = 1, **input_dict)
# # 
# # # input_dict = {'remotePath' : '/Marketing/ECPsharefolder/smart_com/',
# # #                 'serverName' : '10.132.57.198',
# # #                 'userName' :'mahdi.d' ,
# # #                 'passWord' :"@Mahdi112233$$",
# # #                 'localPath' : '//t1w022/Datascience/Farzaneh/',
# # #                 'deleteRemoteFiles':False, 
# # #                 'onlyDiff': False,
# # #                 'contains_pattern':False,
# # #                 'transFile_name_pattern':'',
# # #                 'past_n_day':None,
# # #                 'from_date':'20230310' ,
# # #                 'to_date':'20230313'}
# # 
# # # moveFTPFiles(input_dict)
# # 
# # 
# # 
# # import ftplib
# # 
# # ftp = ftplib.FTP("10.132.57.198")
# # ftp.login("mahdi.d", "@Mahdi112233$$")
# # remotePath = "/Marketing/ECPsharefolder/smart_com/"
# # 
# # ftp.cwd(remotePath)
# # 
# # # Filter the list to only include files that match the pattern
# # files = ftp.nlst()
# # 
# # transferList = [f for f in files   # os.listdir(folder_add) 
# #                  if f.split('-')[-1][:3] == transFile_year_pattern and 
# #                  f.split('-')[-1][5:6] == transFile_month_pattern
# #                  #f.endswith(file_extension) 
# #                 ]
# # 
# # 
# # 
# # 
# # transferList = [f for f in files   # os.listdir(folder_add) 
# #                  if f.split('-')[-1][:4] == transFile_year_pattern and 
# #                  f.split('-')[-1][4:6] == transFile_month_pattern
# #                  and f.split('.')[-1] == 'csv'  # f.endswith(file_extension) 
# #                  ]
# # 
# # wrongfileList = [f for f in files   # os.listdir(folder_add) 
# #                  if f.split('-')[-1] == f 
# #                  and len((f.split('-')[-1]).split('.')[0]) != 8
# #                  
# #                  # or (f.split('-')[-1]).split('.')[-1] != 'csv' 
# #                  # or (f.split('-')[-1]).split('.')[-1] != 'xlsx'
# # 
# #                  ]
# # 
# # 
# # from pandas import DataFrame
# # df = DataFrame(files, columns=['file_name'])
# # 
# # df['date_part'] = df.file_name.str.contains(r'-\d{8}.')
# # df['exten_part'] = df.file_name.str.contains(r'.\w{3,4}')
# # 
# # df['date_value'] = df.file_name.str.extract(r'(-\d{8}.)')
# # df['exten_value'] = df.file_name.str.extract(r'(\.\w{3,4})')
# # 
# # 
# # # pattern = "-20230314.csv"
# # # matching_files = [file for file in files if pattern in file]
# # 
# # # # matching_files2 = [file.split('/')[-1] for file in matching_files ]
# # 
# # # # # Print the list of matching files
# # # print(matching_files)
# # 
# # # # for name in ftp.nlst(path):
# # # #     print(name);
# # # #     filenames = []
# # # #     ftp.retrlines('LIST', lambda line: filenames.append(line.split()[-1]))
# # # #     print(filenames);
# # 
# # # 8247248452298885717-20230314.csv
# # #                    -20230314.csv
# # 
# # =============================================================================
# 
# =============================================================================

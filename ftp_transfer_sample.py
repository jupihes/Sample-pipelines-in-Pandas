from ftp_select_transfer_class import *

### sample 1 ###
# move '.csv' files where year='2023' and month='04'
transfer_obj = FTP_Select_Transfer(remotePath='/Marketing/ECPsharefolder/smart_com/',
                    serverName='10.132.57.198',
                    userName='user_name' ,
                    passWord="password",
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
                    userName='user_name' ,
                    passWord="password",
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


transfer_list1 = transfer_obj.FileSelection()

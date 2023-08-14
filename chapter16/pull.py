import pandas as pd
from sqlalchemy import create_engine,inspect
from datetime import datetime
from ftplib import FTP
import os
from apscheduler.schedulers.blocking import BlockingScheduler
#数据库类型://用户名:密码@主机IP:端口/数据库名称
db='postgresql://cveo:cveo123456@192.168.59.123:32767/postgres'
#服务器
ftpp='ftp.ptree.jaxa.jp'
#用户名
user='dyk878967_gmail.com'
#密码
passwd='SP+wari8'
#路径前缀
front_file='/pub/himawari/L2/WLF/010/'

def postdb(filename,table_name):
    engine=create_engine(db)
    dataframe = pd.read_csv(filename,skiprows=1,delimiter=',(?![^\(]*[\)])',engine='python')
    dataframe.to_sql(table_name, engine, if_exists='replace', index=False)

def is_exist(table_name):

    engine=create_engine(db)
    inspector = inspect(engine)
    if inspector.has_table(table_name):
        return True
    else:
        return False
    
def time_filename():
    now = datetime.now()
    y_m = now.strftime("%Y%m")
    day = now.strftime("%d")
    h=now.strftime("%H")
    return y_m, day, h

def get_filename(line, filenames):
    # 解析每行获取文件名
    parts = line.split(maxsplit=8)
    if len(parts) > 8:
        filename = parts[-1]
        filenames.append(filename)

# def download(filename,y_m,day,h):
#     try: os.mkdir(rf'./{y_m}/{day}/{h}')
#     except:pass
#     savefile=rf'./{y_m}/{day}/{h}/' + filename
#     ftp.retrbinary('RETR ' + filename, open(savefile, 'wb').write)

def start():
    days=[]
    #/pub/himawari/L2/WLF/bet/201508/01/02
    ftp = FTP(ftpp)
    ftp.login(user=user, passwd=passwd)
    y_m,day,h=time_filename()
    #进入工作路径
    # print(front_file + y_m + '/' + day )
    ftp.cwd(front_file + y_m + '/' + day )
    #将目录下的文件名放到days列表中
    ftp.retrlines('LIST',lambda line: get_filename(line, days))
    for hour in days:
        hours=[]
        ftp.cwd(front_file + y_m + '/' + day + '/' + hour)
        ftp.retrlines('LIST',lambda line: get_filename(line, hours))
        
        for file in hours:

            if is_exist(file):
                pass
            else :
                # download(file,y_m,day,h)
                os.makedirs(rf'./{y_m}/{day}/{hour}',exist_ok=True)
                savefile=rf'./{y_m}/{day}/{hour}/' + file
                ftp.retrbinary('RETR ' + file, open(savefile, 'wb').write)
                postdb(rf'./{y_m}/{day}/{hour}/' + file,file)
                #os.remove(f'./{y_m}/{day}/{hour}/' + file)
    # 关闭连接
    # print(days,hours)
    ftp.quit()

start()
if __name__ == '__main__':
        scheduler = BlockingScheduler()
        scheduler.add_job(start, "interval", seconds=600)
        scheduler.start()

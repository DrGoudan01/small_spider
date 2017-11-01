#__author__ = 'li'
# -*- coding:utf-8 -*-
import sqlite3
#sqlite3是一个数据库相关库
base_dir = input()
#输入一个数据库文件的地址，格式为*.sqlite3.db
table_name = "course_info"
#定义一个表格创建函数
def create_table():
    sql3_db = sqlite3.connect(base_dir)
    #链接一个数据库文件
    create_sql = "create table {} if not exists {} (url varchar(1024), title varchar(256) PREMARY KEY ,\
 teacher varchar(128),\
 study_num int, tag varchar(256), types varchar(256), \
 info varchar(1024), tests_name varchar(1024)) "
    #写入一个sql创建语句
    try :
        sql3_db.execute(create_sql.format(table_name,table_name))
    except:
        return False
    sql3_db.close()#关闭保存

#定义一个对数据进行插入，更新和查询的函数
#查询函数，以title为输入
def get_info_from_db (title):
    sql3_db = sqlite3.connect(base_dir)
    query_sql = "select * from {} where title = '{}'".format(table_name,title)
    #创建一个查询游标
    cu= sql3_db.cursor()
    cu.execute(query_sql)
    #从游标中获取数据，因为游标的特性，会随着数据下移,这里使用cursor自带的fetchone（），fetchmany（），fetchall（）来控制游标
    record_list = cu.fetchall()
    if len(record_list)>0:
        #即数据存在，那么输出真，否则输出假
        return True
    else:
        return False

#主体部分
#进行一个创建操作，再通过查询语句选择更新还是插入
create_table()
if get_info_from_db(title={}):
    sql3_db = sqlite3.connect(base_dir)
    update_sql = "update {} set study_num={}, info='{}', tests_name='{}', url='{}' where title='{}'"
    try:
        sql3_db.execute(update_sql)
        sql3_db.commit()
        #提交数据
    except:
        print("update commit false")
    sql3_db.close()
    print("uodate successful")
else:
    #如果查询不到数据存在
    sql3_db = sqlite3.connect(base_dir)
    insert_sql = "insert into {} (url, title, teacher, study_num, tag, types, info, tests_name) values('{}', '{}', '{}', {}, '{}', '{}', '{}', '{}')"
    try:
        sql3_db.execute(insert_sql)
        sql3_db.commit()
    except:
        print ("inset commit false")
    sql3_db.close()
    print("inset successful")

#下面是主要的example
#在主体代码中调用此函数
import sqlite3

base_url = "/home/shiyanlou/Desktop/shiyanlou_spider.sqlite3.db"
table_name = "course_info"

def create_table():
    sql3_db = sqlite3.connect(base_url)
    create_sql = "create table {} (url varchar(1024), title varchar(256), teacher varchar(128), study_num int, tag varchar(256), types varchar(256), info varchar(1024), tests_name varchar(1024))".format(table_name)
    try:
        sql3_db.execute(create_sql)
    except:
        return False
    sql3_db.close()
    return True

def insert_or_update_data(url, title, teacher, study_num, tag, types, info, tests_name):
    create_table() # 创建一次数据库，没有表格时创建，表格存在时不作操作
    if query(title): # 如果查询到title存在，则是更新
        sql3_db = sqlite3.connect(base_url)
        update_sql = "update {} set study_num={}, info='{}', tests_name='{}', url='{}' where title='{}'".format(table_name, study_num, info, tests_name, url, title)
        try:
            sql3_db.execute(update_sql)
            sql3_db.commit()
        except:
            return False
        sql3_db.close()
        return True
    else: # 查询不到title，则插入
        sql3_db = sqlite3.connect(base_url)
        insert_sql = "insert into {} (url, title, teacher, study_num, tag, types, info, tests_name) values('{}', '{}', '{}', {}, '{}', '{}', '{}', '{}')".format(table_name,url, title, teacher, study_num, tag, types, info, tests_name)
        try:
            sql3_db.execute(insert_sql)
            sql3_db.commit()
        except:
            return False
        sql3_db.close()
        return True
    return False

def query(title):
    sql3_db = sqlite3.connect(base_url)
    query_sql = "select * from {} where title = '{}'".format(table_name, title)
    cu = sql3_db.cursor()
    cu.execute(query_sql)
    record_list = cu.fetchall()
    if len(record_list)>0:
        return True
    else:
        return False
    return False












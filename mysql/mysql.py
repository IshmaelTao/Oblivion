"""
mysql.py
pymysql操作数据库基本流程演示
"""

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='ty518518',
                     database='student',
                     charset='utf8')

# 获取游标（操作数据库，执行sql语句）
cur = db.cursor()

# 执行sql语句
sql = "insert into class values (7,'Emma',20,159,'w',90.0,'18044345845','2019/06/07');"
sql = "insert into class values (8,'Yamamoto',21,175,'m',88.0,'17372528050','2019/04/07');"

cur.execute(sql)  # 执行语句

db.commit()  # 将写操作提交，多次写操作一同提交也可以

# 关闭数据库
cur.close()
db.close()
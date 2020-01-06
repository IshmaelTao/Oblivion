"""
save_image.py
二进制文件存储演示
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

# 存储图片
# with open('woman.jpg','rb') as f:
#     data = f.read()
# try:
#     sql = "update class set image = %s where name = 'Catholine';"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

# 获取图片
sql = "select * from class where name = 'Catholine';"
cur.execute(sql)
data = cur.fetchone()
with open('get_pic.jpg','wb')as f:
    f.write(data[0])


# 关闭数据库
cur.close()
db.close()


"""
将单词表存入数据库

1.创建数据库 dict (utf8)
2.创建数据表 words 将单词和单词解释分别存入不同的字段
3.将单词存入words单词表 超过19500 即可
"""

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='ty518518',
                     database='dict',
                     charset='utf8')

# 获取游标（操作数据库，执行sql语句）
cur = db.cursor()
# 写数据库
try:
    # 打开字典文件
    f = open('dict.txt', 'r+')
    while True:
        # 循环读取每一行
        each_line = f.readline()
        # 分割单词与释义
        list_ = each_line.split(' ',1)
        try:
            list_[1] = list_[1].strip()
            word, description = list_[0], list_[1]
        except IndexError:
            break
        if not each_line:
            break
        # 写入到dict数据库
        sql = "insert into words (word,description) " \
              "values (%s,%s)"
        cur.execute(sql,[word,description])

        db.commit()
except Exception as e:
    db.rollback()  # 退回到commit执行之前的状态
    print(e)


# 关闭数据库
cur.close()
db.close()


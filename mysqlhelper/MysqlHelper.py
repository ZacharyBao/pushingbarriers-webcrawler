import pymysql
import datetime

def connectdb():
    print("connecting to Mysql")
    db = pymysql.connect('localhost', 'root', 'root', 'PB')
    print("successfully connected")
    return db


def closedb(db):
    db.close()


def insertdb(db, gamesInfo):
    cursor = db.cursor()
    sql="INSERT INTO game(game_team,game_round, game_date, game_time, game_venue, game_address, game_opposition) VALUES (%s, %s, %s,%s, %s, %s,%s)"
    param=[]
    for ele in gamesInfo:
        param.append([ele.get_team(), ele.get_rnd(), ele.get_date(), ele.get_time(), ele.get_venue(), ele.get_address(), ele.get_opposition()])
    try:
        cursor.executemany(sql, param)
        db.commit()
        print("insert successfully!")
    except Exception as e:
        print("fail to insert data!")
        print(e)
        db.rollback()

def truncatedb(db):
    cursor=db.cursor()
    sql="TRUNCATE TABLE game"
    try:
        cursor.execute(sql)
        db.commit()
        print("truncate successfully!")
    except Exception as e:
        print("fail to truncate data!")
        print(e)
        db.rollback()

def setUpdateTime(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM gameupdatetime")
    today = datetime.datetime.now();
    if(len(cursor.fetchall())==0):
        sql="INSERT INTO gameupdatetime(gameupdatetime_date) VALUE (%s)"
        try:
            cursor.execute(sql,today)
            db.commit()
            print("Insert updatetime successfully!")
        except Exception as e:
            print("fail to insert updatetime!")
            print(e)
            db.rollback()
    else:
        sql="UPDATE gameupdatetime SET gameupdatetime_date = '%s' WHERE gameupdatetime_id = %d"%(datetime.datetime.strftime(today, "%Y/%m/%d"),1)
        try:
            cursor.execute(sql)
            db.commit()
            print("update updatetime successfully!")
        except Exception as e:
            print("fail to update updatetime!")
            print(e)
            db.rollback()
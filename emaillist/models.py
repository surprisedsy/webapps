import MySQLdb
from webapps.settings import DATABASES


def connect():
    try:
        conn = MySQLdb.connect(host=DATABASES['default']['HOST'],
                               port=int(DATABASES['default']['PORT']),
                               user=DATABASES['default']['USER'],
                               password=DATABASES['default']['PASSWORD'],
                               db=DATABASES['default']['NAME'],
                               charset='utf8')
        return conn

    except MySQLdb.Error as e:
        print("Error {0}: {1}".format(e.args[0], e.args[1]))
        return None


def fetchall():
    try:
        conn = connect()
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)

        # sql문 실행
        sql = """ select no, first_name, last_name, email
                    from emaillist
                order by no desc """
        cursor.execute(sql)

        # 결과 받아오기(fetch)
        results = cursor.fetchall()  # fetchall -> while 무한루프 안돌아도 됨

        # 자원 정리
        cursor.close()
        conn.close()

        return results

    except MySQLdb.Error as e:
        print("Error {0}: {1}".format(e.args[0], e.args[1]))
        return None
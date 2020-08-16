import pymysql.cursors
from domain import MemberDomain as dm

class MemberStore:
    con = None
    def __init__(self):
        MemberStore.con = pymysql.connect(host='localhost',
                                    port=3306,
                                    user='aiadmin',
                                    password='aiadmin',
                                    db='club',
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor) 

    # 연결 끊기
    def close(self):
        MemberStore.con.close()

    # 이메일, 패스워드 확인
    def login_ok(self,email,passwd):
        try:
            with MemberStore.con.cursor() as cursor:
                if bool(email) and bool(passwd):
                    sql = "select `email` from `member` where `email`=%s and `passwd`=%s"
                    cursor.execute(sql,(email,passwd))
                    result = cursor.fetchone()
        finally:
            pass
        return result
    
    # 이메일 검증
    def email_Validation(self,email):
        try:
            with MemberStore.con.cursor() as cursor:
                if bool(email):
                    print("이메일검증 sql문 위",email)
                    sql = "select `email` from `member` where `email`=%s"
                    cursor.execute(sql,email)
                    result = cursor.fetchone()
                print("이메일검증 result",result)
                return result
        finally:
            pass

    # 유저 등록
    def insert_member(self,entity):
        try:
            with MemberStore.con.cursor() as cursor:
                print("store",entity.u_email)
                sql = "insert into `member` (`email`,`passwd`,`name`,`nickname`,`phonenumber`,`birthday`,`address`) values (%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (entity.u_email, entity.u_passwd, entity.u_name, entity.u_nick_name, entity.u_phone_number, entity.u_birthday, entity.u_address))
                MemberStore.con.commit()
                return True
        finally:
            pass
    # 유저 수정
    def update_member(self,email,passwd,nickname,phonenumber,address):
        print("유저 수정",email)
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "update `member` set `passwd`=%s, `nickname`=%s, `phonenumber`=%s, `address`=%s where `email`=%s"
                cursor.execute(sql, (passwd, nickname, phonenumber, address, email))
                MemberStore.con.commit()
        finally:
            pass
        return 1
    # 유저 탈퇴
    def delete_member(self,email):
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "delete from `member` where `email`=%s"
                cursor.execute(sql,email)
                MemberStore.con.commit()
        finally:
            pass
        return 1

    # 유저 정보
    def select_one_member(self,email):
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "select * from `member` where `email`=%s"
                cursor.execute(sql,(email))
                result = cursor.fetchone()
        finally:
            pass
        return result
    

from django.db import models
import cx_Oracle

# Create your models here.

class Usuario(models.Model):
    def __str__(self, usuario_id):
        self.usuario_id = usuario_id

    @classmethod
    def getUsers(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select user_id, usuario, pass, type_name, nombre, apellido, estado from usuarios join user_type on usuarios.tipo = user_type.type_id')
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({column[0]:r[0], column[1]:r[1], column[2]:r[2], column[3]:r[3], column[4]:r[4], column[5]:r[5], column[6]:r[6]})
        cur.close()
        con.close()
        return array
    @classmethod
    def getUser(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select * from usuarios where user_id ='+id)
        res = cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0]:res[0], column[1]:res[1], column[2]:res[2], column[3]:res[3], column[4]:res[4], column[5]:res[5], column[6]:res[6]}
        cur.close()
        con.close()
        return obj
    @classmethod
    def createUser(self, user, password, user_type, name, last_name, status):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("create_user",[user, password, user_type, name, last_name, status])
        cur.close()
        con.close()
    def updateUser(id, user, password, user_type, name, last_name, status):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("update_user",[id, user, password, user_type, name, last_name, status])
        cur.close()
        con.close()
    @classmethod
    def deleteUser(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("delete_user",[id])
        cur.close()
        con.close()
    
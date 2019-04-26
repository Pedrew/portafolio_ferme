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
        cur.execute('select user_id, usuario, pass, type_name, nombre, apellido, estado, rut from usuarios join user_type on usuarios.tipo = user_type.type_id')
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({column[0]:r[0], column[1]:r[1], column[2]:r[2], column[3]:r[3], column[4]:r[4], column[5]:r[5], column[6]:r[6], column[7]:r[7]})
        cur.close()
        con.close()
        return array
    @classmethod
    def getUser(self, id, type):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        if type == "proveedor":
            cur.execute('select user_id, usuario, pass, type_name, nombre, apellido, estado, rut, identificador, razon_social, rubro, telefono from usuarios join user_type on usuarios.tipo = user_type.type_id join proveedor on usuarios.user_id = proveedor.proveedor_id where user_id ='+id)
        else:
            cur.execute('select user_id, usuario, pass, type_name, nombre, apellido, estado, rut from usuarios join user_type on usuarios.tipo = user_type.type_id where user_id ='+id)            
        res = cur.fetchone()
        column = [row[0] for row in cur.description]
        if type == "proveedor":
            obj = {column[0]:res[0], column[1]:res[1], column[2]:res[2], column[3]:res[3], column[4]:res[4], column[5]:res[5], column[6]:res[6], column[7]:res[7], column[8]:res[8], column[9]:res[9], column[10]:res[10], column[11]:res[11]}
        else:
            obj = {column[0]:res[0], column[1]:res[1], column[2]:res[2], column[3]:res[3], column[4]:res[4], column[5]:res[5], column[6]:res[6], column[7]:res[7]}            
        cur.close()
        con.close()
        return obj
    @classmethod
    def createUser(self, user, password, user_type, name, last_name, status, rut, rubro, telefono, razon_social, identificador):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        if user_type == "4":
            cur.callproc("create_user",[user, password, user_type, name, last_name, status, rut])
            cur.callproc("create_proveedor",[rubro, telefono, razon_social, identificador])
        else:
            cur.callproc("create_user",[user, password, user_type, name, last_name, status, rut])
        cur.close()
        con.close()
    @classmethod    
    def updateUser(self, id, user, password, user_type, name, last_name, status, rut):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("update_user",[id, user, password, user_type, name, last_name, status, rut])
        cur.close()
        con.close()
    @classmethod
    def deleteUser(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("delete_user",[id])
        cur.callproc("delete_proveedor",[id])
        cur.close()
        con.close()
    
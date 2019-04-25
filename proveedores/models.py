from django.db import models
import cx_Oracle

# Create your models here.

class Proveedor(models.Model):
    def __str__(self, proveedor_id, nombre, rut, mail, telefono):
        self.proveedor_id = proveedor_id
        self.nombre = nombre
        self.rut = rut
        self.mail = mail
        self.telefono = telefono

    @classmethod
    def getProveedores(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select * from proveedor')
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({column[0] :r[0], column[1]:r[1],column[2]:r[2],column[3]:r[3],column[4]:r[4]})
        cur.close()
        con.close()
        return array

    @classmethod
    def getProveedor(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select * from proveedor where proveedor_id ='+id)
        res = cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1],column[2]:res[2],column[3]:res[3],column[4]:res[4]}
        cur.close()
        con.close()
        return obj

    @classmethod
    def createProveedor(self, nombre, rut, mail, telefono):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("create_proveedor",[nombre,rut,mail,telefono])
        cur.close()
        con.close()

    @classmethod 
    def updateProveedor(self,id, nombre, rut, mail, telefono):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("update_proveedor",[id,nombre,rut,mail,telefono])
        cur.close()
        con.close()
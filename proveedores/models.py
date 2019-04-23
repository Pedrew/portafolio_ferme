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
            array.append({column[0] :r[0], column[1]:r[1],column[2]:r[2]})
        cur.close()
        con.close()
        return array

from django.db import models
import cx_Oracle

# Create your models here.

class Product(models.Model):
    def __init__(self, producto_id, nombre, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.precio = precio

    @classmethod
    def getProductos(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select * from products')
        res = cur.fetchall()
        cur.close()
        con.close()
        return res
from django.db import models
import cx_Oracle

# Create your models here.

class Product(models.Model):
    def __str__(self, producto_id, nombre, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.precio = precio

    @classmethod
    def getProductos(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select * from products')
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res :
            array.append({column[0] :r[0], column[1]:r[1],column[2]:r[2]})
        cur.close()
        con.close()
        return array
    @classmethod
    def createProduct(self, nombre, valor):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("create_product",[nombre,valor])
        cur.close()
        con.close()
    @classmethod
    def deleteProduct(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("delete_product",[id])
        cur.close()
        con.close()
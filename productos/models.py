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
        for r in res:
            array.append({column[0] :r[0], column[1]:r[1],column[2]:r[2], column[3]:r[3],column[4]:r[4]})
        cur.close()
        con.close()
        return array
    @classmethod
    def getProduct(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select * from products where producto_id ='+id)
        res = cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1],column[2]:res[2], column[3]:res[3],column[4]:res[4],column[5]:res[5]}
        cur.close()
        con.close()
        return obj
    @classmethod
    def createProduct(self, id, nombre, valor, stock, stock_critico, codigo_tipo):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("create_product",[id, nombre,valor, stock, stock_critico, codigo_tipo])
        cur.close()
        con.close()
    @classmethod
    def updateProduct(self, id, nombre, valor, stock, stock_critico):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("update_product",[id,nombre,valor, stock, stock_critico])
        cur.close()
        con.close()
    @classmethod
    def deleteProduct(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("delete_product",[id])
        cur.close()
        con.close()
    @classmethod    
    def getProveedores(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select proveedor_id, identificador from proveedor')
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({column[0] :r[0],column[1] :r[1]})
        cur.close()
        con.close()
        print(array)
        return array
    @classmethod
    def getFamilias(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select id_familia, familia_producto.identificador as iden_familia, detalle, proveedor.identificador as iden_prov from familia_producto join proveedor on familia_producto.id_prov = proveedor.proveedor_id')
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({column[0] :r[0], column[1]:r[1],column[2]:r[2], column[3]:r[3]})
        cur.close()
        con.close()
        return array
    @classmethod
    def createFamilia(self, identificador, nombre, id_proveedor):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("create_familia",[identificador, nombre, id_proveedor])
        cur.close()
        con.close()
    @classmethod
    def getTipos(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select * from familia_tipo')
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({column[0] :r[0], column[1]:r[1],column[2]:r[2],column[3]:r[3]})
        cur.close()
        con.close()
        return array
    @classmethod
    def createTipo(self, identificador, nombre, id_familia):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("create_tipo_familia",[identificador, nombre, id_familia])
        cur.close()
        con.close()
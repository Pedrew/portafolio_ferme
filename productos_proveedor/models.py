from django.db import models
import cx_Oracle

# Create your models here.

class Product_proveedor(models.Model):
    @classmethod
    def getProductos(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select producto_id, nombre, valor, id_prod, codigo_tipo, identificador, proveedor.razon_social as iden_rz from products_proveedor join proveedor on products_proveedor.id_prov = proveedor.proveedor_id order by nombre')
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({
                column[0] :r[0],
                column[1] :r[1],
                column[2] :r[2],
                column[3] :r[3],
                column[4] :r[4],
                column[5] :r[5],
                column[6] :r[6]
            })
        cur.close()
        con.close()
        return array
    @classmethod
    def getProduct(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select * from products_proveedor where id_prod ='+id)
        res = cur.fetchone()
        column = [row[0] for row in cur.description]
        # obj = {column[0] :res[0], column[1]:res[1],column[2]:res[2], column[3]:res[3],column[4]:res[4],column[5]:res[5],column[6]:res[6],column[7]:res[7]}
        obj = {column[0] :res[0], column[1]:res[1],column[2]:res[2], column[3]:res[3],column[4]:res[4],column[5]:res[5]}
        cur.close()
        con.close()
        return obj
    @classmethod
    def createProduct(self, id, nombre, valor, codigo_tipo, id_proveedor):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("create_product_proveedor",[id, nombre,valor, codigo_tipo, id_proveedor])
        cur.close()
        con.close()
    @classmethod
    def updateProduct(self, id, nombre, valor):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("update_product_proveedor",[id,nombre,valor])
        cur.close()
        con.close()
    @classmethod
    def deleteProduct(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("delete_product_proveedor",[id])
        cur.close()
        con.close()
    @classmethod    
    def getProveedores(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select proveedor_id, identificador, razon_social from proveedor')
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({
                column[0] :r[0].upper(),
                column[1] :r[1].upper(),
                column[2] :r[2].upper()
            })
        cur.close()
        con.close()
        print(array)
        return array
    @classmethod
    def getFamilias(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select id_familia, familia_producto.identificador as iden_familia, detalle, proveedor.identificador as iden_prov, proveedor.razon_social as iden_rz from familia_producto join proveedor on familia_producto.id_prov = proveedor.proveedor_id')
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({
                column[0] :r[0],
                column[1] :r[1],
                column[2] :r[2],
                column[3] :r[3],
                column[4] :r[4]
            })
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
        cur.execute('select id_tipo, codigo_tipo, descripcion, identificador, id_prov from familia_tipo join familia_producto on familia_tipo.id_familia = familia_producto.id_familia order by descripcion')
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({column[0] :r[0], column[1]:r[1],column[2]:r[2],column[3]:r[3],column[4]:r[4]})
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
    @classmethod
    def getProveedorId(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select proveedor_id, identificador from proveedor where proveedor_id ='+id)
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({column[0] :r[0], column[1]:r[1]})
        cur.close()
        con.close()
        return array
    
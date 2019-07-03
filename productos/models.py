from django.db import models
import cx_Oracle

# Create your models here.

class Product(models.Model):
    @classmethod
    def getProductos(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select producto_id, nombre, valor, id_prod, codigo_tipo, stock, stock_critico, razon_social from products join proveedor on products.id_prov = proveedor.proveedor_id')
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({column[0] :r[0], column[1]:r[1],column[2]:r[2], column[3]:r[3],column[4]:r[4],column[5]:r[5],column[6]:r[6],column[7]:r[7]})
        cur.close()
        con.close()
        return array
    @classmethod
    def getProduct(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select * from products where id_prod ='+id)
        res = cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1],column[2]:res[2], column[3]:res[3],column[4]:res[4],column[5]:res[5],column[6]:res[6],column[7]:res[7]}
        cur.close()
        con.close()
        return obj
    @classmethod    
    def getTipo(self,id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select descripcion, detalle from familia_tipo join familia_producto on familia_tipo.id_familia = familia_producto.id_familia where id_tipo ='+id)
        res = cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1]}
        cur.close()
        con.close()
        return obj
    @classmethod
    def createProduct(self, id, nombre, valor, codigo_tipo, id_proveedor):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("create_Product",[id, nombre,valor, codigo_tipo, id_proveedor])
        cur.close()
        con.close()
    @classmethod
    def updateProduct(self, id, nombre, valor):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("update_Product",[id,nombre,valor])
        cur.close()
        con.close()
    @classmethod
    def deleteProduct(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("delete_Product",[id])
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
    @classmethod
    def updateStock(self, id, cantidad):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("update_stock",[id, cantidad])
        cur.close()
        con.close()
    @classmethod
    def createBoleta(self, id_user, pay_type, payment, entrega, fecha, id_prod, cantidad, total):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("create_boleta",[id_user, pay_type, payment, entrega, fecha])
        cur.callproc("create_detalle_boleta",[id_prod, cantidad, total])
        cur.close()
        con.close()
    @classmethod
    def getUser(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select nombre, apellido, direccion, usuario from usuarios join cliente on usuarios.user_id = cliente.usuario_id where usuarios.user_id = '+str(id))
        res = cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1],column[2]:res[2], column[3]:res[3]}
        cur.close()
        con.close()
        return obj
    @classmethod
    def getDetalle(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select nombre, valor, cantidad, total, id_boleta from detalle_boleta join products on detalle_boleta.id_producto = products.id_prod where id_boleta = (select max(id_boleta) from detalle_boleta where id_producto ='+str(id)+')')
        res = cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1],column[2]:res[2], column[3]:res[3], column[4]:res[4]}
        cur.close()
        con.close()
        return obj
    @classmethod
    def getLastBoleta(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select * from boleta where id_boleta = (select max(id_boleta) from boleta where id_usuario ='+str(id)+')')
        res = cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1],column[2]:res[2], column[3]:res[3], column[4]:res[4], column[5]:res[5]}
        cur.close()
        con.close()
        return obj

            
        


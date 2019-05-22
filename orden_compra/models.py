from django.db import models
import cx_Oracle


# Create your models here.

class Orders(models.Model):
    @classmethod
    def getOrders(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select orden_de_compra.id_orden as id_orden, proveedor.razon_social as razon_social, products_proveedor.nombre as producto, usuarios.nombre as solicitante, orden_de_compra.valor as valor, orden_estado.descripcion as estado from orden_de_compra join proveedor on orden_de_compra.id_proveedor = proveedor.proveedor_id join products_proveedor on orden_de_compra.id_producto = products_proveedor.id_prod join usuarios on orden_de_compra.id_usuario = usuarios.user_id join orden_estado on orden_de_compra.estado = orden_estado.id')
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({column[0] :r[0], column[1]:r[1],column[2]:r[2], column[3]:r[3],column[4]:r[4],column[5]:r[5]})
        cur.close()
        con.close()
        return array
    @classmethod
    def getOrder(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select orden_de_compra.id_orden as id_orden, orden_de_compra.stock as stock, orden_de_compra.stock_crit as stock_crit, proveedor.razon_social as razon_social, products_proveedor.nombre as producto, usuarios.nombre as solicitante, products_proveedor.valor as producto_valor, orden_de_compra.valor as valor, orden_estado.descripcion as estado from orden_de_compra join proveedor on orden_de_compra.id_proveedor = proveedor.proveedor_id join products_proveedor on orden_de_compra.id_producto = products_proveedor.id_prod join usuarios on orden_de_compra.id_usuario = usuarios.user_id join orden_estado on orden_de_compra.estado = orden_estado.id where orden_de_compra.id_orden ='+id)
        res = cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1],column[2]:res[2], column[3]:res[3],column[4]:res[4],column[5]:res[5],column[6]:res[6],column[7]:res[7],column[8]:res[8]}
        cur.close()
        con.close()
        return obj
    @classmethod    
    def getProveedores(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select proveedor_id, razon_social, identificador from proveedor')
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({column[0] :r[0],column[1] :r[1], column[2] :r[2]})
        cur.close()
        con.close()
        print(array)
        return array
    @classmethod
    def getProductos(self, id):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select producto_id, nombre, valor, id_prod, codigo_tipo, razon_social from products_proveedor join proveedor on products_proveedor.id_prov = proveedor.proveedor_id where proveedor.proveedor_id = '+id)
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({column[0] :r[0], column[1]:r[1],column[2]:r[2], column[3]:r[3],column[4]:r[4],column[5]:r[5]})
        cur.close()
        con.close()
        return array
    @classmethod
    def createOrder(self, id_prov, id_prod, id_user, valor, estado, stock, stock_crit):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("create_order",[id_prov, id_prod, id_user, valor, estado, stock, stock_crit])
        cur.close()
        con.close()
    @classmethod
    def updateOrder(self, id, estado):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.callproc("update_order_status",[id,estado])
        cur.close()
        con.close()
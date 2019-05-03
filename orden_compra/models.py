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

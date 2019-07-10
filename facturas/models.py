from django.db import models
import cx_Oracle

# Create your models here.

class facturas(models.Model):
    @classmethod
    def getFacturas(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute("select factura.id_factura, usuarios.nombre ||' '|| usuarios.apellido as nombre, factura.tipo_pago, factura.medio_pago, factura.entrega, factura.fecha, detalle_factura.total from factura join usuarios on factura.id_usuario = usuarios.user_id join detalle_factura on factura.id_factura = detalle_factura.id_factura order by factura.id_factura desc")
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({column[0] :r[0], column[1]:r[1],column[2]:r[2],column[3]:r[3],column[4]:r[4],column[5]:r[5],column[6]:r[6]})
        cur.close()
        con.close()
        return array
    @classmethod
    def getfacturaDetail(self, id_factura):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute("select b.id_factura, u.nombre ||' '|| u.apellido as nombre, b.tipo_pago, b.medio_pago, b.entrega, upper(p.nombre) as producto, db.cantidad, b.fecha, db.total from factura b join detalle_factura db on b.id_factura = db.id_factura join usuarios u on b.id_usuario = u.user_id join products p on db.id_producto = p.id_prod where b.id_factura = "+id_factura)
        res = cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1],column[2]:res[2], column[3]:res[3], column[4]:res[4],column[5] :res[5], column[6]:res[6],column[7]:res[7],column[8]:res[8]}
        cur.close()
        con.close()
        return obj

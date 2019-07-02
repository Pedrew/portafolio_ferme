from django.db import models
import cx_Oracle

# Create your models here.

class Boletas(models.Model):
    @classmethod
    def getBoletas(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute("select boleta.id_boleta, usuarios.nombre ||' '|| usuarios.apellido as nombre, boleta.tipo_pago, boleta.medio_pago, boleta.entrega, detalle_boleta.total from boleta join usuarios on boleta.id_usuario = usuarios.user_id join detalle_boleta on boleta.id_boleta = detalle_boleta.id_boleta")
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({column[0] :r[0], column[1]:r[1],column[2]:r[2],column[3]:r[3],column[4]:r[4],column[5]:r[5]})
        cur.close()
        con.close()
        return array
    @classmethod
    def getBoletaDetail(self, id_boleta):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute("select boleta.id_boleta, nombre ||' '|| apellido as nombre, tipo_pago, medio_pago, entrega, id_producto, cantidad, total from boleta join detalle_boleta on boleta.id_boleta = detalle_boleta.id_boleta join usuarios on boleta.id_usuario = usuarios.user_id where boleta.id_boleta = "+id_boleta)
        res = cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1],column[2]:res[2], column[3]:res[3], column[4]:res[4],column[5] :res[5], column[6]:res[6],column[7]:res[7]}
        cur.close()
        con.close()
        return obj

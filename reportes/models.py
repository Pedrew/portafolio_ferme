from django.db import models
import cx_Oracle

# Create your models here.

class Reportes(models.Model):
    @classmethod
    def boletasAnno(self, ano):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select b.id_boleta, u.nombre, u.apellido, b.tipo_pago, b.medio_pago, b.entrega, b.fecha, p.nombre as producto, db.cantidad, db.total from boleta b join detalle_boleta db on b.id_boleta = db.id_boleta join usuarios u on b.id_usuario = u.user_id join products p on db.id_producto = p.id_prod where substr(fecha,1, 4) = '+ ano)
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
                column[6] :r[6],
                column[7] :r[7],
                column[8] :r[8],
                column[9] :r[9],
            })
        cur.close()
        con.close()
        return array

    @classmethod
    def boletasAnnoTotal(self, ano):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select sum(db.total) as total from boleta b join detalle_boleta db on b.id_boleta = db.id_boleta join usuarios u on b.id_usuario = u.user_id join products p on db.id_producto = p.id_prod where substr(fecha,1, 4) = '+ ano)
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        obj = {column[0]:res[0]}
        cur.close()
        con.close()
        return obj

    @classmethod
    def boletasMes(self, mes, ano):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select b.id_boleta, u.nombre, u.apellido, b.tipo_pago, b.medio_pago, b.entrega, b.fecha, p.nombre as producto, db.cantidad, db.total from boleta b join detalle_boleta db on b.id_boleta = db.id_boleta join usuarios u on b.id_usuario = u.user_id join products p on db.id_producto = p.id_prod where substr(fecha,1, 4) = '+ano+' and substr(fecha,6, 2) = '+mes)
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
                column[6] :r[6],
                column[7] :r[7],
                column[8] :r[8],
                column[9] :r[9],
            })
        cur.close()
        con.close()
        return array

    @classmethod
    def boletasMesTotal(self, mes, ano):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select sum(db.total) as total from boleta b join detalle_boleta db on b.id_boleta = db.id_boleta join usuarios u on b.id_usuario = u.user_id join products p on db.id_producto = p.id_prod where substr(fecha,1, 4) = '+ano+' and substr(fecha,6, 2) = '+mes)
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        obj = {column[0]:res[0]}
        cur.close()
        con.close()
        return obj

    @classmethod
    def boletasDia(self, dia, mes, ano):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select b.id_boleta, u.nombre, u.apellido, b.tipo_pago, b.medio_pago, b.entrega, b.fecha, p.nombre as producto, db.cantidad, db.total as total from boleta b join detalle_boleta db on b.id_boleta = db.id_boleta join usuarios u on b.id_usuario = u.user_id join products p on db.id_producto = p.id_prod where substr(fecha,1, 4) = '+ano+' and substr(fecha,6, 2) = '+mes+ ' and substr(fecha, 9,2) = '+dia)    
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
                column[6] :r[6],
                column[7] :r[7],
                column[8] :r[8],
                column[9] :r[9],
            })
        cur.close()
        con.close()
        return array

    @classmethod
    def boletasDiaTotal(self, dia, mes, ano):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select sum(db.total) as total from boleta b join detalle_boleta db on b.id_boleta = db.id_boleta join usuarios u on b.id_usuario = u.user_id join products p on db.id_producto = p.id_prod where substr(fecha,1, 4) = '+ano+' and substr(fecha,6, 2) = '+mes+ ' and substr(fecha, 9,2) = '+dia)
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        obj = {column[0]:res[0]}
        cur.close()
        con.close()
        return obj

    @classmethod
    def comprasUsuario(self):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute('select count(b.id_usuario) as cantidad, u.nombre, u.apellido from boleta b join usuarios u on b.id_usuario = u.user_id group by b.id_usuario, u.nombre, u.apellido')            
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        array = []
        for r in res:
            array.append({
                column[0] :r[0],
                column[1] :r[1],
                column[2] :r[2],
            })
        cur.close()
        con.close()
        print(array)
        return array
    @classmethod
    def comprasMetodo(self, tipoPago):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute("select b.id_boleta, u.nombre, u.apellido, b.tipo_pago, b.medio_pago, b.entrega, b.fecha, p.nombre as producto, db.cantidad, db.total from boleta b join detalle_boleta db on b.id_boleta = db.id_boleta join usuarios u on b.id_usuario = u.user_id join products p on db.id_producto = p.id_prod where b.medio_pago = '"+tipoPago+"'")
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
                column[6] :r[6],
                column[7] :r[7],
                column[8] :r[8],
                column[9] :r[9],
            })
        cur.close()
        con.close()
        print(array)
        return array

    def comprasMetodoTotal(tipoPago):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute("select sum(db.total) as total from boleta b join detalle_boleta db on b.id_boleta = db.id_boleta join usuarios u on b.id_usuario = u.user_id join products p on db.id_producto = p.id_prod where b.medio_pago = '"+tipoPago+"'")
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        obj = {column[0]:res[0]}
        cur.close()
        con.close()
        return obj

    @classmethod
    def comprasEntrega(self, lugar):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute("select b.id_boleta, u.nombre, u.apellido, b.tipo_pago, b.medio_pago, b.entrega, b.fecha, p.nombre as producto, db.cantidad, db.total from boleta b join detalle_boleta db on b.id_boleta = db.id_boleta join usuarios u on b.id_usuario = u.user_id join products p on db.id_producto = p.id_prod where b.entrega = '"+lugar+"'")
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
                column[6] :r[6],
                column[7] :r[7],
                column[8] :r[8],
                column[9] :r[9],
            })
        cur.close()
        con.close()
        print(array)
        return array

    @classmethod
    def comprasEntregaTotal(self, lugar):
        con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
        cur = con.cursor()
        cur.execute("select sum(db.total) as total from boleta b join detalle_boleta db on b.id_boleta = db.id_boleta join usuarios u on b.id_usuario = u.user_id join products p on db.id_producto = p.id_prod where b.entrega = '"+lugar+"'")
        res = cur.fetchall()
        column = [row[0] for row in cur.description]
        obj = {column[0]:res[0]}
        cur.close()
        con.close()
        return obj
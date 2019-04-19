import cx_Oracle

#Llamada a procedimiento almacenado de la base de datos

#con: Conexión con la base de datos (no modificar esta linea).
#con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
#print (con.version)
#cur = con.cursor()
#utilizamos la funcion callproc para llamar al procedimiento almacenado
#parametros: ("Nombre de procedimiento almacenado", [parametro1, parametro2, parametroN])
#cur.callproc("create_user",['inserte','parametros'])
#commit para actualizar cambios en la base de datos
#cur.execute("commit")
#cerramos cursor.
#cur.close()
#cerramos conexión.
#con.close()

#Ejecutar sentencia select en base de datos

#conexión:
con = cx_Oracle.connect('admin/admin123@dbdrew.cteemzssmjhk.sa-east-1.rds.amazonaws.com/DBDREW')
cur = con.cursor()
#utilizamos la funcion execute, para ejecutar cualquier sentencia en la base de datos,
#en este caso select:
cur.execute('select * from products where product_id = 1')
#imprimimos los resultados obtenidos de nuestra sentencia select.
res = cur.fetchall()
print(res)
#for result in cur:
#    print (result)
#cerramos cursor.
cur.close()
#cerramos conexión.
con.close()


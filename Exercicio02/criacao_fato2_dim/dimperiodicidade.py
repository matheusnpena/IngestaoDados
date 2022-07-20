import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MinhaSenha01",
  database="engenhariadados"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE dimperiodicidade AS (SELECT CONCAT(CNPJ, CodigoServico), Periodicidade FROM apidadoscoletados GROUP BY CONCAT(CNPJ, CodigoServico));")

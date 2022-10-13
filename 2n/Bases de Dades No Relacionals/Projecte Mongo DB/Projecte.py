from pymongo import MongoClient
import json
import pandas as pd
from options import Options




################################## PARAMETRES DE CONNEXIÓ ###################################
mongoUser = ''
mongoPassword = ''
mongoDB = ''

"""
1.  Actualitzeu els paràmetres del script NoSQLfromPython.py per poder establir la connexió amb el MongoDB del vostre PC.
"""
# En execució remota
Host = 'dcccluster.uab.es'
Port = 52551


###################################### CONNEXIÓ ##############################################

DSN = "mongodb://{}:{}".format(Host,Port)

conn = MongoClient(DSN)


############################# TRANSFERÈNCIA DE DADES AMB MONGO ##############################

#Selecciona la base de dades a utilitzar --> test
bd = conn['dadesGICESXIX']  #crear una base de dades


"""
2.	Creeu una col·lecció Prova dins la base de dades test e inseriu 100 documents amb un camp a (a=1 ... a=100).
"""
# Creació d'una col·lecció

"""
3.  Consulteu la col·lecció Prova i visualitzeu tots els resultats per la consola de python.
"""
# Consulta d'una col·leccio i mostrar els resultats


# Conta el número de resultats
"""
4.  Conteu el número de resultats retornats amb la comanda adequada.
"""



"""
Carregar les dades des d'un fitxer JSON
"""
#Obrir Fitxer EXCEL

coll_autors = bd.create_collection('autors')
autors = pd.read_excel('dadesGICESXIX.xlsx', sheet_name='autores')
json_autors = autors.to_json(orient='records')


"""
coll_contes = bd.create_collection('contes')
contes = pd.read_excel('dadesGICESXIX.xlsx', sheet_name='Cuentos')
for titol in contes['titulo']:
    for autor,cuento in zip(autors['Autors'],autors['cuento']):
        if titol == cuento:
            contes['autor'] = autor
print(contes['autor'])
for file in contes:
    coll_contes.insert_one(file)
#print('patatas')
#print(contes['titulo'])
"""





# Parse options
opts = Options()
args = opts.parse()
if args.fileName is not None:
    with open(args.fileName) as f:
        dades = json.load(f)

    #Mostrem els continguts de Dades
    print(dades)


# Tanquem les connexions i el tunel
conn.close()

import sys
from datetime import datetime
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def main():
    "Connect to MongoDB"
    try:
        c = MongoClient(
            host="localhost",
            port=27017
        )
        print("Connected successfully")
    except ConnectionFailure:
        sys.stderr.write("Could not connet to MongoDB")
        sys.exit(1)

    db = c['mydb'] #Crea la base de datos / En caso de estar creada la almacena en la variable "db"

    #cargarUsuario(db,'juancito','Juan','Alvarez',datetime(1995,11,7), 'juancito@gmail.com')

    q = buscarUsuarioByName(db, "Patricio") #Buscar en la base de datos un documento con determinado nombre
    print(q)

    q2 = buscarTodosByName(db, 'Juan') #Buscar en la base de datos todos los usuarios con determinado nombre
    for us in q2:
        print(us)

    #Para conocer la cantidad de documentos en una coleccion 
    usersCount = db.users.find().count()
    print('La Cantidad de Usuarios es de: ', usersCount)

    imprimirPorFDN(db) #Imprimir de forma ordenada



def imprimirPorFDN(db):
    users = db.users.find().sort('fechadenacimiento')
    for u in users:
        print(u)


def cargarUsuario(db, us, name, surname, dateofbith, email):
    user_doc = {
        'username': us,
        'nombre': name,
        'apellido': surname,
        'fechadenacimiento': dateofbith,
        'email': email,
    }
    db.users.insert(user_doc)
    print ('Carga exitosa en el documento: ', user_doc)

def buscarUsuarioByName(db, name):
    user = db.users.find_one({"nombre": name})
    return user

def buscarTodosByName(db, name):
    users = db.users.find({'nombre': name})
    return users


def borrarUsuario():
    pass

if __name__ == "__main__":
    main()

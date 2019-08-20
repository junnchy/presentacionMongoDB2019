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

    #Carga de Usuario ===============================================================================================
    #cargarUsuario(db,'pepo','Ramon','Alvarez',datetime(1993,11,7), 'hj@gmail.com')

    #Busquedas ======================================================================================================

    #Buscar en la base de datos un documento con determinado nombre
    #q = buscarUsuarioByName(db, "Patricio")
    #print(q)

    #Buscar en la base de datos todos los usuarios con determinado nombre
    #q2 = buscarTodosByName(db, 'Juan')
    #for us in q2:
    #    print(us)

    #Para conocer la cantidad de documentos en una coleccion
    #usersCount = db.users.find().count()
    #print('La Cantidad de Usuarios es de: ', usersCount)

    #Imprimir de forma ordenada
    #imprimirPorFDN(db)

    #Actualizar un dato del usuario===================================================================================
    #print(actualizarUsuario(db, buscarUsuarioByName(db, 'Ramon'), 'nuevo@gmail.com'))

    #Borrar un usuario================================================================================================
    #borrarUsuario(db, buscarUsuarioByName(db, 'Ramon'))



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

def actualizarUsuario(db, user, nuevoMail):

    db.users.update_one(user, {"$set": {"email":nuevoMail}})
    return user


def borrarUsuario(db, usuario):

    db.users.delete_one(usuario)
    print('El usuario se ha eliminado')



if __name__ == "__main__":
    main()

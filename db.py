import pdb
import random
import psycopg2

#Total de tous les objets
def countElement():
    conn = psycopg2.connect("dbname=projet-sncf user=postgres host=localhost password=1234")
    query = conn.cursor()
    query.execute("SELECT COUNT(*) as total FROM sncf;")
    result=query.fetchone()
    return result[0]

def countObjectsNotReturned():
    conn = psycopg2.connect("dbname=projet-sncf user=postgres host=localhost password=1234")
    query = conn.cursor()
    query.execute("SELECT COUNT(*) as total FROM sncf WHERE date_resti='1970-01-01';")
    result=query.fetchone()
    return result[0]

def countObjectsReturned():
    conn = psycopg2.connect("dbname=projet-sncf user=postgres host=localhost password=1234")
    query = conn.cursor()
    query.execute("SELECT COUNT(*) as total FROM sncf WHERE date_resti!='1970-01-01';")
    result=query.fetchone()
    return result[0]

def statObjectFoundByYear():
    #print("Objet retrouvé par année")
    conn=psycopg2.connect("dbname=projet-sncf user=postgres host=localhost password=1234")
    query=conn.cursor()
    query.execute("SELECT EXTRACT(YEAR FROM date_resti::date) as annee,count(*) as total FROM sncf GROUP BY EXTRACT(YEAR FROM date_resti::date) ORDER BY EXTRACT(YEAR FROM date_resti::date) DESC LIMIT 5;")
    result=query.fetchall()
    return result

#Statistiques annuelle des objets pour l'année en cours:2023
def statAnnualObjectsFoundOrderByMonth():
    res=[]
    conn=psycopg2.connect("dbname=projet-sncf user=postgres host=localhost password=1234")
    query=conn.cursor()
    query.execute("SELECT EXTRACT(MONTH FROM date_resti::date) as mois, count(*) as total FROM sncf WHERE EXTRACT(YEAR FROM date_resti::date)=2023 GROUP BY EXTRACT(MONTH FROM date_resti::date);")
    result=query.fetchall()
    for index in range(0,len(result)):
        res.append(result[index][1])
    print(res)
    return res
 
#Statistiques Objets non restitués
def statAnnualObjectsNotRestoreOrderByMonth():
    print("Oui")
    res=[]
    conn=psycopg2.connect("dbname=projet-sncf user=postgres host=localhost password=1234")
    query=conn.cursor()
    query.execute("SELECT EXTRACT(MONTH FROM date::date) as mois, count(date_resti) as total FROM sncf WHERE date_resti='1970-01-01' GROUP BY EXTRACT(MONTH FROM date::date)")
    result=query.fetchall()
    for index in range(0,len(result)):
        res.append(result[index][1])
    return res

def selectObjectsByRegion():
    print("Ok")

#Total des objets restitués
def countObjectsReturned_():
    print("Objets returned")


statAnnualObjectsNotRestoreOrderByMonth()
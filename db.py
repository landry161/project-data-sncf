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
    query.execute("SELECT EXTRACT(YEAR FROM date_resti::date) as annee,count(*) as total FROM sncf GROUP BY EXTRACT(YEAR FROM date_resti::date) ORDER BY EXTRACT(YEAR FROM date_resti::date) DESC LIMIT 6;")
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
    res=[]
    conn=psycopg2.connect("dbname=projet-sncf user=postgres host=localhost password=1234")
    query=conn.cursor()
    query.execute("SELECT EXTRACT(MONTH FROM date::date) as mois, count(date_resti) as total FROM sncf WHERE date_resti='1970-01-01' AND EXTRACT(YEAR FROM date::date)=2023 GROUP BY EXTRACT(MONTH FROM date::date)")
    result=query.fetchall()
    for index in range(0,len(result)):
        res.append(result[index][1])
    return res

def selectDistinctRegions():
    regionsArray=[]
    conn=psycopg2.connect("dbname=projet-sncf user=postgres host=localhost password=1234")
    query=conn.cursor()
    query.execute("SELECT DISTINCT(region_sncf) as total FROM public.sncf;")
    regions=query.fetchall()
    for index in range(0,len(regions)):
        regionsArray.append(regions[index][0])
    return regionsArray

def selectDistinctYear():
    years=[]
    conn=psycopg2.connect("dbname=projet-sncf user=postgres host=localhost password=1234")
    query=conn.cursor()
    query.execute("SELECT EXTRACT(YEAR FROM date::date) FROM public.sncf group BY EXTRACT(YEAR FROM date::date) ORDER BY EXTRACT(YEAR FROM date::date) DESC;")
    results=query.fetchall()
    for index in range(0,len(results)):
        years.append(results[index][0])
    
    return years

def selectStatObjectsFoundByType():
    stats=[]
    colors=['#2552C4','#011616','#E5F5F5','#140A0D','#2E0103','#873939','#0F485A','#4e73df','#1cc88a','#36b9cc','#2e59d9', '#17a673', '#2c9faf','#dddfeb','#858796','#6e707e'],
    conn=psycopg2.connect("dbname=projet-sncf user=postgres host=localhost password=1234")
    query=conn.cursor()
    query.execute("SELECT COUNT(type_objets) as total, type_objets FROM sncf GROUP BY type_objets ORDER BY COUNT(type_objets) DESC;")
    result=query.fetchall()
    
    for index in range(0,len(result)):
        value={
            'type_objets':result[index][1],
            'value':result[index][0],
            'color':colors[0][index]
        }
        stats.append(value)
    return stats

def selectStatObjectsFoundedByYear():
    pieCharts=[]
    conn=psycopg2.connect("dbname=projet-sncf user=postgres host=localhost password=1234")
    query=conn.cursor()
    query.execute("SELECT EXTRACT(YEAR FROM date::date) as annee, count(*) as total FROM sncf GROUP BY EXTRACT(YEAR FROM date::date);")
    res=query.fetchall()

    for i in range(0,len(res)):
        pieCharts.append({'name':res[i][0],'y':res[i][1]})
    print(pieCharts)
    return pieCharts

#Total des objets restitués
def selectTopTenObjectsFoundForCurrentYear():
    currentResults=[]
    conn=psycopg2.connect("dbname=projet-sncf user=postgres host=localhost password=1234")
    query=conn.cursor()
    query.execute("SELECT region_sncf,COUNT(*) as total FROM sncf WHERE EXTRACT(YEAR from date::date)=2023 GROUP BY region_sncf ORDER BY total DESC LIMIT 10")
    res=query.fetchall()

    for i in range(0,len(res)):
        currentResults.append({'region':res[i][0],'total':res[i][1]})
    
    return currentResults

def selectObjectFoundByDepartement():
    results=[]
    #x: Objets restitues
    #y: Objets non restitués
    conn=psycopg2.connect("dbname=projet-sncf user=postgres host=localhost password=1234")
    query=conn.cursor()
    query.execute("SELECT departement,count(case when date_resti!='1970-01-01' then date_resti end) as resti, count(case when date_resti='1970-01-01' then date_resti end) as non_restitue FROM public.sncf group by departement;")
    res=query.fetchall()

    for i in range(0,len(res)):
        results.append({
            'x':res[i][1],
            'y':res[i][2],
            'name':res[i][0][0:3],
            'country':res[i][0]
        })
    #print(results)
    return results

selectObjectFoundByDepartement()
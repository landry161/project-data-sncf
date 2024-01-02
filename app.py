import pdb
from flask import Flask
from flask import Flask, render_template,request,redirect
from datetime import datetime
import pandas as pd
import json
from db import *
from colors import *

app = Flask(__name__)

def colorsIcons(index):
    arrayColors=["bg-success","bg-warning","bg-danger","bg-info","bg-ligth","bg-dark"]
    return arrayColors[index]

@app.route("/")
def home():
    arrayFinal=[]
    totalSix=0
    myTotal=countElement()
    typesObjs=[]
    totals=[]
    myColors=[]
    backColors=[]
    topTensCategories=[]
    topTensSeries=[]

    arrayObjs=selectStatObjectsFoundByType()
    topTensRegions=selectTopTenObjectsFoundForCurrentYear()
    
    totalNotReturned=countObjectsNotReturned()
    totalReturned=countObjectsReturned()
    statSixByYear=statObjectFoundByYear()
    for index in range(0,len(statSixByYear)):
        keysValue={
            'year':statSixByYear[index][0],
            'value':statSixByYear[index][1],
            'color':colorsIcons(index)
        }
        totalSix+=statSixByYear[index][1]
        arrayFinal.append(keysValue)

    for i in range(0,len(arrayObjs)):
        typesObjs.append(arrayObjs[i]["type_objets"])
        totals.append(arrayObjs[i]["value"])
        myColors.append(arrayObjs[i]['color'])
        backColors.append(getArrayColors(len(arrayObjs)-i))
    
    for j in range(0,len(topTensRegions)):
        topTensCategories.append(topTensRegions[j]["region"])
        topTensSeries.append(topTensRegions[j]["total"])

    return render_template("index.html",bubbleChart=selectObjectFoundByDepartement(),tSeries=topTensSeries,tCategories=topTensCategories,piecharts=selectStatObjectsFoundedByYear(),back=backColors,col=myColors,values=totals,types=typesObjs,years=selectDistinctYear(),regions=selectDistinctRegions(),labelAreaNotRestored=statAnnualObjectsNotRestoreOrderByMonth(),labelArea=statAnnualObjectsFoundOrderByMonth(),totalSix=totalSix,topSix=arrayFinal,total=myTotal,notReturned=totalNotReturned,returned=totalReturned)
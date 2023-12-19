import pdb
from flask import Flask
from flask import Flask, render_template,request,redirect
from datetime import datetime
import pandas as pd
from db import *

app = Flask(__name__)

def colorsIcons(index):
    arrayColors=["bg-success","bg-warning","bg-danger","bg-info","bg-ligth","bg-dark"]
    return arrayColors[index]

@app.route("/")
def home():
    arrayFinal=[]
    totalSix=0
    myTotal=countElement()
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
    print("Voici")
    print(totalSix)
    #pdb.set_trace()
    return render_template("index.html",totalSix=totalSix,topSix=arrayFinal,total=myTotal,notReturned=totalNotReturned,returned=totalReturned)
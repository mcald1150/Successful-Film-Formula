# import necessary libraries
from sqlalchemy import func
import pandas as pd
import json
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score




from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

my_data = []

@app.route("/DA")
def da():
    return render_template("DA.html")

@app.route("/moviesData")
def moviesData():
    df = pd.read_csv('DataSet/movies_metadata.csv')
    movies_data = df.to_dict(orient='records')
    return jsonify(movies_data)
    

# create route that renders index.html template
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nickname = request.form["nickname"]
        age = request.form["age"]

        form_data = {
                "nickname": nickname,
                "age": int(age)
                }
        my_data.append(form_data)
        # return render_template("index.html")
    return render_template("index.html")

@app.route("/send", methods=["GET", "POST"])
def index2():
    if request.method == "POST":
        nickname = request.form["nickname"]
        age = request.form["age"]

        form_data = {
                "nickname": nickname,
                "age": int(age)
                }
        my_data.append(form_data)


        # return render_template("index.html")
    return jsonify(my_data)



@app.route("/api/mydata")
def data():
    print(my_data)
    return jsonify(my_data)

# def home():
    
#     return render_template("index.html")

# @app.route("/data")
# def data():
#     sel = [func.strftime("%Y", Shooting.DATE), func.count(Shooting.DATE)]
#     print(sel)
#     results = db.session.query(*sel).\
#         group_by(func.strftime("%Y", Shooting.DATE)).all()
#     print(results)
#     df = pd.DataFrame(results, columns=['year', 'sightings'])
#     return jsonify(df.to_dict(orient="records"))

@app.route("/data")
def shootingsdata():
    df = pd.read_csv('tmdb_5000_moviestest2.csv',encoding = 'utf_8')
    chart_data = df.to_dict(orient='records')
    return jsonify(chart_data)

my_data = []

@app.route("/mldata")
def mldata():
    return jsonify(my_data)
    

@app.route("/ml", methods=["GET", "POST"])
def ml():
    results={}

    df = pd.read_csv('project_3.csv',encoding = 'utf_8')
    dfmovie = df[['budget','popularity','vote_count','runtime','vote_average','revenue','year','month','original_title',
              'Action','History','Fantasy','Romance','Family','Documentary','Comedy',
              'Western','TV Movie','Adventure', 'War','Music','Animation','Drama','Horror',
              'Foreign','Science Fiction','Mystery','Thriller','Crime']]
    X = dfmovie[['year','month','budget','popularity','vote_count','vote_average','runtime',
             'Action','History','Fantasy','Romance','Family','Documentary',
             'Comedy','Western','TV Movie','Adventure', 'War','Music',
             'Animation','Drama','Horror','Foreign','Science Fiction','Mystery','Thriller','Crime']]
    y = dfmovie[['revenue']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    X_scaler = StandardScaler().fit(X_train)
    y_scaler = StandardScaler().fit(y_train)
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    y_train_scaled = y_scaler.transform(y_train)
    y_test_scaled = y_scaler.transform(y_test)
    model = LinearRegression()
    model.fit(X_train_scaled, y_train_scaled)
    predicted = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test_scaled, predicted)
    r2 = r2_score(y_test_scaled, predicted)
    budgetvalue=0
    if request.method == "POST":
        budgetvalue = request.form["budgetvalue"]
        popularityvalue = request.form["popularityvalue"]
        votecountvalue = request.form["votecountvalue"]
        voteaveragevalue = request.form["voteaveragevalue"]
        yearvalue = request.form["yearvalue"]
        monthvalue = request.form["monthvalue"]
        runtimevalue = request.form["runtimevalue"]
        
        try:
            my_data.pop()
            # you need pop() and not mydata = [] because you need to access the original list, not create a new empty list
        except:
            pass

        if request.form.get("ActionCheckBox"):
             ActionCheckBox = True
        else:
            ActionCheckBox = False

        if request.form.get("HistoryCheckBox"):
             HistoryCheckBox = True
        else:
            HistoryCheckBox = False

        if request.form.get("FantasyCheckBox"):
             FantasyCheckBox = True
        else:
            FantasyCheckBox = False

        if request.form.get("RomanceCheckBox"):
             RomanceCheckBox = True
        else:
            RomanceCheckBox = False

        if request.form.get("FamilyCheckBox"):
             FamilyCheckBox = True
        else:
            FamilyCheckBox = False

        if request.form.get("DocumentaryCheckBox"):
             DocumentaryCheckBox = True
        else:
            DocumentaryCheckBox = False

        if request.form.get("ComedyCheckBox"):
             ComedyCheckBox = True
        else:
            ComedyCheckBox = False

        if request.form.get("WesternCheckBox"):
             WesternCheckBox = True
        else:
            WesternCheckBox = False

        if request.form.get("TVMovieCheckBox"):
             TVMovieCheckBox = True
        else:
            TVMovieCheckBox = False

        if request.form.get("AdventureCheckBox"):
             AdventureCheckBox = True
        else:
            AdventureCheckBox = False

        if request.form.get("WarCheckBox"):
             WarCheckBox = True
        else:
            WarCheckBox = False

        if request.form.get("MusicCheckBox"):
             MusicCheckBox = True
        else:
            MusicCheckBox = False

        if request.form.get("AnimationCheckBox"):
             AnimationCheckBox = True
        else:
            AnimationCheckBox = False

        if request.form.get("DramaCheckBox"):
             DramaCheckBox = True
        else:
            DramaCheckBox = False

        if request.form.get("HorrorCheckBox"):
             HorrorCheckBox = True
        else:
            HorrorCheckBox = False

        if request.form.get("DramaCheckBox"):
             DramaCheckBox = True
        else:
            DramaCheckBox = False

        if request.form.get("ForeignCheckBox"):
             ForeignCheckBox = True
        else:
            ForeignCheckBox = False

        if request.form.get("DramaCheckBox"):
             DramaCheckBox = True
        else:
            DramaCheckBox = False

        if request.form.get("ScienceFictionCheckBox"):
             ScienceFictionCheckBox = True
        else:
            ScienceFictionCheckBox = False

        if request.form.get("MysteryCheckBox"):
             MysteryCheckBox = True
        else:
            MysteryCheckBox = False

        if request.form.get("ThrillerCheckBox"):
             ThrillerCheckBox = True
        else:
            ThrillerCheckBox = False

        if request.form.get("CrimeCheckBox"):
             CrimeCheckBox = True
        else:
            CrimeCheckBox = False
        
        
        #         budgetvalue = request.form["budgetvalue"]
        # popularityvalue = request.form["popularityvalue"]
        # votecountvalue = request.form["votecountvalue"]
        # voteaveragevalue = request.form["voteaveragevalue"]
        # yearvalue = request.form["yearvalue"]
        # monthvalue = request.form["monthvalue"]
        # runtimevalue = request.form["runtimevalue"]


        year = int(yearvalue)
        month = int(monthvalue)
        budget = int(budgetvalue)
        popularity = int(popularityvalue)
        vote_count=int(votecountvalue)
        vote_average = int(voteaveragevalue)
        runtime = int(runtimevalue)
        Action = 1*ActionCheckBox
        History = 1*HistoryCheckBox
        Fantasy = 1*FantasyCheckBox
        Romance  = 1*RomanceCheckBox
        Family  = 1*FamilyCheckBox
        Documentary  = 1*DocumentaryCheckBox
        Comedy  = 1*ComedyCheckBox
        Western  = 1*WesternCheckBox
        TV_Movie  = 1*TVMovieCheckBox
        Adventure  = 1*AdventureCheckBox
        War  = 1*WarCheckBox
        Music  = 1*MusicCheckBox
        Animation  = 1*AnimationCheckBox
        Drama  = 1*DramaCheckBox
        Horror  = 1*HorrorCheckBox
        Foreign  = 1*ForeignCheckBox
        Science_Fiction  = 1*ScienceFictionCheckBox
        Mystery  = 1*MysteryCheckBox
        Thriller  = 1*ThrillerCheckBox
        Crime = 1*CrimeCheckBox

        X_user = [[ year , month , budget , popularity , vote_count , vote_average , runtime ,
              Action , History , Fantasy , Romance , Family , Documentary ,
              Comedy , Western , TV_Movie , Adventure ,  War , Music ,
              Animation , Drama , Horror , Foreign , Science_Fiction , Mystery , Thriller , Crime ]]
        # X_scaler = StandardScaler().fit(X_user)
        # X_user_scaled = X_scaler.transform(X_user)
        # predicted = model.predict(X_user_scaled)
        predicted = model.predict(X_user)
        predicted = np.round(predicted[0][0],2)


        results = {
            'predicted':predicted,
            'mse':mse, 
            'r2':r2, 
            'budgetvalue':budgetvalue, 
            'popularityvalue': popularityvalue,
            'votecountvalue' : votecountvalue,
            'voteaveragevalue' : voteaveragevalue,
            'yearvalue' : yearvalue,
            'monthvalue' : monthvalue,
            'runtimevalue' : runtimevalue,
            'ActionCheckBox':ActionCheckBox,
            'HistoryCheckBox':HistoryCheckBox,
            'FantasyCheckBox':FantasyCheckBox,
            'RomanceCheckBox':RomanceCheckBox,
            'FamilyCheckBox':FamilyCheckBox,
            'DocumentaryCheckBox':DocumentaryCheckBox,
            'ComedyCheckBox':ComedyCheckBox,
            'WesternCheckBox':WesternCheckBox,
            'TVMovieCheckBox':TVMovieCheckBox,
            'AdventureCheckBox':AdventureCheckBox,
            'WarCheckBox':WarCheckBox,
            'MusicCheckBox':MusicCheckBox,
            'AnimationCheckBox':AnimationCheckBox,
            'DramaCheckBox':DramaCheckBox,
            'HorrorCheckBox':HorrorCheckBox,
            'ForeignCheckBox':ForeignCheckBox,
            'ScienceFictionCheckBox':ScienceFictionCheckBox,
            'MysteryCheckBox':MysteryCheckBox,
            'ThrillerCheckBox':ThrillerCheckBox,
            'CrimeCheckBox':CrimeCheckBox
        }


        my_data.append(results)
        return render_template("ml.html", data=results)
    # chart_data = dfmovie.to_dict(orient='records')
    return render_template("ml.html", data=results)
    # return jsonify(chart_data)



if __name__ == "__main__":
    app.run(debug=True)

# Importing necessary libraries

import pandas as pd
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///static/db/warheads.sqlite"

db = SQLAlchemy(app)

class Warhead_launch(db.Model):
    __tablename__ = 'Nuclear_Test_Launches'

    Year = db.Column(db.Text, primary_key = True)
    USA = db.Column(db.Integer)
    USSR_Russia = db.Column(db.Integer)
    United_Kingdom = db.Column(db.Integer)
    France = db.Column(db.Integer)
    China = db.Column(db.Integer)
    India = db.Column(db.Integer)
    Pakistan = db.Column(db.Integer)
    North_Korea = db.Column(db.Integer)
   

    def __repr__(self):
        return '<Warhead_launch %r>' % (self.Year)


@app.before_first_request
def setup():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/doughnut")
def f_doughnut():
    USA_results = db.session.query(func.sum(Warhead_launch.USA)).all()
    USSR_Russia_results = db.session.query(func.sum(Warhead_launch.USSR_Russia)).all() 
    United_Kingdom_results = db.session.query(func.sum(Warhead_launch.United_Kingdom)).all()
    France_results = db.session.query(func.sum(Warhead_launch.France)).all()
    China_results = db.session.query(func.sum(Warhead_launch.China)).all()
    India_results = db.session.query(func.sum(Warhead_launch.India)).all()
    Pakistan_results = db.session.query(func.sum(Warhead_launch.Pakistan)).all()
    North_Korea_results = db.session.query(func.sum(Warhead_launch.North_Korea)).all() 
    trace5 = {}
   
    trace5["value"] = [USA_results[0][0], USSR_Russia_results[0][0], United_Kingdom_results[0][0], France_results[0][0], China_results[0][0], India_results[0][0], Pakistan_results[0][0], North_Korea_results[0][0]]
 
    return jsonify(trace5)


if __name__ == "__main__":
    app.run(debug=True)






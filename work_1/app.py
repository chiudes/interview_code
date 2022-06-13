import os
import sqlalchemy as db
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session, json, jsonify
from datetime import datetime
from flask_moment import Moment
from sqlalchemy import create_engine


load_dotenv()

app = Flask(__name__)
moment = Moment(app)

engine = create_engine('mysql+pymysql://root:Passw0rd!@localhost:3306/lvrland')

@app.route('/', methods=["GET","POST"])
def index():
    connection = engine.connect()

    cursor_dis = connection.execute("select id,district,city from all_lvr_land group by city, district order by city")
    cursor_stl = connection.execute("select style from all_lvr_land group by style")
    result_style = cursor_stl.fetchall()    
    result_district = cursor_dis.fetchall()

    connection.close()
    if request.method == "GET":
        RRR = 1
        return render_template('index.html',
                                district=result_district,
                                style = result_style,
                                RRR = RRR,
                                modinit = 0,
                                tmpAll = 0,
                                tmpInfo_2021 = 0
                                )
    elif request.method == "POST":
        RRR = 2

        select_district = request.form['district']
        select_style = request.form['style']
        select_floor = request.form['floor_num']

        connection = engine.connect()
        cursor = connection.execute(
            f"select district, style, floor from all_lvr_land where (id = '{select_district}') and (style = '{select_style}') and (floor = '{select_floor}');"
            )
        getAll = cursor.fetchall()
        connection.close()              
        
        return jsonify({'result': [dict(row) for row in getAll]})
     


if __name__ == "__main__":
    app.run(debug=True)
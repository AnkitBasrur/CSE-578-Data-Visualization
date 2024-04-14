from flask import Flask, render_template, request, jsonify
import pandas as pd
from sqlalchemy import create_engine
import json

app = Flask(__name__, template_folder="templates")

user = 'root'
pw = 'mysql123'
host = 'localhost'
db = 'data_viz'


def getRecordsFromTable(table):
    engine = create_engine(f'mysql+pymysql://{user}:{pw}@{host}/{db}')
    with engine.connect() as conn, conn.begin():
        data = pd.read_sql_table(table, conn)
    conn.close()
    return data.to_json(orient="records")


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/processDataParticipants', methods=['POST'])
def processDataParticipants():
    return getRecordsFromTable('Participants')

@app.route('/processDataEmployeePopulation', methods=['POST'])
def processDataEmployeePopulation():
    return getRecordsFromTable('employeepopulation')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import requests
from config import conn_str
import pyodbc
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import urllib.parse
from modles import Visitor  

# Define your Azure SQL credentials and server details here.
params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.3.119;DATABASE=threetier;UID=test;PWD=Test#123450;Connection Timeout=60")
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conn_str

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/visitor', methods=['GET', 'POST'])
def visitor():
    if request.method == 'POST':
        visitor_info = {
            'name': request.form['name'],
            'phone': request.form['phone'],
            'email': request.form['email']
        }
        response = requests.post('http://localhost:5000/api/data', json=visitor_info).json()
        print(f"Response from POST request: {response}")
        return render_template('index.html', name=visitor_info['name'])
    return render_template('visitor.html')

@app.route('/all_visitors')
def all_visitors():
    # Get all the visitors
    visitors = Visitor.query.order_by(Visitor.timestamp.desc()).all()

    # Transform results into a list of dictionaries for easier handling in the template
    visitors_list = [{'name': visitor.name, 'visit_date': visitor.timestamp.strftime('%Y-%m-%d %H:%M:%S')} for visitor in visitors]

    return render_template('all_visitors.html', visitors=visitors_list)

if __name__ == '__main__':
     app.run(port=4000)




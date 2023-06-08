from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import urllib.parse

app = Flask(__name__)

# Define your Azure SQL credentials and server details here.
params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.3.119;DATABASE=threetier;UID=test;PWD=Test#123450;Connection Timeout=60")
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)

# The database URI that should be used for the connection.
app.config['SQLALCHEMY_DATABASE_URI'] = conn_str

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    phone = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Visitor {self.name}>'

# Create all the tables in the database which are defined as subclasses of db.Model
if __name__ == '__main__':
    with app.app_context():
        db.create_all()




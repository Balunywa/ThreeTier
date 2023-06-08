from flask import Flask, request, jsonify
from config import conn_str
from modles import Visitor  # Assuming Visitor model is in the modules
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

@app.route('/api/data', methods=['POST'])
def data():
    visitor_info = request.get_json()

    try:
        # Create a new visitor instance
        new_visitor = Visitor(name=visitor_info['name'], phone=visitor_info['phone'], email=visitor_info['email'])
        
        # Add the new visitor to the database session
        db.session.add(new_visitor)
        
        # Commit the transaction
        db.session.commit()

        message = f"Welcome {visitor_info['name']}!"
        return jsonify({'message': message}), 200  # HTTP status code for success

    except Exception as e:
        return jsonify({'message': str(e)}), 500  # HTTP status code for server error

if __name__ == '__main__':
    app.run(port=5000)




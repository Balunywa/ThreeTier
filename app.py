from flask import Flask, render_template, request
import requests
from config import conn_str
import pyodbc


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        visitor_info = {
            'name': request.form['name'],
            'phone': request.form['phone'],
            'email': request.form['email']
        }
        response = requests.post('http://localhost:5000/api/data', json=visitor_info).json()
        print(f"Response from POST request: {response}")  # Added this line to print response
        #return render_template('welcome.html', message=response['message'])
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(port=4000)



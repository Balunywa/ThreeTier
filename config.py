import urllib.parse

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.3.119;DATABASE=threetier;UID=test;PWD=Test#123450;Connection Timeout=60")
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)

#WIN-0PIJMU5U2AB
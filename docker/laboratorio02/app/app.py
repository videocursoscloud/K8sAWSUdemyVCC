import os
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = os.environ['db_host']
app.config['MYSQL_USER'] = os.environ['db_user']
app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_ROOT_PASSWORD']
app.config['MYSQL_DB'] = os.environ['db_name']

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

import peeweedbevolve
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db,Store,Warehouse,Product

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.before_request 
def before_request():
   db.connect()

@app.after_request 
def after_request(response):
   db.close()
   return response

@app.cli.command() 
def migrate(): 
   db.evolve(ignore_tables={'base_model'})

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/store")
def store():   
    return render_template('store.html')

@app.route("/store_form", methods=["POST"])
def store_form(): 
    s = Store(name=request.form['name'])
    if s.save():
        flash("Succesfully saved!")
        return redirect(url_for('store'))
    else:
        flash("not success try again!")
        return render_template('store.html', name=request.form['name'])

@app.route("/warehouse")
def warehouse():
    return render_template('warehouse.html')

if __name__ == '__main__':
    app.run()
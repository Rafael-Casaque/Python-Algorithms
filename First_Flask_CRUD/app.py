from flask import Flask,request, redirect, url_for,render_template

app = Flask(__name__,template_folder='Templates',static_folder='static')
number_id = []
name = []
age = []
tel = []


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create():    
    return render_template('create.html')

@app.route('/create/success',methods=['GET','POST'])
def create_success():
    number_id.append(request.form['id'])
    name.append(request.form['name'])
    age.append(request.form['age'])
    tel.append(request.form['tel'])        
    return redirect(url_for('index'))

@app.route('/update/success',methods=['GET','POST'])
def update_success():
    number_find = number_id.index(request.form['id'])
    name[number_find] = request.form['name']
    age[number_find] = request.form['age']
    tel[number_find] = request.form['tel']
    return redirect(url_for('index'))

@app.route('/delete/success',methods=['GET','POST'])
def delete_success():
    number_find = number_id.index(request.form['id'])
    del number_id[number_find]
    del name[number_find]
    del age[number_find]
    del tel[number_find]
    return redirect(url_for('index'))

@app.route('/read')
def read():
    return render_template('read.html',name = name,number_id = number_id ,age = age,tel = tel)

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')

app.run(debug=True)
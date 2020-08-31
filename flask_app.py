# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template,request,redirect,url_for
from pony.orm import Database, Required, Optional, PrimaryKey, select, db_session
app = Flask(__name__)
db=Database()

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    surname = Required(str)
    score = Required(int)
    age = Optional(int)

db.bind(provider='sqlite', filename='userdata', create_db=True) # username, password, host, database
db.generate_mapping(create_tables=True)




@app.route('/',methods=["POST","GET"])
@db_session
def main():
    if request.method=="POST":
        name = request.form.get('name')
        surname = request.form.get('surname')
        age = request.form.get('age')
        score=0
        if request.form.get('group1')=="b":
            score+=1
        if request.form.get('group2')=="b":
            score+=1
        if request.form.get('group3')=="a":
            score+=1
        if request.form.get('group4')=="b":
            score+=1
        if request.form.get('group5')=="a":
            score+=1
        if request.form.get('group6')=="b":
            score+=1
        if request.form.get('group7')=="a":
            score+=1
        if request.form.get('group8')=="a":
            score+=1
        if request.form.get('group9')=="b":
            score+=1
        if request.form.get('group10')=="a":
            score+=1
        if request.form.get('group11')=="b":
            score+=1
        if request.form.get('group12')=="a":
            score+=1
        if request.form.get('group13')=="b":
            score+=1
        if request.form.get('group14')=="a":
            score+=1
        if request.form.get('group15')=="a":
            score+=1
        if request.form.get('group16')=="b":
            score+=1
        if request.form.get('group17')=="a":
            score+=1
        if request.form.get('group18')=="a":
            score+=1
        if request.form.get('group19')=="a":
            score+=1
        if request.form.get('group20')=="a":
            score+=1
        User(name=name,surname=surname,age=age,score=score)
        users = select(user for user in User)
        return render_template('history.html',USERS=users)
    elif request.method=="GET":
        return render_template('index.html')

@app.route('/history')
@db_session
def history():
    return render_template('history.html',USERS=select(user for user in User))

@app.route("/history/modify/<id>",methods=["GET","POST"])
@db_session
def modify(id):
    if request.method=="POST":
        newname=request.form.get("name")
        newsurname=request.form.get("surname")
        newage=request.form.get("age")
        newscore=request.form.get("score")
        if newname:
            User[id].name=newname
        if newsurname:
            User[id].surname=newsurname
        if newage:
            User[id].age=newage
        if newscore:
            User[id].score=newscore
        return redirect(url_for("history"))
    elif request.method=="GET":
        return render_template("user_info.html",USER=User[id])



@app.route("/history/delete/<id>")
@db_session
def delete(id):
    if User[id]:
        User[id].delete()
    return redirect(url_for("history"))

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
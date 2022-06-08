from flask import Flask, request, render_template, redirect
import requests
from models import library
from forms import libraryForm

app=Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route('/biblioteka',methods=['GET','POST'])
def lib():  
    form=libraryForm()
    if request.method=='POST': 
        library.create(form.data)
        library.save_all()
        return render_template('main.html', form=libraryForm(),books=library.all())
    return render_template('main.html', form=libraryForm(), books=library.all())

@app.route('biblioteka/<int:id>',methods=['GET','POST'])
def lib2(id):
    n=library.get(id)
    return n


if __name__ == "__main__":
    app.run(debug=True)
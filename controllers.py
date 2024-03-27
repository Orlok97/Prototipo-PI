from flask import render_template, request, url_for, redirect , session, jsonify
from models import *

#os metodos index dos controllers renderizam os templates

class LoginController:
    def index(self):
        return render_template('index.html')
    def auth(self):
        if request.method=='POST':
            pass
            

class CadastroController:
    def index(self):
        if request.method=='POST':
            nome=request.form.get('nome')
            email=request.form.get('email')
            telefone=request.form.get('telefone')
            senha=request.form.get('senha')
            if(self.store(nome,email,telefone,senha)):
                session['alert']='cadastro feito com sucesso!'
            else:
                session['alert']='erro ao cadastrar! '
        return render_template('cadastro.html')
    def store(self,nome,email,telefone,senha):
        try:
            Usuario().create(nome,email,telefone,senha)
            print('usuario cadastrado com sucesso!')
            return True
        except Exception as e:
            print('um erro ocorreu: ',e)
            
    def get_all(self):
        return Usuario().get_all()

class HomeController:
    def index(self):
        return render_template('home.html')
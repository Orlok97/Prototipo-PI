from flask import render_template, request, url_for
from flask import redirect , session, flash
from models import *

#os metodos index dos controllers renderizam os templates

class LoginController:
    def index(self):
        if request.method=='POST':
            email=request.form.get('email')
            senha=request.form.get('senha')
            self.auth(email,senha)
        return render_template('index.html')
    def auth(self,email,senha):
        print(Auth().login(email,senha))
        
            

class CadastroController:
    def index(self):
        if request.method=='POST':
            nome=request.form.get('nome')
            email=request.form.get('email')
            telefone=request.form.get('telefone')
            senha=request.form.get('senha')
            if(self.store(nome,email,telefone,senha)):
                flash('usuario cadastrado com sucesso!')
            else:
                flash('erro ao cadastrar!')
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
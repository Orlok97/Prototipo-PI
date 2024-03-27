from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(80),nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    telefone=db.Column(db.Integer)
    senha=db.Column(db.String(120),nullable=False)

    #def __repr__(self):
        #return 'Usuario %r'%self.nome
    @staticmethod
    def create(nome,email,telefone,senha):
        usuario=Usuario(nome=nome,email=email,telefone=telefone,senha=senha)
        db.session.add(usuario)
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(f"erro ao criar : {e}")
            db.session.rollback()
            return False
    @staticmethod
    def auth(email):
        usuario=Usuario.query.filter_by(email=email).first()
        if usuario:
            return usuario

class Solicitar_Coleta(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    titulo=db.Column(db.String(80),nullable=False)
    cidade=db.Column(db.String(120),unique=False,nullable=False)
    bairro=db.Column(db.String(120),nullable=False)
    rua=db.Column(db.String(120),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('usuario.id'),nullable=False)

    def __repr__(self):
        return 'Coleta %r'%self.titulo

class Auth:
    def login(self,e,senha):
        usuario=Usuario.query.filter_by(email=e).first()
        if usuario.senha == senha:
            return True
        

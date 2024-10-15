from database.session import db

class Transaction(db.Model):
	__tablename__ = 'transaction'
	id = db.Column(db.Integer(), primary_key=True)
	conta = db.Column(db.String(10), nullable=False)
	agencia = db.Column(db.String(15), nullable=False)
	texto = db.Column(db.String(), nullable=True)
	valor = db.Column(db.Float(), nullable=False)
	
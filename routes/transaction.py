from flask import request, jsonify

from database.session import db
from model.transaction import Transaction


def register_routes(app):
	@app.route('/transaction', methods=['POST'])
	def create_transaction():
		data = request.get_json()

		new_transaction = Transaction(
			conta=data.get('conta'),
			agencia=data.get('agencia'),
			texto=data.get('texto', None),
			valor=data.get('valor')
		)

		db.session.add(new_transaction)
		db.session.commit()

		return jsonify({'message': 'Transaction created successfully'}), 201

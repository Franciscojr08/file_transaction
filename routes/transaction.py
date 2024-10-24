from flask import request, jsonify

from database.session import db
from model.transaction import Transaction


def register_routes(app):
	@app.route('/cadastrar/transacao', methods=['POST'])
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

	@app.route('/listar/transacao', methods=['GET'])
	def list_transaction():
		transactions = Transaction.query.all()

		resultado = [{
			'id': transaction.id,
			'conta': transaction.conta,
			'agencia': transaction.agencia,
			'texto': transaction.texto,
			'valor': transaction.valor
	        } for transaction in transactions
		]

		return jsonify(resultado), 200

	@app.route("/transacao/<int:id>", methods=['GET'])
	def get_transaction(id):
		transaction = Transaction.query.get_or_404(id)
		resultado = transaction.__dict__
		del resultado['_sa_instance_state']

		return jsonify({'details': resultado}), 200

	@app.route("/delete/transacao/<int:id>", methods=['DELETE'])
	def delete_transaction(id):
		transaction = Transaction.query.get_or_404(id)
		db.session.delete(transaction)
		db.session.commit()

		return jsonify({'message': "Transação deletada com sucesso"}), 200

	@app.route("/atualizar/transacao/<int:id>", methods=['PUT'])
	def update_transaction(id):
		data = request.get_json()
		transaction = Transaction.query.get_or_404(id)

		transaction.conta = data.get('conta', transaction.conta)
		transaction.agencia = data.get('agencia', transaction.agencia)
		transaction.texto = data.get('texto', transaction.texto)
		transaction.valor = data.get('valor', transaction.valor)

		db.session.add(transaction)
		db.session.commit()

		return jsonify({'message': "Transacao atualizada com sucesso"}), 200

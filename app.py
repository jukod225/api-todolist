from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de tarefas (dados temporários)
tarefas = [
    {"id": 1, "titulo": "Estudar API", "feita": False},
    {"id": 2, "titulo": "Criar projeto no GitHub", "feita": True}
]

# Rota para obter todas as tarefas
@app.route("/tarefas", methods=["GET"])
def obter_tarefas():
    return jsonify(tarefas)

# Rota para adicionar uma nova tarefa
@app.route("/tarefas", methods=["POST"])
def adicionar_tarefa():
    nova_tarefa = request.json
    nova_tarefa["id"] = len(tarefas) + 1
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

# Rota para atualizar uma tarefa pelo ID
@app.route("/tarefas/<int:tarefa_id>", methods=["PUT"])
def atualizar_tarefa(tarefa_id):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa.update(request.json)
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

# Rota para excluir uma tarefa pelo ID
@app.route("/tarefas/<int:tarefa_id>", methods=["DELETE"])
def excluir_tarefa(tarefa_id):
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa["id"] != tarefa_id]
    return jsonify({"mensagem": "Tarefa excluída"}), 200

# Executar a API (somente se rodado localmente)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
    
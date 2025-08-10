from flask import Blueprint, request, jsonify
from .scraper import buscar_noticias

main = Blueprint('main', __name__)

@main.route('/buscar')
def buscar():
    termo =request.args.get('q')
    if not termo:
        return jsonify({"erro": "Parâmetro 'q' é obrigatório"}), 400
    
    resultados = buscar_noticias(termo)
    if not resultados:
        return jsonify({'erro': 'Nenhuma noticia encontrada'})
    
    return jsonify(resultados)
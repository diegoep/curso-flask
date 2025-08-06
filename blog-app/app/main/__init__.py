from flask import Blueprint

main = Blueprint('main', __name__)

from . import routes  # Importa as rotas e as associa ao blueprint
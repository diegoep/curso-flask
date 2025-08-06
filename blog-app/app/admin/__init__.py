from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import routes  # Importa as rotas e as associa ao blueprint
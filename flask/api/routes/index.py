from flask import Blueprint, render_template

index_blueprint = Blueprint(name='index', import_name=__name__)


@index_blueprint.route("/")
@index_blueprint.route("/index")
def index():
    print("rendering blueprint")
    return render_template("index.html")

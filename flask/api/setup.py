from flask import Flask


def create_app():
    # Create flask app
    app = Flask(__name__, template_folder="./../templates/")

    # Import all the routes
    from routes.index import index_blueprint
    from routes.start_valheim_server import start_valheim_server_blueprint

    # Register the different routes from the submodules
    app.register_blueprint(index_blueprint)
    app.register_blueprint(start_valheim_server_blueprint)

    return app

app = create_app()

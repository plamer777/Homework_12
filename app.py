"""This is a main Flask app file"""
from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint
from config import UPLOADS
# --------------------------------------------------------------------------

# Creation of Flask instance and blueprints' registration
app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    """This view provides a picture from local storage in secure way

    :param path: A name of the asked image file
    """
    return send_from_directory(UPLOADS, path)


app.run()


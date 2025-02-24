from flask import Flask, render_template
import os

#####

# Create Flask app with React frontend plugged in as template and static folders
REACT_PATH = os.path.abspath("../frontend/build")
app = Flask(
    __name__, template_folder=REACT_PATH, static_folder=REACT_PATH, static_url_path="/"
)


@app.route("/")
def index():
    """
    Serves the compiled React Frontend
    """

    return render_template("index.html")

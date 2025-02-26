import os
import random

from flask import Flask, jsonify, render_template

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


@app.route("/updateMessage")
def update_message():
    """
    Returns a message to display in the frontend
    """

    message_options = [
        "Have a great day!",
        "Thanks for reading!",
        "You're the best!",
        "Wow, what an article!",
    ]

    return jsonify(random.choice(message_options))

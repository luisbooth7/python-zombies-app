from flask import Flask, render_template
from flask_restful import Api
import controllers.zombie_controller as zombie_controller

app = Flask(__name__)
api = Api(app)


for resource in zombie_controller.resources:
    api.add_resource(*resource)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/editZombie/<id>')
def edit_user(id):
    return render_template("edit-zombie.html", id=id)


if __name__ == '__main__':
    app.run()

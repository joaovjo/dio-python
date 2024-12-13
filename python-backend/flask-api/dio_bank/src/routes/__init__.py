from flask import Flask

from dio_bank.src.routes.user.username import username

# Import the routes


# a simple page that says hello
app = Flask(__name__)
app.register_blueprint(username, url_prefix="/username")
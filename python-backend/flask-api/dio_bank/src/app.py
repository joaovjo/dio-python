import os
import click
import sqlalchemy as SA

from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(db.Model):
    id: Mapped[int] = mapped_column(SA.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(SA.String, unique=True)
    email: Mapped[str] = mapped_column(SA.String, unique=True)


class Post(db.Model):
    id: Mapped[int] = mapped_column(SA.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(SA.String, nullable=False)
    body: Mapped[str] = mapped_column(SA.String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(SA.DateTime, server_default=SA.func.now())
    author_id: Mapped[int] = mapped_column(SA.Integer, SA.ForeignKey("user.id"))


@click.command("init-db")  # Define um comando de linha de comando chamado "init-db"
def init_db_command():  # Função que será executada quando o comando "init-db" for chamado
    """Clear the existing data and create new tables."""  # Descrição do comando
    global db
    with current_app.app_context():
        db.create_all()
    click.echo("Initialized the database.")  # Exibe uma mensagem indicando que o banco de dados foi inicializado


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI=os.path.join("sqlite:///diobank.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Registrar o comando de inicialização do banco de dados
    app.cli.add_command(init_db_command)  # Adiciona o comando "init-db" à interface de linha de comando da aplicação

    # Inicializar a extensão SQLAlchemy
    db.init_app(app)

    return app

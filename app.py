# -*- coding: utf-8 -*-
# Time    : 2019/4/21 14:06
# Author  : LiaoKong

import os

from flask import Flask, render_template

from utils import db
from models import User, Movie

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控

db.init_app(app)


@app.route("/")
def index():
    user = User.query.first()
    movies = Movie.query.all()

    return render_template("index.html", name=user, movies=movies)


if __name__ == '__main__':
    app.run(debug=True)

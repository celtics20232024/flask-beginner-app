from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # タイトル
    title = db.Column(db.String(100), nullable=False)

    # 詳細
    description = db.Column(db.Text)

    # 締切日
    deadline = db.Column(db.Date)

    # 完了状態
    completed = db.Column(db.Boolean, default=False)
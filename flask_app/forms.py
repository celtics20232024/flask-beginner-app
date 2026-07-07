from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):

    # TODO：タイトルの入力欄を定義して下さい
	title=StringField("タイトル")
	
    # TODO：詳細の入力欄を定義して下さい
	discription=TextAreaField("詳細")
	
    # TODO：締切日の入力欄を定義して下さい
	deadline=DateField("詳細日")
	
    # TODO：完了状態を表すチェックボックスを定義して下さい
	completed=BooleanField("完了")
	
    # TODO：送信ボタンを定義して下さい
    submit=SubmitField("保存")

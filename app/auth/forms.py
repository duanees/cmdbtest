from flask_wtf import FlaskForm
from wtforms.validators import Required,length, DataRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField

class LoginForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired])
    password = PasswordField('Password',validators=[DataRequired])
    remember_me = BooleanField('Keep me logged in', default=False)
    submit = SubmitField('Log In')

class RegistForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired])
    worknum = StringField('Worknum', validators=[DataRequired])
    password1 = PasswordField('Password', validators=[DataRequired])
    password2 = PasswordField('Password', validators=[DataRequired])
    submit = SubmitField('submit')

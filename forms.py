from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, IntegerField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField("Matricula",[
        validators.DataRequired(message='El campo es requerido')
    ])
    nombre=StringField("Nombre",[
        validators.DataRequired(message='El nombre es requerido')
    ])
    apellido=StringField("Apellido",[
        validators.DataRequired(message='El apellido es requerido')
    ])
    correo=EmailField("Correo",[
        validators.DataRequired(message='El correo es requerido')
    ])
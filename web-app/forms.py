from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, IntegerField,TextAreaField,RadioField,SelectField, DecimalField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError

class PredictForm(FlaskForm):
   mean_radius = IntegerField('Mean Radius')
   mean_texture = StringField('Mean Texture')
   mean_perimeter = DecimalField('Mean Perimeter')
   mean_area = IntegerField('Mean Area')
   mean_smoothness = StringField('Mean Smoothness')
   submit = SubmitField('Predict')
   abc = "" # this variable is used to send information back to the front page

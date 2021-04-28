from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, IntegerField,TextAreaField,RadioField,SelectField, DecimalField, FloatField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError

class PredictForm(FlaskForm):
   mean_radius = FloatField('Mean Radius')
   mean_texture = FloatField('Mean Texture')
   mean_perimeter = FloatField('Mean Perimeter')
   mean_area = FloatField('Mean Area')
   mean_smoothness = FloatField('Mean Smoothness')
   submit = SubmitField('Predict')
   abc = "" # this variable is used to send information back to the front page

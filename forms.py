from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,  TextAreaField, BooleanField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class libraryForm(FlaskForm):
    title=StringField('title',validators=[DataRequired()])
    author=StringField('author',validators=[DataRequired()])
    year=IntegerField('date',validators=[DataRequired()])
    genre=StringField('genre',validators=[DataRequired()])
    description=TextAreaField('description',widget=TextArea())
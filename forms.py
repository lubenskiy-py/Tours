from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange, URL, Optional

class AddTourForm(FlaskForm):
    title = StringField("Назва", validators=[DataRequired()])
    price = FloatField("Ціна", validators=[DataRequired(), NumberRange(min=50)])
    description = TextAreaField("Опис", validators=[DataRequired()])
    image_url = StringField("URL зображення", validators=[URL(), Optional()])
    departure_id = SelectField("Напрямок", validators=[DataRequired()])
    submit = SubmitField("Додати тур")
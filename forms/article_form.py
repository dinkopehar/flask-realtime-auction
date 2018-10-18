from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, InputRequired
from flask_wtf.file import FileField, FileRequired
from .categories import choices
from wtforms.fields import (StringField,
                            SelectField,
                            IntegerField,
                            DateTimeField,
                            TextAreaField)


class ArticleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    category = SelectField(u'Category', choices=choices)
    town = StringField('Town', validators=[DataRequired()])
    minimal_price = IntegerField('Minimal price')
    article_image = FileField('Article_image', validators=[FileRequired()])
    time_left = DateTimeField('Time to end', validators=[InputRequired()],
                              format='%Y-%m-%d %H:%M:%S')
    description = TextAreaField('Description', validators=[DataRequired()])

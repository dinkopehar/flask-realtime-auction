from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, InputRequired
from flask_wtf.file import FileField, FileRequired
from .categories import choices
from wtforms.fields import (StringField,
                            SelectField,
                            IntegerField,
                            TimeField,
                            TextAreaField)


class ArticleForm(FlaskForm):
    name = StringField('Name of Article', validators=[DataRequired()])
    category = SelectField(u'Category', choices=choices)
    town = StringField('Town', validators=[DataRequired()])
    minimal_price = IntegerField('Minimal price')
    article_image = FileField('Article_image', validators=[FileRequired()])
    end_day = StringField('End Date', validators=[InputRequired()])  # String converted to date
    end_time = TimeField('End Time', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])

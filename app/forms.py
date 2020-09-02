from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, SelectMultipleField, TextAreaField
from app.models import Tag
from wtforms.validators import DataRequired

tag_choices = [
    ('fluent', 'Fluent'),
    ('proficient', 'Proficient'),
    ('familiar', 'Familiar')
]


class CreateTagForm(FlaskForm):
    name = StringField('Tag Name', validators=[DataRequired()])
    knowledge = SelectField('What\'s your Proficiency', choices=tag_choices)
    submit = SubmitField('Create Tag')


class UpdateTagForm(FlaskForm):
    name = StringField('Tag Name', validators=[DataRequired()])
    knowledge = SelectField('What\'s your Proficiency', choices=tag_choices)
    submit = SubmitField('Update Tag')


class DeleteTagForm(FlaskForm):
    name = StringField('Tag Name', validators=[DataRequired()])
    submit = SubmitField('Delete Tag')


class CreateProjectForm(FlaskForm):
    title = StringField('Project Title', validators=[DataRequired()])
    project_link = StringField('Project Link')
    short_description = TextAreaField("Short Description")
    long_description = TextAreaField("Long Description")
    tag_name = SelectMultipleField('Tag Name')
    submit = SubmitField('Create Project')


class UpdateProjectForm(FlaskForm):
    title = StringField('Project Title', validators=[DataRequired()])
    project_link = StringField('Project Link')
    short_description = TextAreaField("Short Description")
    long_description = TextAreaField("Long Description")
    tag_name = SelectMultipleField('Tag Name')
    submit = SubmitField('Update Project')


class DeleteProjectForm(FlaskForm):
    title = StringField('Project Title', validators=[DataRequired()])
    submit = SubmitField('Delete Project')

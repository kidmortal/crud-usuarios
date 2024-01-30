from wtforms import Form, EmailField, StringField, IntegerField, validators
import wtforms_json


wtforms_json.init()


class UserRegistrationForm(Form):
    id = IntegerField('Id')
    Name = StringField('Name', [validators.Length(min=5, max=15)])
    Email = EmailField('Email', [validators.Length(min=6, max=35),
                                 validators.email()])

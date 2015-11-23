from django.forms import CharField, ChoiceField, Form, NullBooleanField, TextInput

from livability.models import *

class EditForm(Form):
    yearDeveloped = CharField(max_length=4, required=False)
    name = CharField(max_length=200, required=False)
    author = CharField(max_length=200)
    url = CharField(max_length=200)
    description = TextInput()
    communitySize = ChoiceField(choices=Community_Size.SIZE_CHOICES)
    assessmentFocus = ChoiceField(choices=Assessment_Focus.FOCUS_CHOICES)
    audience = ChoiceField(choices=Audience.AUDIENCE_CHOICES)
    topicTransportation = NullBooleanField()
    topicHousing = NullBooleanField()
    topicInvestment = NullBooleanField()
    topicCompact = NullBooleanField()
    topicHealth = NullBooleanField()
    topicPreservation = NullBooleanField()
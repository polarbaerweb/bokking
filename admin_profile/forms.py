from django import forms
from django.forms import ModelForm

from actors import models as actor_md
from show_data import models as show_md

from . import models as md


class ActorsForm(ModelForm):
    class Meta:
        model = actor_md.Actors
        fields = "__all__"


class JobsForm(ModelForm):
    class Meta:
        model = actor_md.Jobs
        fields = "__all__"


class Prizes(ModelForm):
    class Meta:
        model = actor_md.Prizes
        fields = "__all__"


class CinemaForm(ModelForm):
    class Meta:
        model = md.Cinema
        fields = "__all__"


class HallForm(ModelForm):
    class Meta:
        model = md.Hall
        fields = "__all__"


class Sessions(ModelForm):
	class Meta:
		model = md.Session
		fields = "__all__"

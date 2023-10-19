from django.forms import ModelForm

from . import models as md

class CinemaForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['name'].widget.attrs['class'] = 'main__admin-input'
		self.fields['name'].widget.attrs['placeholder'] = 'enter cinema name'
		self.fields['name'].label_classes = ("main__admin-label", )


	class Meta:
		model = md.Cinema
		fields = "__all__"
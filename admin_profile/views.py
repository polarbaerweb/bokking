from django.shortcuts import render

from . import forms
from . import models as md



def save_data(request):
	FIELDS = {
		"cinema": ["name"]
	}

	FORMS_AND_MODELS_TYPE = {
		"cinema": forms.CinemaForm
	}

	FORMS = {
		"cinema": {
			"form": forms.CinemaForm,
			"title": "cinema",
		},
	}

	if request.method == "POST":
		form_type = request.POST.get("form_type")

		if form_type:
			form = FORMS_TYPE.get(form_type)(request.POST)
			if form.is_valid():
				form.save()
			else:
				print(form.errors)
	
	context = {
		"forms": FORMS
	}

	template_name = "admin_panel.html"

	return render(request, template_name, context)
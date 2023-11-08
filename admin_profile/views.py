"""
User Request handler
"""

import logging

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.core import serializers
from django.db import IntegrityError, OperationalError
from django.forms import ModelForm
from django.http import JsonResponse
from django.shortcuts import redirect, render, reverse
from django.views.decorators.http import require_http_methods

from actors import models as md
from show_data import models as show_models

from . import custom_validation as custom_validation
from . import forms
from . import models as admin_md

Logger = logging.getLogger(__name__)


FORMS_BOX = {
    "actors": {
        "form": forms.ActorsForm,
    },

    "jobs": {
        "form": forms.JobsForm,
    },

    "prizes": {
        "form": forms.Prizes,
    },

		"cinema": {
			"form": forms.CinemaForm
		},

		"sessions": {
			"form": forms.Sessions
		},
}


def handle_form_save(request, form: ModelForm):
	"""This function assists to save data if form is valid"""

	is_valid = custom_validation.is_form_valid(form)

	if not isinstance(is_valid, JsonResponse):
		try:
				form.save()
				return JsonResponse({"message": "saved"}, status=200)
		except (IntegrityError, OperationalError) as error:
				logging.error("An error occurred, %s", str(error))
				return JsonResponse({"message":  str(error)}, status=500)

	return is_valid


def is_superuser(user: User):
    """Check is user super"""
    return user.is_superuser


@user_passes_test(is_superuser, login_url="/user_auth/login/")
@require_http_methods(["GET", "POST"])
def save_data(request):
	"""Handle admin changes"""

	if request.method == "POST":
		form_type = request.POST.get("form_type")

		if not form_type:
				logging.error(
						"An error  ocurred, you did not indicate a form_type")
				return redirect(reverse("admin_profile:admin"))

		form_calling = FORMS_BOX[form_type]["form"]

		form = "photo" in request.FILES and form_calling(
				request.POST) or form_calling(request.POST, request.FILES)

		form_message = handle_form_save(request, form)

		print(form_message)

		return form_message

	template_name = "admin_panel.html"

	return render(request, template_name)


@user_passes_test(is_superuser, login_url="/user_auth/login/")
@require_http_methods(request_method_list=["GET"])
def get_data_by_name(request, name):
    """This function provides us with information needed"""

    queryset_dict = {
        "prizes": md.Prizes.objects.all(),
        "jobs": md.Jobs.objects.all(),
        "cinema": admin_md.Cinema.objects.all(),
        "hall": admin_md.Hall.objects.all(),
        "movie": show_models.Movie.objects.all(),
				"session": admin_md.Session.objects.all(),
    }

    if name not in queryset_dict.keys():
        return JsonResponse({"message": "Invalid 'name' parameter"}, status=400)

    try:
        data = serializers.serialize(
            "json", queryset=queryset_dict[name], fields=("id", "name")
        )
        return JsonResponse({"message": data})
    except (Exception, ) as e:
        return JsonResponse({"message": str(e)}, status=500)


def session_list(request):
	sessions = admin_md.Session.objects.all()
	template_name = "sessions.html"

	context = {
		"sessions": sessions
	}

	return render(request, template_name, context)


def delete_session(request, session_id):
	admin_md.Session.objects.get(id=session_id).delete()
	return redirect("admin_profile:session_list")
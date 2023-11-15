"""
User Request handler
"""

import logging
from typing import Union

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, OperationalError
from django.db.models import QuerySet
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

		"hall": {
			"form": forms.HallForm
		},

		"sessions": {
			"form": forms.Sessions
		},

		"genre": {
			"form": forms.GenreForm
		},

		"movie": {
			"form": forms.MovieForm
		}
}

LOGIN_URL = "/user_auth/login/"


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


@user_passes_test(is_superuser, login_url=LOGIN_URL)
@require_http_methods(["GET", "POST"])
def save_data(request):
	"""Handle admin changes"""

	if request.method == "POST":
		form_type = request.POST.get("form_type")
		img = request.FILES.get("img")


		if not form_type:
				logging.error("An error  ocurred, you did not indicate a form_type")
				
				return JsonResponse({"message": "server error, try  later our developers will fix bug"}, status=500)

		form_calling = FORMS_BOX[form_type]["form"]

		form = None  

		print(img)
		
		if img:
			form = form_calling(request.POST, request.FILES)
		else:
			form = form_calling(request.POST) 


		form_message = handle_form_save(request, form)


		return form_message

	template_name = "admin_panel.html"

	return render(request, template_name)



def get_filtered_session(filter_type: str = None, filter_ids: Union[int, list] = None) -> Union[QuerySet, object]:
	filters_dict = {
		"all": admin_md.Session.objects.all(),
		"cinema": admin_md.Session.objects.filter(cinema__id__in=filter_ids),
		"hall": admin_md.Session.objects.filter(hall__id__in=filter_ids),
	}
	
	sessions = filters_dict.get(filter_type)
	

	serialized_data = []

	for session in sessions:
		serialized_data.append(
			{
				"id": session.id,
				"is_vip": session.is_vip,
				"start_time": session.start_time.strftime("%H:%M"),
				"price": session.price,
				
				"cinema": session.cinema.name,
				"hall": session.hall.name,
				"movie_img": session.movie.img.url,
				"movie_id": session.movie.pk,
				"movie_name": session.movie.name,
			}
		)



	return serialized_data


@user_passes_test(is_superuser, login_url=LOGIN_URL)
@require_http_methods(request_method_list=["GET"])
def get_data_by_name(request, name: str):
    """This function provides us with information needed"""

    queryset_dict = {
        "prizes": md.Prizes.objects.all(),
        "jobs": md.Jobs.objects.all(),
				"actors": md.Actors.objects.all(),
				"genre": show_models.Genre.objects.all(),
        "cinema": admin_md.Cinema.objects.all(),
        "hall": admin_md.Hall.objects.all(),
        "movie": show_models.Movie.objects.all(),
				"session": get_filtered_session(filter_type="all", filter_ids=[]),
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


@user_passes_test(is_superuser, login_url=LOGIN_URL)
@require_http_methods(request_method_list=["GET"])
def get_data_by_name_and_related_obj(request, cinema_id: int):
	""" This function will get data by name and related object to it """

	try:
		cinema = admin_md.Cinema.objects.get(id=cinema_id)
		halls = cinema.halls.all()
		
		data = serializers.serialize("json", queryset=halls, fields=("id", "name"))

	except ObjectDoesNotExist:
		return JsonResponse({"message": "something went wrong try later"})
	else:
		return JsonResponse({"message": data})



@user_passes_test(is_superuser, LOGIN_URL)
@require_http_methods(["GET"])
def session_template(request):
	""" To get session list """

	template_name = "sessions.html"
	return render(request, template_name)


@user_passes_test(is_superuser, LOGIN_URL)
@require_http_methods(["POST"])
def session_filter(request):
	filter_type = request.POST.get("form_type")
	filter_ids =  request.POST.getlist("filter_name")


	sessions = get_filtered_session(filter_type, filter_ids)

	return JsonResponse({"sessions": sessions}, status=200, safe=False)


def delete_session(request, session_id: int):
	""" To delete session by its unique id """
	
	admin_md.Session.objects.get(id=session_id).delete()
	return redirect("admin_profile:session_list")
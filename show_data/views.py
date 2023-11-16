from math import floor

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.timezone import now

from . import models as md


def movies_list(request):
	movies_list = md.Movie.objects.all().order_by("-rating")
	collection = md.Collection.objects.all().order_by("name")


	half_films = floor((movies_list.count() * 50) / 100)

	context = {
		"top_movies": movies_list[:half_films],
		"similar_movies": movies_list[half_films:movies_list.count()],
		"movies_collection": collection,
	}
	
	template_name = "movies_list.html"

	return render(request, template_name, context)


def movies_detail(request, movie_id):
	movie = md.Movie.objects.get(id=movie_id)
	sessions = movie.sessions.filter(start_time__date=now().date())


	context = {
		"movie": movie,
		"sessions": sessions
	}

	template_name = "movies_detail.html"
	return render(request, template_name, context)
	

def get_genre_list(request):
	genre_list = md.Genre.objects.all()
	serialized = serializers.serialize("json", genre_list, fields=("id", "name"))
	return JsonResponse({"list": serialized}, status=200)

def get_genre_by_id(request, genre_id: int):
	genre = md.Genre.objects.get(id=genre_id)
	template_name = "genre_list.html"
	context = {
		"genre": genre
	}

	return render(request, template_name, context)
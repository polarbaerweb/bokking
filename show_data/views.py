from math import floor

from django.shortcuts import render

from . import models as md

def movies_list(request):
	movies_list = md.Movie.objects.all().order_by("-rating")
	collection = md.Collection.objects.all().order_by("title")


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
	context = {
		"movie": movie
	}

	template_name = "movies_detail.html"
	return render(request, template_name, context)
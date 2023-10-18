from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, reverse, render
from django.contrib.auth.hashers import make_password

from django.db import IntegrityError

from . import models as md


def user_login(request):
	template_name = "login.html"

	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(request, username=username, password=password)

		print(user)

		user is not None and login(request, user)

		not user and redirect(reverse("user_auth:login"))

	return render(request, template_name)


def user_signup(request):
	template_name = "signup.html"

	if request.method == "POST":
		# Text based data
		email = request.POST.get("email")
		
		username = request.POST.get("username")
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		
		password1 = request.POST.get("password1")
		password2 = request.POST.get("password2")
		
		# File Based data
		user_image = request.FILES.get("user_image")

		# validation
		if password1 != password2:
			return redirect("user_auth:signup")

		if len(password1) <= 7:
			return redirect("user_auth:signup")

		try:
			user = md.UserModel(
			email=email,
			username=username,
			password=make_password(password1),
			first_name=first_name,
			last_name=last_name
		)
		except IndentationError :
			return redirect(reverse("signup"))
		else:
			if user_image:
				user.user_image = user_image.name
			
			user.save()
			return redirect("user_auth:login")
	
	return render(request, template_name)

def user_logout(request):
	logout(request)
	return redirect(reverse("user_auth:login"))
"""
This module contains itself basic custom validation
"""

import logging
from functools import wraps
from typing import Union

from django.forms import ModelForm
from django.http import JsonResponse

Logger = logging.getLogger(__name__)


def is_form_valid(form: ModelForm) -> Union[JsonResponse, bool]:
	"""Form validation, if form is not valid return record it to log file and return JsonResponse"""
	
	if not form.is_valid():
			errors_dict = form.errors.as_json()
			errors_text = form.errors.as_text()
			logging.error("An error occurred %s", errors_text)
			return JsonResponse(errors_dict, status=400, safe=False)

from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_fun):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('store')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func	

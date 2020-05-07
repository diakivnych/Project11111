from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Person, Comment

def all_users(request):
	users = Person.objects.all()
	return render(request, 'students/all_users.html', {'users': users})

def author(request):
	return render(request, 'students/author.html')

def add_user(request):
	return render(request, 'students/new_user.html')

def leave_comment(request, user_id):
	print('OK')
	try:
		a = Person.objects.get(id = user_id)
	except:
		raise Http404('Користувача не знайдено')

	from django.utils import timezone
	new_comment = a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'], pub_date = timezone.now())
	new_comment.save()
	return HttpResponseRedirect(reverse(all_users))
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import *

def signup(request):
	if request.method == 'POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			#user = authenticate(username=username, password=raw_password)
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
			return HttpResponseRedirect(reverse('polls:list'))
	else:
		form=UserCreationForm()
	return render(request, 'polls/signup.html', {'form':form})

	
class IndexView(generic.TemplateView):
	model=Kraj
	template_name='index.html'

	

class VoteListView(generic.ListView):
	template_name = 'polls/votelist.html'
	context_object_name = 'latest_wybor_list'
	
	def get_queryset(self):
		"""Return the last five published questions"""
		return Wybor.objects.order_by('-id')[:10]


class DetailView(generic.DetailView):
	model = Wybor
	template_name = 'polls/detail.html'
	
	

class ResultsView(generic.DetailView):
	model = Wybor
	template_name = 'polls/results.html'

@login_required
def vote(request, wybor_id):
	try:
		wybor = get_object_or_404(Wybor, pk=wybor_id)
		print(str(wybor.id)+' '+wybor.nazwa)
		selected_candidate = wybor.kandydat_set.get(pk=request.POST['id'])
	except (KeyError):
		return render(request, 'polls/detail.html', 
		{'wybor': wybor,'error_message': "You didn't select a choice.",})	
	except (Kandydat.DoesNotExist):
		return render(request, 'polls/detail.html', 
		{'wybor': wybor,'error_message': "Object does not exist",})

	else:
		selected_candidate.votes += 1
		selected_candidate.save()
		return HttpResponseRedirect(reverse('polls:results', args=(wybor.id,)))
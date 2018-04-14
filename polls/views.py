from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import *

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_wybor_list'
	
	def get_queryset(self):
		"""Return the last five published questions"""
		return Wybor.objects.order_by('-id')[:5]
	
class DetailView(generic.DetailView):
	model = Wybor
	template_name = 'polls/detail.html'
	
class ResultsView(generic.DetailView):
	model = Wybor
	template_name = 'polls/results.html'

def vote(request, wybor_id):
	try:
		wybor = get_object_or_404(Wybor, pk=wybor_id)
		print(str(wybor.id)+' '+wybor.nazwa)
		selected_candidate = wybor.kandydat_set.get(pk=request.POST['adres'])
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
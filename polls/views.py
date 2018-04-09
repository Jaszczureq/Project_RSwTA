from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import *

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_kraj_list'
	
	def get_queryset(self):
		"""Return the last five published questions"""
		return Kraj.objects.order_by('-idKraj')[:5]
	
class DetailView(generic.DetailView):
	model = Kraj
	template_name = 'polls/detail.html'
	
class ResultsView(generic.DetailView):
	model = Kraj
	template_name = 'polls/results.html'

def vote(request, kraj_id):
	try:
		kraj = get_object_or_404(Kraj, pk=kraj_id)
		print(str(kraj.idKraj)+' '+kraj.nazwa)
		selected_adres = kraj.adres_zamieszkania_set.get(pk=request.POST['adres'])
		print(selected_adres.ulica+', '+selected_adres.miejscowosc)
	except (KeyError):
		return render(request, 'polls/detail.html', 
		{'kraj': kraj,'error_message': "You didn't select a choice.",})	
	except (Adres_zamieszkania.DoesNotExist):
		return render(request, 'polls/detail.html', 
		{'kraj': kraj,'error_message': "Object does not exist",})

	else:
		selected_adres.votes += 1
		selected_adres.save()
		return HttpResponseRedirect(reverse('polls:results', args=(kraj.idKraj,)))
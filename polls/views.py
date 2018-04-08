from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
import re

from .models import *

def index(request):
	latest_kraj_list = Kraj.objects.order_by('-idKraj')
	#template = loader.get_template('polls/index.html')
	context = {
		'latest_kraj_list': latest_kraj_list,
	}
	return render(request, 'polls/index.html', context)
	
def detail(request, kraj_id):
    kraj = get_object_or_404(Kraj, pk=kraj_id)
    return render(request, 'polls/detail.html', {'kraj': kraj})

def vote(request, kraj_id):
	kraj = get_object_or_404(Kraj, pk=kraj_id)
	try:
		selected_adres = kraj.adres_zamieszkania_set.get(pk=request.POST.get('adres_zamieszkania', False))
	except (KeyError, Adres_zamieszkania.DoesNotExist):
        # Redisplay the question voting form.
		return render(request, 'polls/detail.html', {'question': kraj,'error_message': "You didn't select a choice.",})
	else:
		selected_adres.votes += 1
		selected_adres.save()
		return HttpResponseRedirect(reverse('polls:results', args=(kraj.id,)))
	
def results(request, kraj_id):
	question = get_object_or_404(Kraj, pk=kraj_id)
	return render(request, 'polls/results.html', {'question':question})
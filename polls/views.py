from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Kraj

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
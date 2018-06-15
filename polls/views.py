from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils.decorators import method_decorator
from django.db.models import Q

from Project_RSwTA.forms import SignUpForm
from .models import *


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect(reverse('index'))
    else:
        form = SignUpForm()
    return render(request, 'polls/signup.html', {'form': form})


def hola(request):
    if request.user.is_superuser:
        return HttpResponseRedirect('/admin/')
    else:
        return HttpResponseRedirect('/')


class IndexView(generic.TemplateView):
    model = Kraj
    template_name = 'index.html'


@method_decorator(login_required, name='dispatch')
class VoteListView(generic.ListView):
    template_name = 'polls/votelist.html'
    context_object_name = 'latest_wybor_list'

    wybor_set = Wybor.objects.all().order_by('-id')
    wybors = list(wybor_set)
    cur = timezone.now()

    for i in wybors:

        if cur > i.dataRozpoczecia:
            if cur < i.dataZakonczenia:
                i.status = 0
                i.save()
            else:
                i.status = 1
                i.save()
        else:
            i.status = -1
            i.save()

        print(i.nazwa + " " + str(i.status))
        print(i.dataRozpoczecia)
        print(timezone.now())
        print(i.dataZakonczenia)

    def get_queryset(self):
        crit1 = Q(status="0")
        crit2 = Q(status="1")
        return Wybor.objects.filter(crit1 | crit2)


@method_decorator(login_required, name='dispatch')
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
        print(str(wybor.id) + ' ' + wybor.nazwa)
        selected_candidate = wybor.kandydat_set.get(pk=request.POST['id'])
    except (KeyError):
        return render(request, 'polls/detail.html',
                      {'wybor': wybor, 'error_message': "You didn't select a choice.", })
    except (Kandydat.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {'wybor': wybor, 'error_message': "Object does not exist", })

    else:
        selected_candidate.votes += 1
        selected_candidate.save()
        return HttpResponseRedirect(reverse('polls:results', args=(wybor.id,)))

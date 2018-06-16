from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic

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
        print("Jestem w pętli")
        print(cur)
        print(i.dataRozpoczecia)
        print(i.dataZakonczenia)
        if cur > i.dataRozpoczecia:
            if cur < i.dataZakonczenia:
                i.status = 0
                i.save()
                print("Zmiana statusu na 0")
            else:
                i.status = 1
                i.save()
                print("Zmiana statusu na 1")
        else:
            i.status = -1
            i.save()
            print("Zmiana statusu na -1")

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

    # def get(self, request, *args, **kwargs):
    #     model = Wybor
    #     pdf = render_to_pdf('polls/results.html', {'wybor': Wybor})
    #     return HttpResponse(pdf, content_type='application/pdf')


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
        # myuser = request.user
        # voters = list(Oddany_glos.objects.all())
        # cur = timezone.now()
        # if not voters:
        #     myosoba = Osoba.objects.get(imie='Jan')
        #     upraw = Uprawniony(osoba=myosoba, wybor=wybor)
        #     upraw.save()
        #     glos = Oddany_glos(user=myuser, dataOddaniaGlosu=cur, wybor=wybor)
        #     glos.save()
        #     print("Dodano oddany glos")
        # else:
        #     print("Lista voters nie pusta")
        #     for voter in voters:
        #         user=voter.get_username
        #         if user.username == myuser.username and wybor.nazwa == voter.wybor.nazwa:
        #             print("Istnieje glosujacy")
        #             return HttpResponseRedirect(reverse('polls:results', args=(wybor.id,)))
        #         else:
        #             print("Nie istenieje glosujacy")
        #             print("Username:" + myuser.username)
        #             print("Data oddania" + cur)
        #             print("Nazwa wyborow" + wybor.nazwa)
        #             time.sleep(1)
        #             glos = Oddany_glos(user=myuser, dataOddaniaGlosu=cur, wybor=wybor)
        #             glos.save()

        current_user = request.user
        votes = list(Oddany_glos.objects.all())
        current_time = timezone.now()
        exists = 0

        for i in votes:
            print("Username: " + i.author.username + ", Wybór: " + i.wybor.nazwa)

        if not votes:
            print("Lista jest pusta")
            glos = Oddany_glos(author=current_user, dataOddaniaGlosu=current_time, wybor=wybor)
            glos.save()
        else:
            print("Lista nie jest pusta")
            for vote in votes:
                if vote.author.username == current_user.username and vote.wybor.nazwa == wybor.nazwa:
                    print("Istnieje taki glos")
                    return HttpResponseRedirect(reverse('polls:results', args=(wybor.id,)))

        print("Nie istnieje taki glos")
        glos = Oddany_glos(author=current_user, dataOddaniaGlosu=current_time, wybor=wybor)
        glos.save()

        selected_candidate.votes += 1
        selected_candidate.save()
        return HttpResponseRedirect(reverse('polls:results', args=(wybor.id,)))

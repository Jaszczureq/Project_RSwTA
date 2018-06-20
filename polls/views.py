from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic
import subprocess

from Project_RSwTA.forms import SignUpForm
from Project_RSwTA.utils import render_to_pdf
from .models import *
from .tokens import account_activation_token


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your eVoting account.'
            message = render_to_string('registration/acc_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')

    else:
        form = SignUpForm()
    return render(request, 'polls/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Activation link is invalid!')


def hola(request):
    print('dupa')
    if request.user.is_superuser:
        return HttpResponseRedirect('/admin/')
    else:
        return HttpResponseRedirect('/')


def move_users(request):
    current_time = timezone.now()
    current_time_delta = timezone.now() - timezone.timedelta(minutes=10)

    crit1 = Q(date_joined__lt=current_time)
    crit2 = Q(date_joined__gt=current_time_delta)

    users = list(User.objects.filter(crit1 & crit2))

    print("Funkcja dziala poprawnie")
    for user in users:
        print("Nowo dodany uzytkownik: " + user.username)

    return HttpResponse('/')


class IndexView(generic.TemplateView):
    model = Kraj
    template_name = 'index.html'

    # subprocess.call('start', shell=True)


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


class AuthorizedListsView(generic.DetailView):
    model = Wybor
    template_name = 'polls/authorized.html'


@method_decorator(login_required, name='dispatch')
class DetailView(generic.DetailView):
    model = Wybor
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Wybor
    template_name = 'polls/results.html'


class ResultsViewPdf(generic.DetailView):
    model = Wybor
    template_name = 'polls/results_pdf.html'

    def get(self, request, pk, *args, **kwargs):
        model = Wybor.objects.get(pk=pk)
        pdf = render_to_pdf('polls/results_pdf.html', {'wybor': model})
        return HttpResponse(pdf, content_type='application/pdf')


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

        current_user = request.user
        votes = list(Oddany_glos.objects.all())
        current_time = timezone.now()

        for i in votes:
            print("Username: " + i.author.username + ", Wybór: " + i.wybor.nazwa)

        authorized = list(Uprawniony.objects.all())

        for i in authorized:
            if i.osoba.username == current_user.username and i.wybor.nazwa == wybor.nazwa:
                print("Uzytkownik jest uprawniony")

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
            else:
                print("Uzytkownik nie jest uprawniony")

        return HttpResponseRedirect(reverse('polls:results', args=(wybor.id,)))

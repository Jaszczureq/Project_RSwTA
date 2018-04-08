from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:kraj_id>/', views.detail, name='detail'),
	path('<int:kraj_id>/results/', views.results, name='results'),
	path('<int:kraj_id>/vote/', views.vote, name='vote'),
]

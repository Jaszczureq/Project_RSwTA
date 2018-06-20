from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.VoteListView.as_view(), name='list'),
    path('move/', views.move_users, name='move'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/voters', views.AuthorizedListsView.as_view(), name='voters'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/results/pdf', views.ResultsViewPdf.as_view(), name='results-pdf'),
    path('<int:wybor_id>/vote/', views.vote, name='vote'),
]

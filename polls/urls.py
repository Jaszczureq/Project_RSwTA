from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.VoteListView.as_view(), name='list'),
	#path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('<int:wybor_id>/vote/', views.vote, name='vote'),
]

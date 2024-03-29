from django.urls import path
from . import views
urlpatterns = [
	path('', views.index, name='index'), # ex /polls/
	path('<int:question_id>/', views.detail, name='detail'), # ex /polls/5
	path('<int:question_id>/results/', views.results, name='result'), # ex /polls/results
	path('<int:question_id>/vote/', views.vote, name='vote'), # ex /polls/5/vote
]
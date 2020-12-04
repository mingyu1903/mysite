from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('',views.helloworld, name='hellworld'),
        # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    path('<int:id>/vote/', views.vote, name='vote')
]
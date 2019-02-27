from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^activities/$',views.Activities,name='Activities'),
    url(r'^library/$',views.Library,name='Library'),
]

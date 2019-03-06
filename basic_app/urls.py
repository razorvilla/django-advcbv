from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
    url(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='detail'),
    # path('detail',views.SchoolDetailView.as_view(),name='anotherdetail')

]

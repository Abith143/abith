from django.urls import path, include
from .import views
urlpatterns=[
    path('',views.demo,name='demo'),
    path('abc/<int:movie_id>/',views.demo1,name='save'),
    path('update/<int:id>/',views.UPDATE,name='update'),
    path('delete/<int:id>/',views.DELETE,name='delete'),
    path('add',views.ADD,name='add')
]

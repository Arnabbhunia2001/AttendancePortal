from django.urls import path
from . import views
urlpatterns=[
    # path('',views.home,name="home"),
    path('home2',views.home2,name="home2"),
    path('',views.authenticatePage,name='authenticatePage'),
    path('saveData',views.saveData,name="saveData"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('signout',views.signout,name='signout'),

    # views.home is function call from views.py
]
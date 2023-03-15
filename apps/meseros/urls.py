from django.urls import path
from . import views

urlpatterns =[
    path('meseros_list', views.meseros_list, name='meseros_list')

#    URLs para las vistas basadas en clases
    path("meseros_list_vc/", views.MeserosList.as_view(), name="meseros_list_vc"),
    path("meseros_edit_vc/<int:pk>", views.MeserosUpdate.as_view(), name="meseros_edit_vc"),
    path("meseros_delete_vc/<int:pk>", views.MeserosDelete.as_view(), name="meseros_delete_vc"),
]
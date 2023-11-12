from django.urls import path

from basic_app import views

urlpatterns = [
    path('viloyat/', views.ViloyatList.as_view()),
    path('tuman/', views.TumanList.as_view()),
    path('stansiya/', views.StansiyaList.as_view()),
    path('osimlik/', views.OsimlikList.as_view()),
    path('hashorot/', views.HashorotList.as_view()),
    path('datahashorot/', views.DataHashorotList.as_view()),
    path('data/', views.dataSList.as_view()),

]

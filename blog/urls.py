from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('listpost/',views.BlogListView.as_view(),name ='listpost'),

]
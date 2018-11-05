from . import views
from django.urls import path
from django.conf.urls import url
# urlpatterns =[
#     path('', views.index, name='index'),
#     url(r'^/chat/$', views.chat, name='chat'),
# ]

urlpatterns = [
    path('', views.Rgistration.as_view(), name='registration'),
    url(r'^index$', views.index, name='index'),
    url(r'^chat/(?P<room_name>[^/]+)/$', views.room, name='room'),
]
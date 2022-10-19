from django.urls import path, include
from messenger import views

urlpatterns = [
    path('messages/<slug:chats>/', views.GetDialog.as_view()),
    path('messages/', views.GetChats.as_view()),
    path('<slug:account_slug>/', views.GetAccount.as_view())
]
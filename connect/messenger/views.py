from django.shortcuts import render
from django.http import Http404
from .serializer import AccountSerializer, MessagesSerializer, ChatsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import account, chats, message
# Create your views here.

class GetDialog(APIView):
    def get(self, request, format=None):
        messages = message.object.all()
        serializer = MessagesSerializer(messages, many=True)
        return Response(serializer.data)

class GetChats(APIView):
    def get(self, request, format=None):
        chat_list = chats.objects.all()
        serializer = ChatsSerializer(chat_list, many=True)
        return Response(serializer.data)

class GetAccount(APIView):
    def get_object(self, account_slug):
        try:
            return account.objects.get(slug = account_slug)
        except account.DoesNotExist:
            raise Http404

    def get(self, request, account_slug, format=None):
        data = self.get_object(account_slug)
        serializer = AccountSerializer(data)
        return Response(serializer.data)

""" def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
 """        
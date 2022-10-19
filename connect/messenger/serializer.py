from rest_framework import serializers

from .models import account, chats, message

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = (
            "slug",
            "author_name",
            "get_adress",
            "message",
            "date",
        )

class ChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = chats
        fields = (
            "slug",
            "person_name",
            "last_message",
        )

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = (
            "slug",
            "chats",
            "name"
        )
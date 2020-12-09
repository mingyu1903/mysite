from rest_framework import serializers
from .models import Room, Question, Choice, Hupu

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 
                  'votes_to_skip','created_at')

class HupuSerializers(serializers.ModelSerializer):

    class Meta:
        model = Hupu
        fields = ('id', 'hupu_title', 'hupu_content')

class QuestionSerializers(serializers.ModelSerializer):

    class Meta:
        # model = Choice
        # fields = ('question', 'choice_text', 'votes',)

        model = Question
        fields = ('id', 'question_text', 'was_published_recently')
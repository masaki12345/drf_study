# from .models import Post
from rest_framework import serializers
from .models import Profession,Person



class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    # Profession = ProfessionSerializer(many=False, read_only=True)
    class Meta:
        model = Person
        fields = '__all__'
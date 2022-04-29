from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    roll_no = serializers.IntegerField()
    major = serializers.CharField()

    def create(self, validated_data):
        print(validated_data)
        return Student.objects.create(**validated_data)

    
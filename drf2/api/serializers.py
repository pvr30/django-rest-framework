from dataclasses import field
from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student

# validate func
# def name_length_check(value):
#     if len(value) < 4:
#         raise serializers.ValidationError("name length should be more than 4")
#     return value


# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(validators=[name_length_check])
#     roll_no = serializers.IntegerField()
#     major = serializers.CharField()

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll_no = validated_data.get('roll_no', instance.roll_no)
#         instance.major = validated_data.get('major', instance.major)

#         instance.save()
#         return instance

#     # field level validation
#     def validate_roll_no(self, value):
#         if value > 100:
#             raise serializers.ValidationError('Seats were Full')
#         return value

#     # object level validation
#     def validate(self, attrs):
#         majors = ['Physics', 'Chemistry', 'Maths', 'Biology']
#         major = attrs.get('major')
#         if major not in majors:
#             raise serializers.ValidationError("major should be from ['Physics', 'Chemistry', 'Maths', 'Biology']")
#         return attrs


# Model Serializer

class StudentSerializer(serializers.ModelSerializer):
    def name_length_check(value):
        if len(value) < 4:
            raise serializers.ValidationError("name length should be more than 4")
        return value

    name = serializers.CharField(validators=[name_length_check])
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll_no', 'major']

    
     # field level validation
    def validate_roll_no(self, value):
        if value > 100:
            raise serializers.ValidationError('Seats were Full')
        return value

    
    # object level validation
    def validate(self, attrs):
        majors = ['Physics', 'Chemistry', 'Maths', 'Biology']
        major = attrs.get('major')
        if major not in majors:
            raise serializers.ValidationError("major should be from ['Physics', 'Chemistry', 'Maths', 'Biology']")
        return attrs
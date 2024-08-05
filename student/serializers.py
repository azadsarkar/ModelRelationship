from rest_framework import serializers
from .models import Student,Subject,StudentSubject



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields='__all__'


class StudentSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset = Subject.objects.all(),many=True,write_only=True)# nested serializer
    
    class Meta:
        model=Student
        fields=["subject", "first_name", "last_name", "roll", "email"]

    def create(self, validated_data):
        subject = validated_data.pop("subject")
        instance = Student.objects.create(**validated_data)
        for sub in subject:
            StudentSubject.objects.create(student=instance,subject = sub)
        
        return instance

class StudentSubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model=StudentSubject
        fields="__all__"
        
class StudentSubjectGetSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.first_name")
    student_roll = serializers.CharField(source="student.roll")
    subjct_name = serializers.CharField(source="subject.subject_name")
    class Meta:
        model=StudentSubject
        fields="__all__"


class StudentSubjectUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model=StudentSubject
        fields=["student"]

from rest_framework import serializers
from .models import Student

class Studentserializrs(serializers.ModelSerializer):
    class Meta:
        model = Student
        field = ['id','name','roll','city']

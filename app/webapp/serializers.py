from rest_framework import serializers
from . models import employees


class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        #fields = ('firstname', 'lastname')
        fields = '__all__'

class nameSerializer(serializers.Serializer):

        name = serializers.CharField(max_length=20)
        

from rest_framework import serializers
from .models import Component, ComponentGroup

class ComponentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentGroup
        fields = ('id', 'name')
        #fields = '__all__'
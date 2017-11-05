from rest_framework import serializers
from .models import Component, ComponentGroup, ThreatCatalogue, Threat, CountermeasureCatalogue, Countermeasure, Responsible, Role, LifecyclePhase

class ComponentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentGroup
        fields = ('id', 'name')
        #fields = '__all__'

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id', 'name')
        #fields = '__all__'

class ThreatCatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreatCatalogue
        fields = ('id', 'name')
        #fields = '__all__'

class ThreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threat
        fields = ('id', 'name', 'description')
        #fields = '__all__'

class CountermeasureCatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountermeasureCatalogue
        fields = ('id', 'name')
        #fields = '__all__'

class CountermeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countermeasure
        fields = ('id', 'name', 'description')
        #fields = '__all__'

class ResponsibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsible
        fields = ('id', 'role', 'cm')
        #fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('name', 'description')
        #fields = '__all__'

class LifecyclePhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifecyclePhase
        fields = ('id', 'name')
        #fields = '__all__'
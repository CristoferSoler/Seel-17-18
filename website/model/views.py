from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  Component, ComponentGroup, ThreatCatalogue, Threat, CountermeasureCatalogue, Countermeasure, Responsible, Role, LifecyclePhase, BSIArticle
from .serializer import  ComponentSerializer, ComponentGroupSerializer, ThreatCatalogueSerializer, ThreatSerializer, CountermeasureCatalogueSerializer, CountermeasureSerializer, ResponsibleSerializer, RoleSerializer, LifecyclePhaseSerializer, BSIArticleSerializer

# Create your views here.

#Lists all ComponentGroupList or create a new one
#ComponentGroups/
class ComponentGroupList(APIView):
    
    def get(self, request):
        componentGroups = ComponentGroup.objects.all()
        serializer = ComponentGroupSerializer(componentGroups, many=True)
        return Response(serializer.data)

    def post(self):
        pass

#Lists all componentList or create a new one
#Component/
class ComponentList(APIView):
    
    def get(self, request):
        component = Component.objects.all()
        serializer = ComponentSerializer(component, many=True)
        return Response(serializer.data)

    def post(self):
        pass

#Lists all ThreatCatalogue or create a new one
#ThreatCatalogue/
class ThreatCatalogueList(APIView):
    
    def get(self, request):
        threatCatalogue = ThreatCatalogue.objects.all()
        serializer = ThreatCatalogueSerializer(threatCatalogue, many=True)
        return Response(serializer.data)

    def post(self):
        pass

#Lists all Threat or create a new one
#Threat/
class ThreatList(APIView):
    
    def get(self, request):
        threat = Threat.objects.all()
        serializer = ThreatSerializer(threat, many=True)
        return Response(serializer.data)

    def post(self):
        pass

#Lists all CountermeasureCatalogue or create a new one
#CountermeasureCatalogue/
class CountermeasureCatalogueList(APIView):
    
    def get(self, request):
        countermeasureCatalogue = CountermeasureCatalogue.objects.all()
        serializer = CountermeasureCatalogueSerializer(countermeasureCatalogue, many=True)
        return Response(serializer.data)

    def post(self):
        pass

#Lists all Countermeasure or create a new one
#Countermeasure/
class CountermeasureList(APIView):
    
    def get(self, request):
        countermeasure = Countermeasure.objects.all()
        serializer = CountermeasureSerializer(countermeasure, many=True)
        return Response(serializer.data)

    def post(self):
        pass

#Lists all Responsible or create a new one
#Responsible/
class ResponsibleList(APIView):
    
    def get(self, request):
        responsible = Responsible.objects.all()
        serializer = ResponsibleSerializer(responsible, many=True)
        return Response(serializer.data)

    def post(self):
        pass

#Lists all Role or create a new one
#Role/
class RoleList(APIView):
    
    def get(self, request):
        role = Role.objects.all()
        serializer = RoleSerializer(role, many=True)
        return Response(serializer.data)

    def post(self):
        pass

#Lists all LifecyclePhase or create a new one
#LifecyclePhase/
class LifecyclePhaseList(APIView):
    
    def get(self, request):
        lifecyclePhase = LifecyclePhase.objects.all()
        serializer = LifecyclePhaseSerializer(lifecyclePhase, many=True)
        return Response(serializer.data)

    def post(self):
        pass

# Lists all BSI catalog
# BSIArticle/
class BSIArticleList(APIView):
    def get(self, request):
        bsi_arts = BSIArticle.objects.all()
        serializer = BSIArticleSerializer(bsi_arts, many=True)
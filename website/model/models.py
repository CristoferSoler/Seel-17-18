from abc import ABC

from django.db import models


class ComponentGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Component(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    group = models.ForeignKey('ComponentGroup', blank=False)

    def __str__(self):
        return self.name


class ThreatCatalogue(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Threat(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CountermeasureCatalogue(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Countermeasure(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Responsible(models.Model):
    """
    This abstract class represents the link between a role and a countermeasure. Each countermeasure has a responsible initiation role and a responsible implementation role.
    """
    id = models.IntegerField(primary_key=True)
    role = models.ForeignKey('Role', blank=False)
    cm = models.ForeignKey('Countermeasure', blank=False)

    def __init__(self, role, countermeasure):
        role = role
        countermeasure = countermeasure

    def get_role(self):
        return self.role

    def get_countermeasure(self):
        return self.cm


class ResponsibleInit(Responsible):
    @staticmethod
    def deliver(role, countermeasure):
        for e in ResponsibleInit.objects.all():
            if e.get_role().equals(role) & e.get_countermeasure().equals(countermeasure):
                return e

        return ResponsibleInit(role, countermeasure)

    def __str__(self):
        return 'According to countermeasure %s the role %s is responsible for initiation.' % (
            self.cm.name, self.role.name)


class ResponsibleImpl(Responsible):
    @staticmethod
    def deliver(role, countermeasure):
        for e in ResponsibleImpl.objects.all():
            if e.get_role().equals(role) & e.get_countermeasure().equals(countermeasure):
                return e

        return ResponsibleImpl(role, countermeasure)

    def __str__(self):
        return 'According to countermeasure %s the role %s is responsible for implementation.' % (
            self.cm.name, self.role.name)


class Checking(models.Model):
    """
    This class represents a single checking ('Prüffrage') of a countermeasure.
    """
    description = models.TextField()
    countermeasure = models.ForeignKey('Countermeasure', blank=False)

    def __str__(self):
        return 'Compliance with countermeasure %s can be proven by:\n%s' % (self.countermeasure, self.description)


class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class LifecyclePhase(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

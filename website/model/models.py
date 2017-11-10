<<<<<<< HEAD
from abc import ABC
from django.db import models


class ComponentGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
=======
from django.db import models


class BSIArticle(models.Model):
    COMPONENT = 'C'
    THREAT = 'T'
    C_MEASURE = 'CM'
    ARTICLE_TYPE = (
        (COMPONENT, 'Component'),
        (THREAT, 'Threat'),
        (C_MEASURE, 'Countermeasure'),
    )
    id = models.CharField(primary_key=True, max_length=10)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    article_type = models.CharField(max_length=2, choices=ARTICLE_TYPE) 
>>>>>>> 3e556736b8a57ffb1aa106f31046089b47abd21d

    def __str__(self):
        return self.name

<<<<<<< HEAD

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
=======
    # probably needed - please remove if unused
    def is_component(self):
        return self.article_type in (COMPONENT)

    def is_threat(self):
        return self.article_type in (THREAT)

    def is_countermeasure(self):
        return self.article_type in (C_MEASURE)

    def whatType(self):
        return self.article_type;

>>>>>>> 3e556736b8a57ffb1aa106f31046089b47abd21d

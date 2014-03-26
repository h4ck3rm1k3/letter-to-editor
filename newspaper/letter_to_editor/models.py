from django.db import models

# Create your models here.

class Website(models.Model):
    domain = models.CharField(max_length=255, primary_key=True)
    url    = models.URLField(primary_key=True)

class Webpage(models.Model):
    url = models.URLField(primary_key=True)

class Webcache(models.Model):
    page = models.ForeignKey('Webpage')
    contents = models.FileField()

class WikipediaPage(Webpage):
    lang = models.CharField(max_length=2)
    page = models.DateTimeField('date published')

class SocialAccount(Webpage):
    site = models.ForeignKey('Website')
    name = models.CharField(max_length=50)
    page = models.ForeignKey('Webpage')

class Phone(Webpage):
    number = models.CharField(max_length=50)
    role = models.CharField(max_length=20)


class Image(models.Model):
    name = models.CharField(max_length=255)
    image                = models.ImageField()
    caption              = models.CharField(max_length=255)

class Location(Image):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)

class Person(models.Model):
    name = models.CharField(max_length=50)
    social = models.ManyToManyField("SocialAccount")
    phone = models.ManyToManyField("Phone")

class History(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

class PersonRole(History):
    role = models.CharField(max_length=50)
    person = models.ForeignKey(Person)

class Company(models.Model):
    name = models.CharField(max_length=50)
    logo =   models.ForeignKey('Logo')
    image =   models.ForeignKey('Image')
    owners = models.ManyToManyField("Person")
    founder              = models.ForeignKey('Person')
    president            = models.ForeignKey('PersonRole')
    generalmanager       = models.ForeignKey('PersonRole')
    staff                = models.ManyToManyField("PersonRole")
    headquarters         = models.ForeignKey('Location')
    website              = models.ForeignKey('Website')
    foundation           = models.DateField()
    phone                = models.ManyToManyField("Phone")

class CirculationHistory(models.Model):
    circulation          = models.IntegerField(blank=True, null=True)
    circulation_date     = models.DateField()

class Newspaper(Company):
    name = models.CharField(max_length=50)
    newspaper_type       = models.CharField(max_length=50)
    newspaper_format     = models.CharField(max_length=50)
    publisher            = models.ForeignKey('PersonRole')
    editor               = models.ForeignKey('PersonRole')
    chiefeditor          = models.ForeignKey('PersonRole')
    assoceditor          = models.ForeignKey('PersonRole')
    maneditor            = models.ForeignKey('PersonRole')
    newseditor           = models.ForeignKey('PersonRole')
    managingeditordesign = models.ForeignKey('PersonRole')
    campuseditor         = models.ForeignKey('PersonRole')
    campuschief          = models.ForeignKey('PersonRole')
    metroeditor          = models.ForeignKey('PersonRole')
    metrochief           = models.ForeignKey('PersonRole')
    opeditor             = models.ForeignKey('PersonRole')
    sportseditor         = models.ForeignKey('PersonRole')
    photoeditor          = models.ForeignKey('PersonRole')

    #name of Director of Interactive
    dirinteractive       = models.ForeignKey('PersonRole')

    political            = models.CharField(max_length=50)
    language             = models.CharField(max_length=50)
    ceased_publication   = models.DateField()
    relaunched           = models.ManyToManyField(History)
    circulation          = models.ManyToManyField(CirculationHistory)
    sister_newspapers    = models.ManyToManyField(Newspaper)
    ISSN                 = models.CharField(max_length=50)
    oclc                 = models.CharField(max_length=50)
    # the newspaper's online free achives
    free                 =  models.ForeignKey('Website')

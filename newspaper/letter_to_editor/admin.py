from django.contrib import admin

# Register your models here.

from letter_to_editor.models import (
    CirculationHistory,
    Company,
    History,
    Image,
    Location,
    Newspaper,
    Person,
    PersonRole,
    Phone,
    SocialAccount,
    Webcache,
    Webpage,
    Website,
    WikipediaPage)

for model in (
    CirculationHistory,
    Company,
    History,
    Image,
    Location,
    Newspaper,
    Person,
    PersonRole,
    Phone,
    SocialAccount,
    Webcache,
    Webpage,
    Website,
    WikipediaPage) :
    admin.site.register(model)

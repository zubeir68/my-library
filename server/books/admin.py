# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book

@admin.register(Book)

# Register your models here.

class bookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'description']
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import CaseMaster, ModuleMaster, TemplateMaster

admin.site.register(CaseMaster)
admin.site.register(ModuleMaster)
admin.site.register(TemplateMaster)
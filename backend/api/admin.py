from django.contrib import admin

from .models import Company, Vacancy, DetailVacancy, Resume

admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(DetailVacancy)
admin.site.register(Resume)
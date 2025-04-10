from django.urls import path 
from .views import Companies, OneCompany, VacanciesByCompany, DetailedVacancy, ProtectedView, RegisterView, Vacancies, resume

urlpatterns = [
    path('company/', Companies),
    path('company/<int:id>/', OneCompany),
    path('resume/', resume),
    path('company/<int:id>/vacancy/', VacanciesByCompany.as_view()),
    path('vacancy/', Vacancies.as_view()),
    path('vacancy/<int:id>/details/', DetailedVacancy.as_view()),
    path('register/', RegisterView.as_view()),
    path('protected/', ProtectedView.as_view(), name='protected')
]
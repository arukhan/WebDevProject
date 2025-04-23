from django.urls import path
from .views import Companies, OneCompany, CreateCompany, UpdateCompany, DeleteCompany, \
    Vacancies, VacanciesByCompany, DetailVacancy, CreateVacancy, UpdateVacancy, DeleteVacancy, \
    CreateDetailVacancy, UpdateDetailVacancy, DeleteDetailVacancy, ResumeListView, CreateResume, UpdateResume, DeleteResume, RegisterView, ProtectedView, VacancyListAPIView, CompanyListAPIView

urlpatterns = [
    path('companies/', Companies),
    path('company/<int:id>/', OneCompany),
    path('company/create/', CreateCompany),
    path('company/update/<int:id>/', UpdateCompany),
    path('company/delete/<int:id>/', DeleteCompany),
    
    path('vacancies/', Vacancies.as_view()),
    path('vacancies/create/', CreateVacancy.as_view()),
    path('vacancies/update/<int:id>/', UpdateVacancy.as_view()),
    path('vacancies/delete/<int:id>/', DeleteVacancy.as_view()),
    path('vacancies/company/<int:id>/', VacanciesByCompany.as_view()),

    path('vacancy/<int:id>/details/', DetailVacancy.as_view()),
    path('vacancy/details/create/', CreateDetailVacancy.as_view()),
    path('vacancy/details/update/<int:id>/', UpdateDetailVacancy.as_view()),
    path('vacancy/details/delete/<int:id>/', DeleteDetailVacancy.as_view()),
    
    path('resumes/', ResumeListView.as_view()),
    path('resumes/create/', CreateResume.as_view()),
    path('resumes/update/<int:id>/', UpdateResume.as_view()),
    path('resumes/delete/<int:id>/', DeleteResume.as_view()),
    
    path('register/', RegisterView.as_view()),
    path('protected/', ProtectedView.as_view()),
    path('vacancy/', VacancyListAPIView.as_view()),
    path('company/', CompanyListAPIView.as_view()),
]

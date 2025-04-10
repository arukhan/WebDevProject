from django.shortcuts import render
from .models import Company, Vacancy, DetailVacancy, Resume
from .serializer import CompanySerializer, VacancySerializer, DetailVacancySerializer, UserSerializer, ResumeSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions

@api_view(['GET'])
def Companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def OneCompany(request, id):
    company = Company.objects.get(id=id)
    serializer = CompanySerializer(company)
    return Response(serializer.data)

@api_view(['GET'])
def resume(request):
    resume = Resume.objects.all()
    serializer = ResumeSerializer(resume, many = True)
    return Response(serializer.data)

class Vacancies(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many = True)
        return Response(serializer.data)

class VacanciesByCompany(APIView):
    def get(self, request, id):
        company = Company.objects.get(id=id)
        vacancies = company.vacancies.all()
        serializer = VacancySerializer(vacancies, many = True)
        return Response(serializer.data)
    
class DetailedVacancy(APIView):
    def get(self, request, id):
        vacancy = Vacancy.objects.get(id = id)
        details = vacancy.details.all()
        serializer = DetailVacancySerializer(details, many = True)
        return Response(serializer.data)


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': f'Привет, {request.user.username}!'})


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=201)
        return Response(serializer.errors, status=400)

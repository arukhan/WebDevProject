from django.shortcuts import render
from .models import Company, Vacancy, DetailVacancy, Resume
from .serializer import CompanySerializer, VacancySerializer, DetailVacancySerializer, ResumeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django.contrib.auth import authenticate
from rest_framework.generics import ListAPIView

@api_view(['GET'])
def Companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def OneCompany(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        raise NotFound(detail="Company not found")
    serializer = CompanySerializer(company)
    return Response(serializer.data)

@api_view(['POST'])
def CreateCompany(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def UpdateCompany(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        raise NotFound(detail="Company not found")
    serializer = CompanySerializer(company, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def DeleteCompany(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        raise NotFound(detail="Company not found")
    company.delete()
    return Response({"message": "Company deleted successfully"}, status=204)


class Vacancies(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    
class DetailVacancy(APIView):
    def get(self, request, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist:
            raise NotFound(detail="Vacancy not found")

        details = vacancy.details.all()
        serializer = DetailVacancySerializer(details, many=True)
        return Response(serializer.data)
    
class VacanciesByCompany(APIView):
    def get(self, request, id):
        try:
            company = Company.objects.get(id=id)
        except Company.DoesNotExist:
            raise NotFound(detail="Company not found")
        vacancies = company.vacancies.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

class CreateVacancy(APIView):
    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UpdateVacancy(APIView):
    def put(self, request, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist:
            raise NotFound(detail="Vacancy not found")
        serializer = VacancySerializer(vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class DeleteVacancy(APIView):
    def delete(self, request, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist:
            raise NotFound(detail="Vacancy not found")
        vacancy.delete()
        return Response({"message": "Vacancy deleted successfully"}, status=204)

class DetailVacancyListView(APIView):
    def get(self, request, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist:
            raise NotFound(detail="Vacancy not found")
        details = vacancy.details.all()
        serializer = DetailVacancySerializer(details, many=True)
        return Response(serializer.data)

class CreateDetailVacancy(APIView):
    def post(self, request):
        serializer = DetailVacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UpdateDetailVacancy(APIView):
    def put(self, request, id):
        try:
            detail = DetailVacancy.objects.get(id=id)
        except DetailVacancy.DoesNotExist:
            raise NotFound(detail="DetailVacancy not found")
        serializer = DetailVacancySerializer(detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class DeleteDetailVacancy(APIView):
    def delete(self, request, id):
        try:
            detail = DetailVacancy.objects.get(id=id)
        except DetailVacancy.DoesNotExist:
            raise NotFound(detail="DetailVacancy not found")
        detail.delete()
        return Response({"message": "DetailVacancy deleted successfully"}, status=204)


class ResumeListView(APIView):
    def get(self, request):
        resumes = Resume.objects.all()
        serializer = ResumeSerializer(resumes, many=True)
        return Response(serializer.data)

class CreateResume(APIView):
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UpdateResume(APIView):
    def put(self, request, id):
        try:
            resume = Resume.objects.get(id=id)
        except Resume.DoesNotExist:
            raise NotFound(detail="Resume not found")
        serializer = ResumeSerializer(resume, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class DeleteResume(APIView):
    def delete(self, request, id):
        try:
            resume = Resume.objects.get(id=id)
        except Resume.DoesNotExist:
            raise NotFound(detail="Resume not found")
        resume.delete()
        return Response({"message": "Resume deleted successfully"}, status=204)


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': f'Hello, {request.user.username}! This is a protected view.'})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)


class VacancyListAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [IsAuthenticated]

class CompanyListAPIView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
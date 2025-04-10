from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company, Vacancy, DetailVacancy, Resume

class CompanySerializer(serializers.ModelSerializer):             #ModelSerializer
    class Meta:
        model = Company
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'
    

class VacancySerializer(serializers.ModelSerializer):                 #Serializer
    id = serializers.IntegerField()
    company_id = serializers.IntegerField(source='company.id')


    class Meta:
        model = Vacancy
        fields = ['id', 'name', 'experience', 'salary', 'company_id']


class DetailVacancySerializer(serializers.Serializer):            #Serializer
    name = serializers.CharField(max_length=255)
    requirements = serializers.CharField(max_length=255)
    salary = serializers.IntegerField()
    experience = serializers.IntegerField()
    hours =serializers.IntegerField()
    skills = serializers.CharField(max_length=255)
    vacancy_id = serializers.IntegerField()

    def create(self, validated_data):
        return DetailVacancy.objects.create(**validated_data)
    
    def update(self, instance, validated_data ):
        instance.requirements = validated_data.get('requirements', instance.requirements)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.hours = validated_data.get('hours', instance.hours)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.vacancy = validated_data.get('vacancy', instance.vacancy)
        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data.get('email', ''),
        )
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user
    
    
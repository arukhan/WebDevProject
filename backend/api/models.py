from django.db import models

class Company(models.Model):
    name = models.CharField(max_length= 255)
    description = models.CharField(max_length= 255)
    field = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = models.CharField(max_length= 255)
    experience = models.IntegerField()
    salary = models.IntegerField()
    company = models.ForeignKey(Company, on_delete= models.CASCADE, related_name= "vacancies")

    def __str__(self):
        return self.name
    
class DetailVacancy(models.Model):
    name = models.CharField(max_length=255)
    requirements = models.CharField(max_length= 255)
    salary = models.IntegerField()
    experience = models.IntegerField()
    hours = models.IntegerField()
    skills = models.CharField(max_length=255)
    vacancy = models.ForeignKey(Vacancy, on_delete= models.CASCADE, related_name= "details")

    def __str__(self):
        return self.name 

class Resume(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    experience = models.IntegerField()
    speciality = models.TextField()

    def __str__(self):
        return self.name

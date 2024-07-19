from django.db import models


class School(models.Model):
    School_Id:models.IntegerField
    school_name:models.CharField
   
class Class(models.Model):
    Class_Id:models.IntegerField
    Class_name:models.CharField

class Assessment_Areas(models.Model):
    Student_Id:models.IntegerField
    Fullname:models.IntegerField

class Student(models.Model):
    Student_Id:models.IntegerField
    Fullname:models.CharField

class Answers(models.Model):
    Id:models.IntegerField  
    Answers:models.CharField  

class Awards(models.Model):
    Id:models.IntegerField
    Name:models.CharField

class Subject(models.Model):
    Id:models.IntegerField
    Subject:models.CharField
    Subject_score:models.IntegerField    

class Summary(models.Model):
    School_Id:models.IntegerField
    Sydney_Participant:models.CharField
    Sydeney_Percentile:models.IntegerField
    Assessment_Area_Id:models.IntegerField
    Award_Id:models.IntegerField
    Class_Id:models.IntegerField
    Correct_answer_percentage_per_class:models.IntegerField
    Correct_Answer:models.CharField
    Student_Id:models.IntegerField
    Participant:models.CharField
    Student_score:models.IntegerField
    Subject_Id:models.IntegerField
    Category_Id:models.IntegerField
    Year_level_name:models.CharField
    Answer_Id:models.IntegerField
    Correct_answer_Id:models.IntegerField



# Create your models here.

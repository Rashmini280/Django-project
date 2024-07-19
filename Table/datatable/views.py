
# myapp/views.py
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
import pandas as pd
from .models import School, Class, Assessment_Areas, Student, Answers, Awards, Subject, Summary
from .serializers import SchoolSerializer, ClassSerializer, AssessmentAreaSerializer, StudentSerializer, AnswerSerializer, AwardSerializer, SubjectSerializer, SummarySerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class AssessmentAreaViewSet(viewsets.ModelViewSet):
    queryset = Assessment_Areas.objects.all()
    serializer_class = AssessmentAreaSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer

class AwardViewSet(viewsets.ModelViewSet):
    queryset = Awards.objects.all()
    serializer_class = AwardSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SummaryViewSet(viewsets.ModelViewSet):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer

class UploadCSV(APIView):
    def post(self, request, format=None):
        file = request.FILES['file']
        file_path = default_storage.save('Ganison_dataset_1.csv', file)
        file_path = default_storage.save('Ganison_dataset_2.csv', file)
        file_path = default_storage.save('Ganison_dataset_3.csv', file)
        file_path = default_storage.save('Ganison_dataset_4.csv', file)
        file_path = default_storage.save('Ganison_dataset_5.csv', file)
        file_path = default_storage.save('Ganison_dataset_6.csv', file)

        file_path = default_storage.path(file_path)
        
        data = pd.read_csv(file_path)
        
        for _, row in data.iterrows():
            # Map CSV columns to model fields here
            # Example for Student model
            student, created = Student.objects.get_or_create(
                student_id=row['Student_Id'],
                defaults={'fullname': row['Fullname']}
            )
            # Repeat the process for other models as needed
            
        return Response(status=status.HTTP_201_CREATED)

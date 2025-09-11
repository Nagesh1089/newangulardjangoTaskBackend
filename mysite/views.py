from django.http import JsonResponse
from students.models import Student

def student_list(request):
    students = Student.objects.all().values()  # fetch all rows
    return JsonResponse(list(students), safe=False)

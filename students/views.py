import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import StudentForm
from .models import Student
@csrf_exempt
# import sys
@csrf_exempt
def student_create(request):
    if request.method == "POST":
        try:
            # request.body is bytes, decode to string
            body_unicode = request.body.decode('utf-8')
            # convert JSON string to Python dict
            data = json.loads(body_unicode)
            student = Student.objects.create(
                name=data.get("name"),
                city=data.get("city"),
                address=data.get("address"),
                birth_date=data.get("birth_date"),
                is_active=data.get("is_active", True)
            )
            return JsonResponse({"message": "Student created", "id": student.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    # Return JSON even if method is not allowed
    return JsonResponse({"error": "Method not allowed"}, status=405)
@csrf_exempt
def student_update(request):
    if request.method == "PUT":
        try:
            student_id = request.GET.get("id")
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)

        try:
            # Decode JSON body
            body_unicode = request.body.decode('utf-8')
            data = json.loads(body_unicode)

            # Update only the fields provided
            if "name" in data:
                student.name = data["name"]
            if "city" in data:
                student.city = data["city"]
            if "address" in data:
                student.address = data["address"]
            if "birth_date" in data:
                student.birth_date = data["birth_date"]
            if "is_active" in data:
                student.is_active = data["is_active"]

            student.save()
            return JsonResponse({"message": "Student updated", "id": student.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    # Method not allowed
    return JsonResponse({"error": "Method not allowed", "method": request.method}, status=405)
@csrf_exempt
def delete_student(request):
    if request.method == "DELETE":
        student_id = request.GET.get("id")
        if not student_id:
            return JsonResponse({"error": "ID not provided"}, status=400)
        try:
            student = Student.objects.get(id=student_id)
            student.delete()
            return JsonResponse({"message": "Student deleted"})
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)
    return JsonResponse({"error": "Method not allowed"}, status=405)
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from main2.models import Student
from main2.models import Teacher
from api1.models import Pair


@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        students = [s.to_json() for s in students]
        return JsonResponse(students, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        student = Student(name=data['name'], created_by=User.objects.first())
        student.save();
        return JsonResponse(student.to_json())


@csrf_exempt
def student_detail(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        return JsonResponse(student.to_json())
    elif request.method == "PUT":
        data = json.loads(request.body)
        student.name = data.get('name', student.name)
        student.save()
        return JsonResponse(student.to_json())
    elif request.method == "DELETE":
        student.delete()
        return JsonResponse({'deleted': True}, status=204)


@csrf_exempt
def teacher_list(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        teachers = [t.to_json() for t in teachers]
        return JsonResponse(teachers, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        teacher = Teacher(name=data['name'], created_by=User.objects.first())
        teacher.save()
        return JsonResponse(teacher.to_json())


@csrf_exempt
def teacher_detail(request, pk):
    try:
        teacher = Teacher.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        return JsonResponse(teacher.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        teacher.name = data('name', teacher.name)
        teacher.surname = data('surname', teacher.surname)
        teacher.save()
        return JsonResponse(teacher.to_json())
    elif request.method == 'DELETE':
        teacher.delete()
        return JsonResponse({'deleted': True}, status=204)

@csrf_exempt
def pair_list(request):
    if request.method == 'GET':
        pairs = Pair.objects.all()
        pairs = [p.to_json() for p in pairs]
        return JsonResponse(pairs, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        pair = Pair(name=data['name'], created_by=User.objects.first())
        pair.save()
        return JsonResponse(pair.to_json())

from django.shortcuts import render

from app.models import Student



def home(request):
    students=Student.objects.filter(paid_students=False).order_by('-updated_at')
    paid_students=Student.objects.filter(paid_students=True)
    context={
        'students':students,
        'paid_students':paid_students
    }
    return render(request,'home.html',context)
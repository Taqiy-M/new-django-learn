from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# Create your views here.


# def home(request):
#     return HttpResponse("Salom ZED!!")

def salom(request):
    return render(request, "index.html")

def all_students(request):
    # if request.method == 'GET':
    if request.method == 'POST':
        Student.objects.create(
            ism=request.POST.get('name'),
            st_raqam=request.POST.get('st_raqam'),
            kitoblar_soni=request.POST.get('kitoblar_soni')
        )
        return redirect('/all-students/')

    c = Student.objects.all()
    a = {'students': c}
    return render(request, "talaba.html", a)

def single_student(request, a):
    student = Student.objects.get(id=a)
    data = {'student': student}
    return render(request, 'students.html', data)

def all_books(request):
    if request.method == 'POST':
        m_id = request.POST.get('muallif')
        muallif = Yozuvchi.objects.get(id=m_id)

        Kitob.objects.create(
            nom=request.POST.get('nom'),
            sahifa=request.POST.get('sahifa'),
            yil=request.POST.get('yil'),
            janr=request.POST.get('janr'),
            yozuvchi=muallif
        )
        return redirect('/all-books/')
    c = Kitob.objects.all()
    m = Yozuvchi.objects.all()
    a = {
        'books': c,
        'authors': m
         }
    return render(request, "kitoblar.html", a)



def delete_book(request, a):
    Kitob.objects.get(id=a).delete()
    return redirect('/all-books/')

def book_update(request, a):
    m_id = request.POST.get('muallif')
    muallif = Yozuvchi.objects.get(id=m_id)

    if request.method == "POST":
        Kitob.objects.filter(id=a).update(
            nom=request.POST.get('nom'),
            sahifa=request.POST.get('sahifa'),
            yil=request.POST.get('yil'),
            janr=request.POST.get('janr'),
            yozuvchi=muallif
        )
        return redirect('/all-books/')
    data = {
        'authors': Yozuvchi.objects.all(),
        'book': Kitob.objects.get(id=a)
    }
    return render(request, 'book_update.html', data)


def hello_world(request):
    print("Hello world!!")
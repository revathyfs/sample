from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors,Booking
from .form import BookingForm

# create your vies here.
def index(request):
    # person ={
    #     'name' : 'Revathy',
    #     'age' : 20,
    #     'place' : 'Kollam'
    # }

    # if condition
    # numbers = {
    #     'num' : 10,
    # }

    # loop
    # numbers = {
    #     'num' : [1,2,3,4,5,6,7,8,9,10]
    # }

    return render(request,'index.html',)

def about(request):
    return render(request,'about.html')

def doctors(request):
    doct={
        'doc': Doctors.objects.all()    
    }
    return render(request,'doctors.html',doct)

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
        # You can redirect or render a success message here
    form = BookingForm()
    form_dic={
        'form': form,
    }
    return render(request,'booking.html',form_dic)

def department(request):
    dept={
        'dep': Departments.objects.all()    
    }
    
    return render(request,'department.html',dept)

def contact(request):
    return render(request,'contact.html')


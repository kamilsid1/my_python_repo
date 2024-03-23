from django.shortcuts import render

# Create your views here.

def home(request, id):
    data={
        'data1':id
    }
    return render(request, 'home.html', {'key':data})
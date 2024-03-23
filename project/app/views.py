from django.shortcuts import render

# Create your views here.

# def home(request, id):
#     data={
#         'data1':id
#     }
#     return render(request, 'home.html', {'key':data})


def home(request, ab, pk, pkid, abid):
    data = {
        'data1': ab,
        'data2': pk,
        'data3': pkid,
        'data4': abid
    }
    return render(request, 'home.html', data)
from django.shortcuts import render
from core.startpage.models import Person

def viewData(request):
    data={
        'persons':Person.objects.filter(peticiones="1")
    }
    return render(request,'report_users.html',data)


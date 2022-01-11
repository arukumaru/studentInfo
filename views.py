from django.http import HttpResponse
from .models import StudentInfo
from .models import StudentAcademics


def index(request):
    all_studentinfo = StudentInfo.objects.all()
    html = ''
    for studentinfo in all_studentinfo:
        url = '/academics/' + str(studentinfo.Roll_no)
        html += '<a href=" ' + url +' ">' + studentinfo.Name + '</a><br>'

    return HttpResponse(html)


def detail(request, Roll_no):
    return HttpResponse("<h2>Details for Roll_No: " + str(Roll_no) + "</h2>")

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from employeeapp.models import EmployeeDetail
from .fusioncharts import FusionCharts
import openpyxl
import xlrd


def main(request):
    return render(request, 'main.html')


def add(request):
    if request.method == 'GET':
        return render(request, 'add.html')

    elif request.method == 'POST':
        id = request.POST.get("id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        contactno = request.POST.get("contactno")
        employee = EmployeeDetail(
            id=id, name=name, email=email, contactno=contactno)
        employee.save()
        return redirect("/add")


def show(request):
    data = {}
    emplist = EmployeeDetail.objects.all()
    return render(request, 'show.html', context={'emplist': emplist})


def edit(request, id):
    if request.method == 'GET':
        employee = EmployeeDetail.objects.get(id=id)
        show = {
            "id": employee.id,
            "name": employee.name,
            "email": employee.email,
            "contactno": employee.contactno}
        return render(request, 'edit.html', context=show)

    elif request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        contactno = request.POST.get("contactno")
        employee = EmployeeDetail.objects.get(id=id)
        employee.name = name
        employee.email = email
        employee.contactno = contactno
        employee.save()
        return redirect("/show")


def delete(request, id):
    employee = EmployeeDetail.objects.get(id=id)
    employee.delete()
    return redirect("/show")


def search(request):
    data = {}
    if request.method == 'GET':
        return render(request, 'search.html')
    elif request.method == 'POST':
        name = request.POST.get("searchedData")
        emplist = EmployeeDetail.objects.filter(name__iregex=name)
        return render(request, 'search.html', context={'emplist': emplist})

def upload(request):

    if "GET" == request.method:
        return render(request, 'upload.html', {})
    else:
        excel_file = request.FILES['excel_file']
        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb["Sheet1"]
        excel_data = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
            emplist = EmployeeDetail(
                id=row_data[0], name=row_data[1], email=row_data[2], contactno=row_data[3])
            emplist.save()
        emplist = EmployeeDetail.objects.all()

        return render(request, 'show.html', context={'emplist': emplist})

def chart(request):
   chartObj = FusionCharts( 'column3d', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Most used Social Media",
    "subcaption": "For the year 2019",
    "yaxisname": "No of users in million",
    "decimals": "1",
    "theme": "fusion"
  },
  "data": [
    {
      "label": "Facebook",
      "value": "9.36"
    },
    {
      "label": "Instagram",
      "value": "8.3"
    },
    {
      "label": "Twitter",
      "value": "5.8"
    },
    {
      "label": "TikTok",
      "value": "6.9"
    },
    {
      "label": "You Tube",
      "value": "7.9"
    },
    {
      "label": "LinkedIn",
      "value": "5.8"
    },
    {
      "label": "Pinterest",
      "value": "4.6"
    },
    {
      "label": "Google+",
      "value": "8.9"
    },
  
  ]
}""")
   return render(request, 'chart.html', {'output': chartObj.render()})


from django.shortcuts import render

from django.shortcuts import render
from .models import Department, Position, Employee, Project, ProjectExecution


def list_tables(request):
    data = {
        "departments": Department.objects.all(),
        "positions": Position.objects.all(),
        "employees": Employee.objects.all(),
        "projects": Project.objects.all(),
        "executions": ProjectExecution.objects.all(),
    }
    return render(request, "list_tables.html", data)

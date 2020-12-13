from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Company, BillingInfo, User, Project, Task, Tag
from .serializers import CompanySerializer, BillingInfoSerializer, UserSerializer, ProjectSerializer, TaskSerializer, TagSerializer

@api_view(['GET', 'POST'])
def companies(request):
    #buscar lista de empresas
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    #añadir una empresa a la lista
    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def company(request, pk):
    #buscar la empresa en la base de datos
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) #no existe

    #recuperar una empresa
    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #modificar una empresa
    elif request.method == 'PUT':
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    #borrar una empresa
    elif request.method == 'DELETE':
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def billinginfolist(request):
    #buscar lista de info de facturación
    if request.method == 'GET':
        billingInfoList = BillingInfo.objects.all()
        serializer = BillingInfoSerializer(billingInfoList, many=True)
        return Response(serializer.data)
    #añadir un elemento info de facturación a la lista
    elif request.method == 'POST':
        serializer = BillingInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def billinginfo(request, pk):
    #buscar la info de facturación en la base de datos
    try:
        billingInfo = BillingInfo.objects.get(pk=pk)
    except BillingInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) #no existe

    #recuperar una info de facturación
    if request.method == 'GET':
        serializer = BillingInfoSerializer(billingInfo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #modificar una info de facturación
    elif request.method == 'PUT':
        serializer = BillingInfoSerializer(billingInfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    #borrar una info de facturación
    elif request.method == 'DELETE':
        billingInfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def users(request):
    #buscar lista de usuarios
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    #añadir un usuario a la lista
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user(request, pk):
    #buscar el usuario en la base de datos
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) #no existe

    #recuperar un usuario
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #modificar un usuario
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    #borrar un usuario
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def projects(request):
    #buscar lista de proyectos
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    #añadir un proyecto a la lista
    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def project(request, pk):
    #buscar el proyecto en la base de datos
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) #no existe

    #recuperar un proyecto
    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #modificar un proyecto
    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    #borrar un proyecto
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def tasks(request):
    #buscar lista de tareas
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    #añadir una tarea a la lista
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            #Restricción: crear tarea si el usuario pertenece al proyecto
            if userBelongsProject(serializer):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data, status=status.HTTP_412_PRECONDITION_FAILED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def task(request, pk):
    #buscar la tarea en la base de datos
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) #no existe

    #recuperar una tarea
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #modificar una tarea
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            #Restricción: crear tarea si el usuario pertenece al proyecto
            if userBelongsProject(serializer):
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                serializer.save()
            else:
                return Response(serializer.data, status=status.HTTP_412_PRECONDITION_FAILED)
    #borrar una tarea
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def tags(request):
    #buscar lista de etiquetas
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    #añadir una etiqueta a la lista
    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tag(request, pk):
    #buscar la etiqueta en la base de datos
    try:
        tag = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) #no existe

    #recuperar una etiqueta
    if request.method == 'GET':
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #modificar una etiqueta
    elif request.method == 'PUT':
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    #borrar una etiqueta
    elif request.method == 'DELETE':
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
@Param: Request 
Ejemplo:
{
	"title" : "task1",
	"description" : "task1",
	"due_date" : "2020-12-31",
	"user" : "1",
	"project" : "2"
}
@Return: True si el usuario pertenece al proyecto
'''
def userBelongsProject(serializer):
    #obtener usuario del JSON de entrada
    inputUser = serializer.validated_data.get('user')
    #obtener proyecto del JSON de entrada
    inputProject = serializer.validated_data.get('project')
    #obtener proyecto de base de datos
    project = Project.objects.get(pk=inputProject.id)
    #obtener usuarios del proyecto
    usersInProject = project.user.all()
    if inputUser in usersInProject:
        return True
    else:
        return False

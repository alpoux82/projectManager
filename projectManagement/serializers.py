from rest_framework import serializers
from .models import Company, BillingInfo, User, Project, Task, Tag

class CompanySerializer(serializers.ModelSerializer):
    #mostrar información de facturación según función __str__
    billingInfo = serializers.StringRelatedField(many=False)
    class Meta:
        model = Company
        fields = ['id', 'name', 'billingInfo']

class BillingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingInfo
        fields = ['id', 'cif', 'zipCode', 'country', 'ccc', 'company']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'company']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'code', 'name', 'user']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'user', 'project']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'task']
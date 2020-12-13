from django.db import models

class Company(models.Model):

    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'company'
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class BillingInfo(models.Model):
    
    cif = models.CharField(max_length=20)
    zipCode = models.IntegerField(default=0)
    country = models.CharField(max_length=20)
    ccc = models.IntegerField(default=0)
    #Una empresa tiene una información de facturación y una información de facturación se refiere a una empresa
    company = models.OneToOneField(Company, related_name='billingInfo', on_delete = models.CASCADE)

    class Meta:
        db_table = 'billing_info'
        ordering = ['cif']

    def __str__(self):
        """String for representing the Model object."""
        return self.cif    

class User(models.Model):
    
    name = models.CharField(max_length=100)
    #Un usuario pertenece a una empresa y una empresa puede tener muchos usuarios
    company = models.ForeignKey(Company, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'user'
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name 

class Project(models.Model):
    
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    #Un usuario puede tener múltiples proyectos y un proyecto puede tener múltiples usuarios
    user = models.ManyToManyField(User)

    class Meta:
        db_table = 'project'
        ordering = ['code']

    def __str__(self):
        """String for representing the Model object."""
        return self.code 

class Task(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    due_date = models.DateField()
    #Una tarea está asociada a un usario y un usuario puede tener múltiples tareas
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    #Una tarea pertenece a un solo proyecto y un proyecto puede tener múltiples tareas
    project = models.ForeignKey(Project, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'task'
        ordering = ['title']

    def __str__(self):
        """String for representing the Model object."""
        return self.title 

class Tag(models.Model):
    
    name = models.CharField(max_length=100)
    #Una tarea puede tener múltiples etiquetas y una etiqueta múltiples tareas
    task = models.ManyToManyField(Task)

    class Meta:
        db_table = 'tag'
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name 
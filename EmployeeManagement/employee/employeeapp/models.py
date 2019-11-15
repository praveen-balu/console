from django.db import models
# Create your models here.

class EmployeeDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    contactno = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)

    class Meta:
        db_table = "EmployeeManagement"


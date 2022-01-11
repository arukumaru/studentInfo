from django.db import models


class StudentInfo(models.Model):
    Roll_no = models.CharField(primary_key=True, max_length=250)
    Name = models.CharField(max_length=250)
    Class = models.CharField(max_length=250)
    School = models.CharField(max_length=250)
    Mobile = models.CharField(max_length=250)
    Address = models.CharField(max_length=250)

    def __str__(self):
        return self.Name + ' _ ' + self.Class


class StudentAcademics(models.Model):
    Roll_no = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    Maths = models.CharField(max_length=250)
    Physics = models.CharField(max_length=250)
    Chemistry = models.CharField(max_length=250)
    Biology = models.CharField(max_length=250)
    English = models.CharField(max_length=250)

    def __str__(self):
        return self.Maths




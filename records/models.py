from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=200)
    pid = models.IntegerField(max_length=15)
    date_of_birth = models.DateField()
    medical_history = models.TextField()
    presentation_date = models.DateField()
    presentation = models.TextField()

    def __str__(self):
        return self.name


class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_date = models.DateField()
    visit_note = models.TextField()
    visit_image = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.visit_date)
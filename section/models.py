from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name + ": " + str(self.sid)

    def __unicode__(self):
        return self.name + ": " + str(self.sid)


class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Section(models.Model):
    date = models.CharField(max_length=255)
    capacity = models.IntegerField(default=25)
    place = models.CharField(max_length=255)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.date + " - " + self.place

    def __unicode__(self):
        return self.date + " - " + self.place

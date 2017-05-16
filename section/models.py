from __future__ import unicode_literals

from django.db import models


class Client(models.Model):
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
    available = models.IntegerField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.date + " - " + self.place

    def __unicode__(self):
        return self.date + " - " + self.place


class Reg(models.Model):
    section_id = models.ForeignKey('Section', on_delete=models.CASCADE)
    sid = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sid) + ": " + str(self.section_id)

    def __unicode__(self):
        return str(self.sid) + ": " + str(self.section_id)
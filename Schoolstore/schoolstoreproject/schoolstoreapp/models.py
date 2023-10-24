from django.db import models

# Create your models here.

class Department(models.Model):
    dname=models.CharField(unique=True,max_length=200)
    slug=models.SlugField(max_length=200,unique=True)

    def __str__(self):
        return self.dname





class Course(models.Model):
    cname=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    category=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.cname

class Box(models.Model):
    bname=models.CharField(max_length=200)
    bimg=models.ImageField(upload_to="pics")
    bdesc=models.TextField()

    def __str__(self):
        return self.bname


class Testimonial(models.Model):
    tname=models.CharField(max_length=200)
    timg=models.ImageField(upload_to="pics2")
    tdesc=models.TextField()

    def __str__(self):
        return self.tname



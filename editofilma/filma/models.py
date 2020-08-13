from django.db import models



class Network(models.Model):
    id=models.AutoField(primary_key=True)
    network_name=models.CharField(max_length=255)
    network_pic=models.FileField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()


class Genre(models.Model):
    id=models.AutoField(primary_key=True)
    genre_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class Filma(models.Model):
    id=models.AutoField(primary_key=True)
    movie_name=models.CharField(max_length=255)
    profile_pic=models.FileField()
    network_id=models.ForeignKey(Network,on_delete=models.SET_NULL,null=True)
    genre_id=models.ForeignKey(Genre,on_delete=models.SET_NULL,null=True)
    describe=models.TextField()
    imdb=models.FloatField()
    data=models.DateField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()



   
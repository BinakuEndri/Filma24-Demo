from django import forms
from django.forms import ChoiceField

from filma.models import Filma , Network , Genre


class ChoiceNoValidation(ChoiceField):
    def validate(self, value):
        pass

class DateInput(forms.DateInput):
    input_type = "date"

class AddMovieForm(forms.Form):
    
    movie_name=forms.CharField(label="Emri",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

    network_list=[]
    try:
        networks=Network.objects.all()
        for network in networks:
            small_network=(network.id,network.network_name)
            network_list.append(small_network)
    except:
        network_list=[]
    
    genre_list=[]
    try:
        genres=Genre.objects.all()
        for genre in genres:
            small_genre=(genre.id,genre.genre_name)
            genre_list.append(small_genre)
    except:
        genre_list=[]
    
    genre=forms.ChoiceField(label="Zhandrri",choices=genre_list,widget=forms.Select(attrs={"class":"form-control"}))
    network=forms.ChoiceField(label="Platforma",choices=network_list,widget=forms.Select(attrs={"class":"form-control"}))
    describe=forms.CharField(label="Pershkrimi",max_length=255,widget=forms.Textarea(attrs={"class":"form-control"}))
    data = forms.DateField(label="Data",widget=DateInput(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))

class EditMovieForm(forms.Form):
    
    movie_name=forms.CharField(label="Emri",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)


    network_list=[]
    try:
        networks=Network.objects.all()
        for network in networks:
            small_network=(network.id,network.network_name)
            network_list.append(small_network)
    except:
        network_list=[]
    
    genre_list=[]
    try:
        genres=Genre.objects.all()
        for genre in genres:
            small_genre=(genre.id,genre.genre_name)
            genre_list.append(small_genre)
    except:
        genre_list=[]
        
    genre=forms.ChoiceField(label="Zhandrri",choices=genre_list,widget=forms.Select(attrs={"class":"form-control"}))
    network=forms.ChoiceField(label="Platforma",choices=network_list,widget=forms.Select(attrs={"class":"form-control"}))
    describe=forms.CharField(label="Pershkrimi",max_length=255,widget=forms.Textarea(attrs={"class":"form-control"}),required=False)
    data = forms.DateField(label="Data",widget=DateInput(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
    



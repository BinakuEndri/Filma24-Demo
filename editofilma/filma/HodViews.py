import json

import requests
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from filma.models import Network, Genre, Filma
from filma.forms import AddMovieForm, EditMovieForm


def home(request):

    filma_count=Filma.objects.all().count()
    network_count=Network.objects.all().count()
    genre_count=Genre.objects.all().count()

    network_all=Network.objects.all()
    genre_all=Genre.objects.all()

    movies=Filma.objects.all()

    network_name_list=[]
    movie_network_list=[]

    for network in network_all:
        filma=Filma.objects.filter(network_id=network.id).count()
        network_name_list.append(network.network_name)
        movie_network_list.append(filma)

    genre_name_list=[]
    movie_genre_list=[]
    for genre in genre_all:
        filma_n=Filma.objects.filter(genre_id=genre.id).count()
        genre_name_list.append(genre.genre_name)
        movie_genre_list.append(filma_n)






    return render(request, "hod_template/home_content.html",{"filma_count":filma_count,"network_count":network_count,"genre_count":genre_count,"movie_network_list":movie_network_list,"network_name_list":network_name_list,"movie_genre_list":movie_genre_list,"genre_name_list":genre_name_list,"movies":movies})


def add_genre(request):
    return render(request, "hod_template/add_genre_template.html")


def add_genre_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        genre = request.POST.get("genre")
        try:
            genre_model = Genre(genre_name=genre)
            genre_model.save()
            messages.success(request, "Successfully Added genre")
            return HttpResponseRedirect(reverse("add_genre"))
        except:
            messages.error(request, "Failed To Add genre")
            return HttpResponseRedirect(reverse("add_genre"))


def add_network(request):
    return render(request, "hod_template/add_network_template.html")


def add_network_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        network = request.POST.get("network")
        try:
            network_model = Network(network_name=network)
            network_model.save()
            messages.success(request, "Successfully Added network")
            return HttpResponseRedirect(reverse("add_network"))
        except:
            messages.error(request, "Failed To Add network")
            return HttpResponseRedirect(reverse("add_network"))


def add_movie(request):
    form = AddMovieForm()
    return render(request, "hod_template/add_movie_template.html", {"form": form})


def add_movie_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:

        form = AddMovieForm(request.POST, request.FILES)

        
        if form.is_valid():
            movie_name = form.cleaned_data["movie_name"]
            genre_id = form.cleaned_data["genre"]
            network_id = form.cleaned_data["network"]
            describe_id = form.cleaned_data["describe"]
            data_id = form.cleaned_data["data"]

            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
            try:
                movie = Filma(movie_name=movie_name,describe=describe_id, data=data_id)
                
                movie.profile_pic=profile_pic_url

                genre_obj = Genre.objects.get(id=genre_id)
                movie.genre_id = genre_obj
                network_obj = Network.objects.get(id=network_id)
                movie.network_id = network_obj

                
                movie.save()

                messages.success(request, "Successfully Added Movie")
                return HttpResponseRedirect(reverse("add_movie"))
            except:
              messages.error(request,"Failed to Add movie")
              return HttpResponseRedirect(reverse("add_movie"))
        else:
            form = AddMovieForm(request.POST)
            return render(request, "hod_template/add_movie_template.html", {"form": form})


def manage_genre(request):
    genres = Genre.objects.all()
    return render(request, "hod_template/manage_genre_template.html", {"genres": genres})


def manage_network(request):
    networks = Network.objects.all()
    return render(request, "hod_template/manage_network_template.html", {"networks": networks})


def manage_movie(request):
    movies = Filma.objects.all()
    return render(request, "hod_template/manage_movie_template.html", {"movies": movies})


def edit_movie(request, movie_id):
    request.session['movie_id'] = movie_id
    movie = Filma.objects.get(id=movie_id)
    form = EditMovieForm()
    form.fields['movie_name'].initial = movie.movie_name
    form.fields['genre'].initial = movie.movie_name
    form.fields['network'].initial = movie.movie_name
    form.fields['describe'].initial = movie.describe
    form.fields['data'].initial = movie.data
    return render(request, "hod_template/edit_movie_template.html", {"form": form, "id": movie_id, "movie_name": movie.movie_name})


def edit_movie_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")

    else:
        movie_id = request.session.get("movie_id")
        if movie_id == None:
            return HttpResponseRedirect(reverse("manage_movie"))
        form = EditMovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie_name = form.cleaned_data["movie_name"]
            genre_id = form.cleaned_data["genre"]
            network_id = form.cleaned_data["network"]
            describe_id = form.cleaned_data["describe"]
            data_id = form.cleaned_data["data"]

            if request.FILES.get('profile_pic', False):
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None

            try:
                movie = Filma.objects.get(id=movie_id)
                movie.movie_name = movie_name
                movie.describe = describe_id
                movie.data = data_id
                network = Network.objects.get(id=network_id)
                movie.network_id = network
                genre = Genre.objects.get(id=genre_id)
                movie.genre_id = genre
                if profile_pic_url != None:
                    movie.profile_pic = profile_pic_url
                movie.save()
                del request.session['movie_id']
                messages.success(request, "Successfully Edited movie")
                return HttpResponseRedirect(reverse("edit_movie", kwargs={"movie_id": movie_id}))
            except:
                messages.error(request, "Failed to Edit movie")
                return HttpResponseRedirect(reverse("edit_movie", kwargs={"movie_id": movie_id}))
        else:
            form = EditMovieForm(request.POST)
            movie = Filma.objects.get(id=movie_id)
            return render(request, "hod_template/edit_movie_template.html", {"form": form, "id": movie_id, "movie_name": movie.movie_name})


def edit_genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    return render(request, "hod_template/edit_genre_template.html", {"genre": genre, "id": genre_id})


def edit_genre_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        genre_id = request.POST.get("genre_id")
        genre_name = request.POST.get("genre")

        try:
            genre = Genre.objects.get(id=genre_id)
            genre.genre_name = genre_name
            genre.save()
            messages.success(request, "Successfully Edited genre")
            return HttpResponseRedirect(reverse("edit_genre", kwargs={"genre_id": genre_id}))
        except:
            messages.error(request, "Failed to Edit genre")
            return HttpResponseRedirect(reverse("edit_genre", kwargs={"genre_id": genre_id}))


def edit_network(request, network_id):
    network = Network.objects.get(id=network_id)
    return render(request, "hod_template/edit_network_template.html", {"network": network, "id": network_id})


def edit_network_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        network_id = request.POST.get("network_id")
        network_name = request.POST.get("network")

        try:
            network = Network.objects.get(id=network_id)
            network.network_name = network_name
            network.save()
            messages.success(request, "Successfully Edited genre")
            return HttpResponseRedirect(reverse("edit_network", kwargs={"network_id": network_id}))
        except:
            messages.error(request, "Failed to Edit genre")
            return HttpResponseRedirect(reverse("edit_network", kwargs={"network_id": network_id}))


def delete_movie(request, movie_id):

    movies = Filma.objects.all()
    movie = Filma.objects.get(id=movie_id)

    movie.delete()
    return render(request, "hod_template/manage_movie_template.html", {"movies": movies})


def delete_genre(request, genre_id):

    genres = Genre.objects.all()
    genre = Genre.objects.get(id=genre_id)

    genre.delete()
    return render(request, "hod_template/manage_genre_template.html", {"genres": genres})


def delete_network(request,network_id):

    networks = Network.objects.all()
    network = Network.objects.get(id=network_id)

    network.delete()
    return render(request, "hod_template/manage_network_template.html", {"networks": networks})

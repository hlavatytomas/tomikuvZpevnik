"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pisnicky import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import render

# import sys
# sys.path.append("..")
# from SongBook import SongBook

# songsDir = '../songs/'
# songBookTex = 'Songbook'

# # create song book
# songBook = SongBook(songsDir,songBookTex)

urlpatterns = [
    path('docs/index.html', views.home, name='home'),    # added
    path('docs/addSong.html', views.addSong, name='addSong'),    # added
    path('docs/editSong.html', views.editSong, name='editSong'),    # added
    path('docs/handleEdit.html', views.handleEdit, name='handleEdit'),    # added
    path('docs/song.html', views.song, name='song'),    # added
    # path('docs/songs/1970.html', views.p1970, name='p1970'),    # added
]
# for i in range(len(songBook.songsLst)):
#     urlpatterns.append(path('docs/songs/%s.html'%songBook.songsLst, render('1970.html'), name='home'))

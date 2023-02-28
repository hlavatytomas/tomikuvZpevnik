from django.shortcuts import render
from django.http import HttpResponseRedirect   # added

from .forms import *


import sys
sys.path.append("..")
from SongBook import SongBook
from pathlib import Path,PurePosixPath
import pandas as pd
import os

def home(request):
    return render(request, 'index.html')

def handleEdit(request):
	if request.method == 'GET':
		form = SongNameForm(request.GET)
		if not (len(form.data)) == 0:
			whtChanges = []
			formsToEdit = request.session.get('formsToEdit')
			for i in range(len(formsToEdit)):
				if form.data[formsToEdit[i]] != request.session.get(formsToEdit[i]):
					whtChanges.append(i)
			
			if len(whtChanges) > 0:
				name = request.session.get('name')
				songsDir = '../songs/'
				songBookDb = pd.read_csv(Path(songsDir).joinpath("00_songdb.csv"),encoding="utf-8") 
				for chI in whtChanges:
					if chI == 0:
						request.session['name'] = form.data[formsToEdit[chI]] 
					songBookDb.loc[songBookDb.query('name == @name').index, formsToEdit[chI]] = form.data[formsToEdit[chI]]
			
				songBookDb.to_csv(Path(songsDir).joinpath("00_songdb.csv"),encoding="utf-8",index=False)
			
			songsDir = '../songs/'
			songBookTex = 'Songbook'
			songBook = SongBook(songsDir,songBookTex)
			songBook.loadSongs()
			songBook.createHTML('../docs')
			songBook.createHTMLForDjango('./docs',sngDir='../')
			form.full_clean()
			if 0 in whtChanges:
				return HttpResponseRedirect('./index.html')
			else:
				return HttpResponseRedirect('./handleEdit.html')
		else:
			return HttpResponseRedirect('./songs/%s.html'%request.session.get('name'))

	# return render(request, 'addSong.html', {'form': form})

def editSong(request):
    # if this is a POST request we need to process the form data
	if request.method == 'GET':
		form = NameForm(request.GET)
		name = (form.data['song'])
		songsDir = '../songs/'
		songBookDb = pd.read_csv(Path(songsDir).joinpath("00_songdb.csv"),encoding="utf-8") 
		infoSong = (songBookDb.query("name == @name").iloc[0])
		formsToEdit = ['name', 'author', 'capo', 'owner']
		songForm = SongNameForm(initial={	
									formsToEdit[0]: infoSong['name'], 
									formsToEdit[1]: infoSong['author'],
									formsToEdit[2]: infoSong['capo'],
									formsToEdit[3]: infoSong['owner'],
								})
		for i in range(len(formsToEdit)):
			request.session[formsToEdit[i]] = str(infoSong[i])
		request.session['formsToEdit'] = formsToEdit
	else:
		songForm = SongNameForm()

	# return render(request, 'addSong.html', {'form': form})
	return render(request, 'editSong.html', {'songForm': songForm})

def addSong(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			songsDir = '../songs/'
			songBookTex = 'Songbook'

			# create song book
			songBook = SongBook(songsDir,songBookTex)
			name = songBook.addSong(runFromWeb=True, pageStrW=form.cleaned_data['your_name'])
			songBook.loadSongs()
			songBook.createHTML('../docs')
			songBook.createHTMLForDjango('./docs')
			return HttpResponseRedirect('editSong.html?song=%s'%name)
	# if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()

	return render(request, 'addSong.html', {'form': form})

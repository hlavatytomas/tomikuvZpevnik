from django.shortcuts import render
from django.http import HttpResponseRedirect   # added

from .forms import *


import sys
sys.path.append("..")
from SongBook import SongBook

def home(request):
    return render(request, 'index.html')

def handleEdit(request):
	if request.method == 'GET':
		form = SongNameForm(request.GET)
		if not (len(form.data)) == 0:
			atributes = ['songName','author', 'capo', 'transpose','owner']
			songsDir = '../songs/'
			songBookTex = 'Songbook'
			songBook = SongBook(songsDir,songBookTex)

			initials = request.session.get('initials')

			request.session['name'] = form.data['songName']

			replaces = []
			for i in range(len(atributes)):
				if initials[i] != form.data[atributes[i]]:
					# print(atributes[i], form.data[atributes[i]])
					replaces.append([atributes[i], form.data[atributes[i]]])

			songBook.changeInSong(initials[0], replaces)
			songBook.loadSongs()
			songBook.createHTML('../docs')
			songBook.createHTMLForDjango('./docs')
			form.full_clean()
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
		songBookTex = 'Songbook'
		songBook = SongBook(songsDir,songBookTex)
		s, i, c, t, o = songBook.infoAboutSong(name)
		songForm = SongNameForm(initial={	
									'songName': s, 
									'author': i,
									'capo': c,
									'transpose': t,
									'owner': o,
								})
		request.session['initials'] = [s, i, c, t, o]
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

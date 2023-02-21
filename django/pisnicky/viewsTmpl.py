from django.shortcuts import render
from django.http import HttpResponseRedirect   # added

from .forms import NameForm

import sys
sys.path.append("..")
from SongBook import SongBook

def home(request):
    return render(request, 'index.html')

def editSong(request):
    return render(request, 'editSong.html')

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
			songBook.addSong(runFromWeb=True, pageStrW=form.cleaned_data['your_name'])
			songBook.loadSongs()
			songBook.createHTML('../docs')
			songBook.createHTMLForDjango('./docs')
			return HttpResponseRedirect('addSong.html')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()

	return render(request, 'addSong.html', {'form': form})

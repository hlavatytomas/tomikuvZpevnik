from django.shortcuts import render
from django.http import HttpResponseRedirect   # added

from .forms import *


import sys
sys.path.append("..")
from SongBook import SongBook
from pathlib import Path
import pandas as pd
import os
import re
from django.http import HttpResponse
from django.template import loader

def home(request):
	template = loader.get_template('index.html')
	songsDir = '../songs/'
	songBookDb = pd.read_csv(Path(songsDir).joinpath("00_songdb.csv"),encoding="utf-8")
	songs = ''
	for _,row in songBookDb.iterrows():
		songName = row["name"]
		songOwner = row["owner"]
		songs += (f'<div class="song_item" owner="{songOwner}"><a href="./song.html?song={songName}"><div class="song_ref"><span class="song_name">{re.sub("_"," ",songName)}</span><span class="owner">{songOwner}</span></div></a></div>\n')
	context = {
		'songs': songs,
	}
	return HttpResponse(template.render(context, request))

def handleEdit(request):
	if request.method == 'GET':
		form = SongNameForm(request.GET)
		if not (len(form.data)) == 0:
			whtChanges = []
			formsToEdit = request.session.get('formsToEdit')
			for i in range(len(formsToEdit)-1):
				if form.data[formsToEdit[i]].replace(' ','_') != request.session.get(formsToEdit[i]):
					whtChanges.append(i)
			
			text = form.data['text']

			text = re.sub(r'beginsong{.*}\[by={.*}\]', 'beginsong{%s}[by={%s}]' % (form.data['name'], form.data['author']), text)

			text = re.sub(r'\\capo{([^}]*)}', r'', text)

			print(text)

			if form.data['capo'] != '0':
				text = re.sub(r'}]', '}]\\capo{%s}' % (form.data['capo']), text)

			# text = re.sub(r'\\capo{([^}]*)}', r'\\capo{%s}' % form.data['capo'], text)

			if text != request.session.get('text'):
				with open('../' + request.session.get('path'),"w", encoding='utf-8') as tex:
					tex.write(text)

			if len(whtChanges) > 0:
				name = request.session.get('name')
				songsDir = '../songs/'
				songBookTex = 'Songbook'
				songBook = SongBook(songsDir,songBookTex)
				songBookDb = songBook.songsLst 
				songIndex = songBookDb.query('name == @name').index
				print(songIndex)
				for chI in whtChanges:
					if chI == 0:
						request.session['name'] = form.data[formsToEdit[chI]].replace(' ','_')
						songBookDb.loc[songIndex, formsToEdit[chI]] = form.data[formsToEdit[chI]].replace(' ','_') 
						name = form.data[formsToEdit[chI]].replace(' ','_')
					if 'owner' in formsToEdit[chI] or chI == 0:
						if not form.data['owner'] == 'T':
							ownFL = [fL[0] for fL in songBook.owners]
							ownInd = ownFL.index(form.data['owner'])
							pathNew = 'songs/' + 'ŽŽ_%sSongs/%s.tex' % (songBook.owners[ownInd], name)
						else:
							pathNew = 'songs/' + '%s.tex' % (name)
						pathOld = songBookDb.loc[songIndex,'path'].iloc[0]
						print(pathOld)
						os.system(f'mv ../{pathOld} ../%s' % (pathNew))
						songBookDb.loc[songIndex,'path'] = pathNew
					if not chI == 0:
						songBookDb.loc[songIndex,formsToEdit[chI]] = form.data[formsToEdit[chI]]
			
				songBookDb.to_csv(Path(songsDir).joinpath("00_songdb.csv"),encoding="utf-8",index=False)

				songBook.loadSongs()
				songBook.saveDB()
				# songBook.createHTML('../docs')
				# songBook.createHTMLForDjango('./docs',sngDir='../')
			form.full_clean()
			# return HttpResponseRedirect('./songs/%s.html'%request.session.get('name'))
			return HttpResponseRedirect('./handleEdit.html')
		else:
			return HttpResponseRedirect('./song.html?song=%s'%request.session.get('name'))

	# return render(request, 'addSong.html', {'form': form})

def editSong(request):
    # if this is a POST request we need to process the form data
	if request.method == 'GET':
		form = NameForm(request.GET)
		name = (form.data['song'])
		songsDir = '../songs/'
		songBookDb = pd.read_csv(Path(songsDir).joinpath("00_songdb.csv"),encoding="utf-8") 
		formsToEdit = ['name', 'author', 'capo', 'owner','path']
		infoSong = songBookDb.query("name == @name").iloc[0][formsToEdit]
		with open('../' + infoSong['path'],"r", encoding='utf-8') as tex:
			content=tex.read()
		# content = re.search(r'\\transpose{([^}]*)}',content)
		textOfSong = content
		# print(infoSong)
		songForm = SongNameForm(initial={	
									formsToEdit[0]: infoSong[formsToEdit[0]].replace('_',' '), 
									formsToEdit[1]: infoSong[formsToEdit[1]],
									formsToEdit[2]: int(infoSong[formsToEdit[2]]),
									formsToEdit[3]: infoSong[formsToEdit[3]],
									'text': textOfSong,
								})
		for i in range(len(formsToEdit)):
			request.session[formsToEdit[i]] = str(infoSong[i])
		request.session['formsToEdit'] = formsToEdit
		request.session['text'] = textOfSong
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
			songBook.saveDB()
			# songBook.createHTML('../docs')
			# songBook.createHTMLForDjango('./docs')
			return HttpResponseRedirect('editSong.html?song=%s'%name)
	# if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()

	return render(request, 'addSong.html', {'form': form})

def song(request):
	form = NameForm(request.GET)
	name = form.data['song']
	template = loader.get_template('song.html')
	songsDir = '../songs/'
	songBookDbRow = pd.read_csv(Path(songsDir).joinpath("00_songdb.csv"),encoding="utf-8").query('name == @name').iloc[0]
	# songBookTex = 'Songbook'

	# create song book
	# songBook = SongBook(songsDir,songBookTex)
	with open(Path('../').joinpath(songBookDbRow['path']),"r", encoding='utf-8') as tex:
		content=tex.read()

	content = SongBook.songToHtml(content)

	capo = ''
	try:
		if songBookDbRow['capo'] != 0:
			capo = '<div id="capo">Capo %d</div>' % int(songBookDbRow['capo'])
	except:
		pass

	context = {
		'name': name.replace('_', ' '),
		'name2': name,
		'author':songBookDbRow['author'],
		'capo': capo,
		'songText': content,
	}
	return HttpResponse(template.render(context, request))

def pdfCompilation(request):
	if request.method == 'GET':
		form = NameForm(request.GET)
		if not (len(form.data)) == 0:	
			if form.data['inProgress'] == '1':
				songsDir = '../songs/'
				songBookTex = 'Songbook'
				songBook = SongBook(songsDir,songBookTex)
				songBook.createSongBook(runFromWeb=True) 
				form.full_clean()
				template = loader.get_template('pdfCompilation.html')
				context = {
					'tlacitko': 'Kompilace dokončena',
				}
				return HttpResponse(template.render(context, request))
		else:
			template = loader.get_template('pdfCompilation.html')
			context = {
				'tlacitko': 'Zkompiluj PDF',
			}
			return HttpResponse(template.render(context, request))
	else:
		template = loader.get_template('pdfCompilation.html')
		context = {
			'tlacitko': 'Zkompiluj PDF',
		}
		return HttpResponse(template.render(context, request))

def handleDownload(request):
	# Define the full file path
	filepath = '../Songbook.pdf'
	# Open the file for reading content
	path = open(filepath, 'rb')
	response = HttpResponse(path)
	# Set the HTTP header for sending to browser
	response['Content-Disposition'] = "attachment; filename=Songbook.pdf"
	# Return the response value
	return response
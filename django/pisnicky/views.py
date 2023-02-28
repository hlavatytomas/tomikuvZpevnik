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

def p0(request):
	return render(request, '1970.html')

def p1(request):
	return render(request, '1_Signální.html')

def p2(request):
	return render(request, 'Accidentally_In_Love.html')

def p3(request):
	return render(request, 'Africa.html')

def p4(request):
	return render(request, 'Anděl.html')

def p5(request):
	return render(request, 'Ani_K_Stáru.html')

def p6(request):
	return render(request, 'Až_Mi_Bude_Pětašedesát.html')

def p7(request):
	return render(request, 'Bad_Bad_Leroy_Brown.html')

def p8(request):
	return render(request, 'Baroko.html')

def p9(request):
	return render(request, 'Batalion.html')

def p10(request):
	return render(request, 'Bára.html')

def p11(request):
	return render(request, 'Behind_Blue_Eyes.html')

def p12(request):
	return render(request, 'Bláznova_Ukolébavka.html')

def p13(request):
	return render(request, 'Blíženci.html')

def p14(request):
	return render(request, 'Boli_Sme_Raz_Milovaní.html')

def p15(request):
	return render(request, 'Boulevard_Of_Broken_Dreams.html')

def p16(request):
	return render(request, 'Budu_Všechno_Co_Si_Budeš_Přát.html')

def p17(request):
	return render(request, 'Cant_Help_Falling_In_Love.html')

def p18(request):
	return render(request, 'Cesta.html')

def p19(request):
	return render(request, 'Cesta_Z_Města.html')

def p20(request):
	return render(request, 'Chci_Zas_V_Tobě_Spát.html')

def p21(request):
	return render(request, 'Co_Z_Tebe_Bude.html')

def p22(request):
	return render(request, 'Čarodějnice_Z_Amesbury.html')

def p23(request):
	return render(request, 'Černí_andělé.html')

def p24(request):
	return render(request, 'Darmodej.html')

def p25(request):
	return render(request, 'Dej_Mi_Víc_Své_Lásky.html')

def p26(request):
	return render(request, 'Demons.html')

def p27(request):
	return render(request, 'Dlouhej_Kouř.html')

def p28(request):
	return render(request, 'Dobrák_Od_Kosti.html')

def p29(request):
	return render(request, 'Dont_Look_Back_In_Anger.html')

def p30(request):
	return render(request, 'Do_Nebe.html')

def p31(request):
	return render(request, 'Drive_By.html')

def p32(request):
	return render(request, 'Drobná_Paralela.html')

def p33(request):
	return render(request, 'Duše_Z_Gumy.html')

def p34(request):
	return render(request, 'Fair_Play.html')

def p35(request):
	return render(request, 'Get_Lucky.html')

def p36(request):
	return render(request, 'Good_Riddance_Time_Of_Your_Life.html')

def p37(request):
	return render(request, 'Grónská_písnička.html')

def p38(request):
	return render(request, 'Hallelujah.html')

def p39(request):
	return render(request, 'Hero.html')

def p40(request):
	return render(request, 'Hey_Soul_Sister.html')

def p41(request):
	return render(request, 'Hey_There_Delilah.html')

def p42(request):
	return render(request, 'Hlídač_Krav.html')

def p43(request):
	return render(request, 'Hlupák_Váhá.html')

def p44(request):
	return render(request, 'Holky_To_Objektivně_Lehčí_Maj.html')

def p45(request):
	return render(request, 'Hollywood_Hills.html')

def p46(request):
	return render(request, 'Honey_Honey.html')

def p47(request):
	return render(request, 'Hotel_California.html')

def p48(request):
	return render(request, 'Hrobar.html')

def p49(request):
	return render(request, 'Hruška.html')

def p50(request):
	return render(request, 'Im_A_Believer.html')

def p51(request):
	return render(request, 'Im_Yours.html')

def p52(request):
	return render(request, 'Jarní_Tání.html')

def p53(request):
	return render(request, 'Jasná_Zpráva.html')

def p54(request):
	return render(request, 'Jdou_Po_Mně_Jdou.html')

def p55(request):
	return render(request, 'Jožin_Z_Bažin.html')

def p56(request):
	return render(request, 'Každý_Ráno.html')

def p57(request):
	return render(request, 'Kdo_Vchází_Do_Tvých_Snů_Má_Lásko.html')

def p58(request):
	return render(request, 'Když_Nemůžeš_Tak_Přidej.html')

def p59(request):
	return render(request, 'Krátke_Lásky.html')

def p60(request):
	return render(request, 'Křídla_Z_Mýdla.html')

def p61(request):
	return render(request, 'Kupte_Si_Hřebeny.html')

def p62(request):
	return render(request, 'Kutil.html')

def p63(request):
	return render(request, 'Lachtani.html')

def p64(request):
	return render(request, 'Láska_Na_Vsi.html')

def p65(request):
	return render(request, 'Leaving_On_A_Jet_Plane.html')

def p66(request):
	return render(request, 'Let_Her_Go.html')

def p67(request):
	return render(request, 'Let_It_Be.html')

def p68(request):
	return render(request, 'Let_It_Go.html')

def p69(request):
	return render(request, 'Living_Next_Door_To_Alice.html')

def p70(request):
	return render(request, 'Magdalena.html')

def p71(request):
	return render(request, 'Malá_Dáma.html')

def p72(request):
	return render(request, 'Malování.html')

def p73(request):
	return render(request, 'Mamma_Mia.html')

def p74(request):
	return render(request, 'Marie.html')

def p75(request):
	return render(request, 'Matfyzák_Na_Discu.html')

def p76(request):
	return render(request, 'Mám_Doma_Kočku.html')

def p77(request):
	return render(request, 'Mám_Jizvu_Na_Rtu.html')

def p78(request):
	return render(request, 'Mikymauz.html')

def p79(request):
	return render(request, 'Milenci_V_Texaskách.html')

def p80(request):
	return render(request, 'Million_Reasons.html')

def p81(request):
	return render(request, 'Mimorealita.html')

def p82(request):
	return render(request, 'Minulost.html')

def p83(request):
	return render(request, 'Mrs_Robinson.html')

def p84(request):
	return render(request, 'Můj_Svět.html')

def p85(request):
	return render(request, 'Nagasaki_Hirošima.html')

def p86(request):
	return render(request, 'Nechte_Zvony_Znít.html')

def p87(request):
	return render(request, 'Netušim.html')

def p88(request):
	return render(request, 'Okno_Mé_Lásky.html')

def p89(request):
	return render(request, 'On_Top_Of_The_World.html')

def p90(request):
	return render(request, 'Osmý_Den.html')

def p91(request):
	return render(request, 'Panic.html')

def p92(request):
	return render(request, 'Pažitka.html')

def p93(request):
	return render(request, 'Perfect.html')

def p94(request):
	return render(request, 'Piano_Man.html')

def p95(request):
	return render(request, 'Pocity.html')

def p96(request):
	return render(request, 'Pohoda.html')

def p97(request):
	return render(request, 'Pompeii.html')

def p98(request):
	return render(request, 'Proklínám.html')

def p99(request):
	return render(request, 'Proměny.html')

def p100(request):
	return render(request, 'Ráda_Se_Miluje.html')

def p101(request):
	return render(request, 'Ring-O-Ding.html')

def p102(request):
	return render(request, 'Riptide.html')

def p103(request):
	return render(request, 'Runaway_Train.html')

def p104(request):
	return render(request, 'Sáro.html')

def p105(request):
	return render(request, 'Sbírka_Zvadlejch_Růží.html')

def p106(request):
	return render(request, 'Sbohem_Galánečko.html')

def p107(request):
	return render(request, 'Slzy_Tvý_Mámy.html')

def p108(request):
	return render(request, 'Srdce_Jako_Knize_Rohan.html')

def p109(request):
	return render(request, 'Starý_Muž.html')

def p110(request):
	return render(request, 'Stitches.html')

def p111(request):
	return render(request, 'Svaz_Českých_Bohémů.html')

def p112(request):
	return render(request, 'Šaman.html')

def p113(request):
	return render(request, 'Šrouby_A_Matice.html')

def p114(request):
	return render(request, 'Těšínská.html')

def p115(request):
	return render(request, 'Thinking_Out_Loud.html')

def p116(request):
	return render(request, 'This_Is_The_Life.html')

def p117(request):
	return render(request, 'Touha.html')

def p118(request):
	return render(request, 'Toulavej.html')

def p119(request):
	return render(request, 'Tři_Kříže.html')

def p120(request):
	return render(request, 'Ulica.html')

def p121(request):
	return render(request, 'Umbrella.html')

def p122(request):
	return render(request, 'Untitled.html')

def p123(request):
	return render(request, 'Včelín.html')

def p124(request):
	return render(request, 'Veď_mě_dál,_cesto_má.html')

def p125(request):
	return render(request, 'Viva_La_Vida.html')

def p126(request):
	return render(request, 'Vymlácený_Entry.html')

def p127(request):
	return render(request, 'Vymyslená.html')

def p128(request):
	return render(request, 'V_7_25.html')

def p129(request):
	return render(request, 'V_Lese.html')

def p130(request):
	return render(request, 'Waterloo.html')

def p131(request):
	return render(request, 'When_All_Is_Said_And_Done.html')

def p132(request):
	return render(request, 'When_Youre_Gone.html')

def p133(request):
	return render(request, 'With_Or_Without_You.html')

def p134(request):
	return render(request, 'Wonderwall.html')

def p135(request):
	return render(request, 'Zalůbení.html')

def p136(request):
	return render(request, 'Zanedbaný_Sex.html')

def p137(request):
	return render(request, 'Zombie.html')

def p138(request):
	return render(request, 'Better_Together.html')

def p139(request):
	return render(request, 'Brandy_Youre_A_Fine_Girl.html')

def p140(request):
	return render(request, 'Let_My_Love_Open_The_Door.html')

def p141(request):
	return render(request, 'Mandy.html')

def p142(request):
	return render(request, 'Mmm_Mmm_Mmm_Mmm.html')

def p143(request):
	return render(request, 'Sweet_Child_O_Mine.html')

def p144(request):
	return render(request, 'Take_It_Easy.html')

def p145(request):
	return render(request, 'The_Weight.html')

def p146(request):
	return render(request, 'Waiting_On_The_World_To_Change.html')

def p147(request):
	return render(request, 'House_Of_Memories.html')

def p148(request):
	return render(request, 'Love_Again.html')

def p149(request):
	return render(request, 'Matfyzák_Na_Discu.html')

def p150(request):
	return render(request, 'Sweater_Weather.html')

def p151(request):
	return render(request, 'The_Middle.html')

def p152(request):
	return render(request, 'The_Saga_Begins.html')

def p153(request):
	return render(request, 'Ayo_Technology.html')

def p154(request):
	return render(request, 'Breakfast_At_Tiffanys.html')

def p155(request):
	return render(request, 'Dont_Go_Breaking_My_Heart.html')

def p156(request):
	return render(request, 'Jdevozem.html')

def p157(request):
	return render(request, 'Not_Fair.html')

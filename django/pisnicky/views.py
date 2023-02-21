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

def p0(request):
	return render(request, '1970.html')

def p1(request):
	return render(request, '1_Sign�ln�.html')

def p2(request):
	return render(request, 'Accidentally_In_Love.html')

def p3(request):
	return render(request, 'Africa.html')

def p4(request):
	return render(request, 'And�l.html')

def p5(request):
	return render(request, 'Ani_K_St�ru.html')

def p6(request):
	return render(request, 'A�_Mi_Bude_P�ta�edes�t.html')

def p7(request):
	return render(request, 'Bad_Bad_Leroy_Brown.html')

def p8(request):
	return render(request, 'Baroko.html')

def p9(request):
	return render(request, 'Batalion.html')

def p10(request):
	return render(request, 'B�ra.html')

def p11(request):
	return render(request, 'Behind_Blue_Eyes.html')

def p12(request):
	return render(request, 'Bl�znova_Ukol�bavka.html')

def p13(request):
	return render(request, 'Bl�enci.html')

def p14(request):
	return render(request, 'Boli_Sme_Raz_Milovan�.html')

def p15(request):
	return render(request, 'Boulevard_Of_Broken_Dreams.html')

def p16(request):
	return render(request, 'Budu_V�echno_Co_Si_Bude�_P��t.html')

def p17(request):
	return render(request, 'Cant_Help_Falling_In_Love.html')

def p18(request):
	return render(request, 'Cesta.html')

def p19(request):
	return render(request, 'Cesta_Z_M�sta.html')

def p20(request):
	return render(request, 'Chci_Zas_V_Tob�_Sp�t.html')

def p21(request):
	return render(request, 'Co_Z_Tebe_Bude.html')

def p22(request):
	return render(request, '�arod�jnice_Z_Amesbury.html')

def p23(request):
	return render(request, '�ern�_and�l�.html')

def p24(request):
	return render(request, 'Darmodej.html')

def p25(request):
	return render(request, 'Dej_Mi_V�c_Sv�_L�sky.html')

def p26(request):
	return render(request, 'Demons.html')

def p27(request):
	return render(request, 'Dlouhej_Kou�.html')

def p28(request):
	return render(request, 'Dobr�k_Od_Kosti.html')

def p29(request):
	return render(request, 'Dont_Look_Back_In_Anger.html')

def p30(request):
	return render(request, 'Do_Nebe.html')

def p31(request):
	return render(request, 'Drive_By.html')

def p32(request):
	return render(request, 'Drobn�_Paralela.html')

def p33(request):
	return render(request, 'Du�e_Z_Gumy.html')

def p34(request):
	return render(request, 'Fair_Play.html')

def p35(request):
	return render(request, 'Get_Lucky.html')

def p36(request):
	return render(request, 'Good_Riddance_Time_Of_Your_Life.html')

def p37(request):
	return render(request, 'Gr�nsk�_p�sni�ka.html')

def p38(request):
	return render(request, 'Hallelujah.html')

def p39(request):
	return render(request, 'Hero.html')

def p40(request):
	return render(request, 'Hey_Soul_Sister.html')

def p41(request):
	return render(request, 'Hey_There_Delilah.html')

def p42(request):
	return render(request, 'Hl�da�_Krav.html')

def p43(request):
	return render(request, 'Hlup�k_V�h�.html')

def p44(request):
	return render(request, 'Holky_To_Objektivn�_Leh��_Maj.html')

def p45(request):
	return render(request, 'Hollywood_Hills.html')

def p46(request):
	return render(request, 'Honey_Honey.html')

def p47(request):
	return render(request, 'Hotel_California.html')

def p48(request):
	return render(request, 'Hrobar.html')

def p49(request):
	return render(request, 'Hru�ka.html')

def p50(request):
	return render(request, 'Im_A_Believer.html')

def p51(request):
	return render(request, 'Im_Yours.html')

def p52(request):
	return render(request, 'Jarn�_T�n�.html')

def p53(request):
	return render(request, 'Jasn�_Zpr�va.html')

def p54(request):
	return render(request, 'Jdou_Po_Mn�_Jdou.html')

def p55(request):
	return render(request, 'Jo�in_Z_Ba�in.html')

def p56(request):
	return render(request, 'Ka�d�_R�no.html')

def p57(request):
	return render(request, 'Kdo_Vch�z�_Do_Tv�ch_Sn�_M�_L�sko.html')

def p58(request):
	return render(request, 'Kdy�_Nem��e�_Tak_P�idej.html')

def p59(request):
	return render(request, 'Kr�tke_L�sky.html')

def p60(request):
	return render(request, 'K��dla_Z_M�dla.html')

def p61(request):
	return render(request, 'Kupte_Si_H�ebeny.html')

def p62(request):
	return render(request, 'Kutil.html')

def p63(request):
	return render(request, 'Lachtani.html')

def p64(request):
	return render(request, 'L�ska_Na_Vsi.html')

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
	return render(request, 'Mal�_D�ma.html')

def p72(request):
	return render(request, 'Malov�n�.html')

def p73(request):
	return render(request, 'Mamma_Mia.html')

def p74(request):
	return render(request, 'Marie.html')

def p75(request):
	return render(request, 'Matfyz�k_Na_Discu.html')

def p76(request):
	return render(request, 'M�m_Doma_Ko�ku.html')

def p77(request):
	return render(request, 'M�m_Jizvu_Na_Rtu.html')

def p78(request):
	return render(request, 'Mikymauz.html')

def p79(request):
	return render(request, 'Milenci_V_Texask�ch.html')

def p80(request):
	return render(request, 'Million_Reasons.html')

def p81(request):
	return render(request, 'Mimorealita.html')

def p82(request):
	return render(request, 'Minulost.html')

def p83(request):
	return render(request, 'Mrs_Robinson.html')

def p84(request):
	return render(request, 'M�j_Sv�t.html')

def p85(request):
	return render(request, 'Nagasaki_Hiro�ima.html')

def p86(request):
	return render(request, 'Nechte_Zvony_Zn�t.html')

def p87(request):
	return render(request, 'Netu�im.html')

def p88(request):
	return render(request, 'Okno_M�_L�sky.html')

def p89(request):
	return render(request, 'On_Top_Of_The_World.html')

def p90(request):
	return render(request, 'Osm�_Den.html')

def p91(request):
	return render(request, 'Panic.html')

def p92(request):
	return render(request, 'Pa�itka.html')

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
	return render(request, 'Prokl�n�m.html')

def p99(request):
	return render(request, 'Prom�ny.html')

def p100(request):
	return render(request, 'R�da_Se_Miluje.html')

def p101(request):
	return render(request, 'Ring-O-Ding.html')

def p102(request):
	return render(request, 'Riptide.html')

def p103(request):
	return render(request, 'Runaway_Train.html')

def p104(request):
	return render(request, 'S�ro.html')

def p105(request):
	return render(request, 'Sb�rka_Zvadlejch_R���.html')

def p106(request):
	return render(request, 'Sbohem_Gal�ne�ko.html')

def p107(request):
	return render(request, 'Slzy_Tv�_M�my.html')

def p108(request):
	return render(request, 'Srdce_Jako_Knize_Rohan.html')

def p109(request):
	return render(request, 'Star�_Mu�.html')

def p110(request):
	return render(request, 'Stitches.html')

def p111(request):
	return render(request, 'Svaz_�esk�ch_Boh�m�.html')

def p112(request):
	return render(request, '�aman.html')

def p113(request):
	return render(request, '�rouby_A_Matice.html')

def p114(request):
	return render(request, 'T��nsk�.html')

def p115(request):
	return render(request, 'Thinking_Out_Loud.html')

def p116(request):
	return render(request, 'This_Is_The_Life.html')

def p117(request):
	return render(request, 'Touha.html')

def p118(request):
	return render(request, 'Toulavej.html')

def p119(request):
	return render(request, 'T�i_K��e.html')

def p120(request):
	return render(request, 'Ulica.html')

def p121(request):
	return render(request, 'Umbrella.html')

def p122(request):
	return render(request, 'Untitled.html')

def p123(request):
	return render(request, 'V�el�n.html')

def p124(request):
	return render(request, 'Ve�_m�_d�l,_cesto_m�.html')

def p125(request):
	return render(request, 'Viva_La_Vida.html')

def p126(request):
	return render(request, 'Vyml�cen�_Entry.html')

def p127(request):
	return render(request, 'Vymyslen�.html')

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
	return render(request, 'Zal�ben�.html')

def p136(request):
	return render(request, 'Zanedban�_Sex.html')

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
	return render(request, 'Matfyz�k_Na_Discu.html')

def p150(request):
	return render(request, 'Sweater_Weather.html')

def p151(request):
	return render(request, 'The_Middle.html')

def p152(request):
	return render(request, 'The_Saga_Begins.html')

def p153(request):
	return render(request, 'Breakfast_At_Tiffanys.html')

def p154(request):
	return render(request, 'Dont_Go_Breaking_My_Heart.html')

def p155(request):
	return render(request, 'Jdevozem.html')

def p156(request):
	return render(request, 'Not_Fair.html')

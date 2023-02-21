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
    # path('docs/songs/1970.html', views.p1970, name='p1970'),    # added
	path('docs/songs/1970.html', views.p0, name='1970'),
	path('docs/songs/1_Sign�ln�.html', views.p1, name='1_Sign�ln�'),
	path('docs/songs/Accidentally_In_Love.html', views.p2, name='Accidentally_In_Love'),
	path('docs/songs/Africa.html', views.p3, name='Africa'),
	path('docs/songs/And�l.html', views.p4, name='And�l'),
	path('docs/songs/Ani_K_St�ru.html', views.p5, name='Ani_K_St�ru'),
	path('docs/songs/A�_Mi_Bude_P�ta�edes�t.html', views.p6, name='A�_Mi_Bude_P�ta�edes�t'),
	path('docs/songs/Bad_Bad_Leroy_Brown.html', views.p7, name='Bad_Bad_Leroy_Brown'),
	path('docs/songs/Baroko.html', views.p8, name='Baroko'),
	path('docs/songs/Batalion.html', views.p9, name='Batalion'),
	path('docs/songs/B�ra.html', views.p10, name='B�ra'),
	path('docs/songs/Behind_Blue_Eyes.html', views.p11, name='Behind_Blue_Eyes'),
	path('docs/songs/Bl�znova_Ukol�bavka.html', views.p12, name='Bl�znova_Ukol�bavka'),
	path('docs/songs/Bl�enci.html', views.p13, name='Bl�enci'),
	path('docs/songs/Boli_Sme_Raz_Milovan�.html', views.p14, name='Boli_Sme_Raz_Milovan�'),
	path('docs/songs/Boulevard_Of_Broken_Dreams.html', views.p15, name='Boulevard_Of_Broken_Dreams'),
	path('docs/songs/Budu_V�echno_Co_Si_Bude�_P��t.html', views.p16, name='Budu_V�echno_Co_Si_Bude�_P��t'),
	path('docs/songs/Cant_Help_Falling_In_Love.html', views.p17, name='Cant_Help_Falling_In_Love'),
	path('docs/songs/Cesta.html', views.p18, name='Cesta'),
	path('docs/songs/Cesta_Z_M�sta.html', views.p19, name='Cesta_Z_M�sta'),
	path('docs/songs/Chci_Zas_V_Tob�_Sp�t.html', views.p20, name='Chci_Zas_V_Tob�_Sp�t'),
	path('docs/songs/Co_Z_Tebe_Bude.html', views.p21, name='Co_Z_Tebe_Bude'),
	path('docs/songs/�arod�jnice_Z_Amesbury.html', views.p22, name='�arod�jnice_Z_Amesbury'),
	path('docs/songs/�ern�_and�l�.html', views.p23, name='�ern�_and�l�'),
	path('docs/songs/Darmodej.html', views.p24, name='Darmodej'),
	path('docs/songs/Dej_Mi_V�c_Sv�_L�sky.html', views.p25, name='Dej_Mi_V�c_Sv�_L�sky'),
	path('docs/songs/Demons.html', views.p26, name='Demons'),
	path('docs/songs/Dlouhej_Kou�.html', views.p27, name='Dlouhej_Kou�'),
	path('docs/songs/Dobr�k_Od_Kosti.html', views.p28, name='Dobr�k_Od_Kosti'),
	path('docs/songs/Dont_Look_Back_In_Anger.html', views.p29, name='Dont_Look_Back_In_Anger'),
	path('docs/songs/Do_Nebe.html', views.p30, name='Do_Nebe'),
	path('docs/songs/Drive_By.html', views.p31, name='Drive_By'),
	path('docs/songs/Drobn�_Paralela.html', views.p32, name='Drobn�_Paralela'),
	path('docs/songs/Du�e_Z_Gumy.html', views.p33, name='Du�e_Z_Gumy'),
	path('docs/songs/Fair_Play.html', views.p34, name='Fair_Play'),
	path('docs/songs/Get_Lucky.html', views.p35, name='Get_Lucky'),
	path('docs/songs/Good_Riddance_Time_Of_Your_Life.html', views.p36, name='Good_Riddance_Time_Of_Your_Life'),
	path('docs/songs/Gr�nsk�_p�sni�ka.html', views.p37, name='Gr�nsk�_p�sni�ka'),
	path('docs/songs/Hallelujah.html', views.p38, name='Hallelujah'),
	path('docs/songs/Hero.html', views.p39, name='Hero'),
	path('docs/songs/Hey_Soul_Sister.html', views.p40, name='Hey_Soul_Sister'),
	path('docs/songs/Hey_There_Delilah.html', views.p41, name='Hey_There_Delilah'),
	path('docs/songs/Hl�da�_Krav.html', views.p42, name='Hl�da�_Krav'),
	path('docs/songs/Hlup�k_V�h�.html', views.p43, name='Hlup�k_V�h�'),
	path('docs/songs/Holky_To_Objektivn�_Leh��_Maj.html', views.p44, name='Holky_To_Objektivn�_Leh��_Maj'),
	path('docs/songs/Hollywood_Hills.html', views.p45, name='Hollywood_Hills'),
	path('docs/songs/Honey_Honey.html', views.p46, name='Honey_Honey'),
	path('docs/songs/Hotel_California.html', views.p47, name='Hotel_California'),
	path('docs/songs/Hrobar.html', views.p48, name='Hrobar'),
	path('docs/songs/Hru�ka.html', views.p49, name='Hru�ka'),
	path('docs/songs/Im_A_Believer.html', views.p50, name='Im_A_Believer'),
	path('docs/songs/Im_Yours.html', views.p51, name='Im_Yours'),
	path('docs/songs/Jarn�_T�n�.html', views.p52, name='Jarn�_T�n�'),
	path('docs/songs/Jasn�_Zpr�va.html', views.p53, name='Jasn�_Zpr�va'),
	path('docs/songs/Jdou_Po_Mn�_Jdou.html', views.p54, name='Jdou_Po_Mn�_Jdou'),
	path('docs/songs/Jo�in_Z_Ba�in.html', views.p55, name='Jo�in_Z_Ba�in'),
	path('docs/songs/Ka�d�_R�no.html', views.p56, name='Ka�d�_R�no'),
	path('docs/songs/Kdo_Vch�z�_Do_Tv�ch_Sn�_M�_L�sko.html', views.p57, name='Kdo_Vch�z�_Do_Tv�ch_Sn�_M�_L�sko'),
	path('docs/songs/Kdy�_Nem��e�_Tak_P�idej.html', views.p58, name='Kdy�_Nem��e�_Tak_P�idej'),
	path('docs/songs/Kr�tke_L�sky.html', views.p59, name='Kr�tke_L�sky'),
	path('docs/songs/K��dla_Z_M�dla.html', views.p60, name='K��dla_Z_M�dla'),
	path('docs/songs/Kupte_Si_H�ebeny.html', views.p61, name='Kupte_Si_H�ebeny'),
	path('docs/songs/Kutil.html', views.p62, name='Kutil'),
	path('docs/songs/Lachtani.html', views.p63, name='Lachtani'),
	path('docs/songs/L�ska_Na_Vsi.html', views.p64, name='L�ska_Na_Vsi'),
	path('docs/songs/Leaving_On_A_Jet_Plane.html', views.p65, name='Leaving_On_A_Jet_Plane'),
	path('docs/songs/Let_Her_Go.html', views.p66, name='Let_Her_Go'),
	path('docs/songs/Let_It_Be.html', views.p67, name='Let_It_Be'),
	path('docs/songs/Let_It_Go.html', views.p68, name='Let_It_Go'),
	path('docs/songs/Living_Next_Door_To_Alice.html', views.p69, name='Living_Next_Door_To_Alice'),
	path('docs/songs/Magdalena.html', views.p70, name='Magdalena'),
	path('docs/songs/Mal�_D�ma.html', views.p71, name='Mal�_D�ma'),
	path('docs/songs/Malov�n�.html', views.p72, name='Malov�n�'),
	path('docs/songs/Mamma_Mia.html', views.p73, name='Mamma_Mia'),
	path('docs/songs/Marie.html', views.p74, name='Marie'),
	path('docs/songs/Matfyz�k_Na_Discu.html', views.p75, name='Matfyz�k_Na_Discu'),
	path('docs/songs/M�m_Doma_Ko�ku.html', views.p76, name='M�m_Doma_Ko�ku'),
	path('docs/songs/M�m_Jizvu_Na_Rtu.html', views.p77, name='M�m_Jizvu_Na_Rtu'),
	path('docs/songs/Mikymauz.html', views.p78, name='Mikymauz'),
	path('docs/songs/Milenci_V_Texask�ch.html', views.p79, name='Milenci_V_Texask�ch'),
	path('docs/songs/Million_Reasons.html', views.p80, name='Million_Reasons'),
	path('docs/songs/Mimorealita.html', views.p81, name='Mimorealita'),
	path('docs/songs/Minulost.html', views.p82, name='Minulost'),
	path('docs/songs/Mrs_Robinson.html', views.p83, name='Mrs_Robinson'),
	path('docs/songs/M�j_Sv�t.html', views.p84, name='M�j_Sv�t'),
	path('docs/songs/Nagasaki_Hiro�ima.html', views.p85, name='Nagasaki_Hiro�ima'),
	path('docs/songs/Nechte_Zvony_Zn�t.html', views.p86, name='Nechte_Zvony_Zn�t'),
	path('docs/songs/Netu�im.html', views.p87, name='Netu�im'),
	path('docs/songs/Okno_M�_L�sky.html', views.p88, name='Okno_M�_L�sky'),
	path('docs/songs/On_Top_Of_The_World.html', views.p89, name='On_Top_Of_The_World'),
	path('docs/songs/Osm�_Den.html', views.p90, name='Osm�_Den'),
	path('docs/songs/Panic.html', views.p91, name='Panic'),
	path('docs/songs/Pa�itka.html', views.p92, name='Pa�itka'),
	path('docs/songs/Perfect.html', views.p93, name='Perfect'),
	path('docs/songs/Piano_Man.html', views.p94, name='Piano_Man'),
	path('docs/songs/Pocity.html', views.p95, name='Pocity'),
	path('docs/songs/Pohoda.html', views.p96, name='Pohoda'),
	path('docs/songs/Pompeii.html', views.p97, name='Pompeii'),
	path('docs/songs/Prokl�n�m.html', views.p98, name='Prokl�n�m'),
	path('docs/songs/Prom�ny.html', views.p99, name='Prom�ny'),
	path('docs/songs/R�da_Se_Miluje.html', views.p100, name='R�da_Se_Miluje'),
	path('docs/songs/Ring-O-Ding.html', views.p101, name='Ring-O-Ding'),
	path('docs/songs/Riptide.html', views.p102, name='Riptide'),
	path('docs/songs/Runaway_Train.html', views.p103, name='Runaway_Train'),
	path('docs/songs/S�ro.html', views.p104, name='S�ro'),
	path('docs/songs/Sb�rka_Zvadlejch_R���.html', views.p105, name='Sb�rka_Zvadlejch_R���'),
	path('docs/songs/Sbohem_Gal�ne�ko.html', views.p106, name='Sbohem_Gal�ne�ko'),
	path('docs/songs/Slzy_Tv�_M�my.html', views.p107, name='Slzy_Tv�_M�my'),
	path('docs/songs/Srdce_Jako_Knize_Rohan.html', views.p108, name='Srdce_Jako_Knize_Rohan'),
	path('docs/songs/Star�_Mu�.html', views.p109, name='Star�_Mu�'),
	path('docs/songs/Stitches.html', views.p110, name='Stitches'),
	path('docs/songs/Svaz_�esk�ch_Boh�m�.html', views.p111, name='Svaz_�esk�ch_Boh�m�'),
	path('docs/songs/�aman.html', views.p112, name='�aman'),
	path('docs/songs/�rouby_A_Matice.html', views.p113, name='�rouby_A_Matice'),
	path('docs/songs/T��nsk�.html', views.p114, name='T��nsk�'),
	path('docs/songs/Thinking_Out_Loud.html', views.p115, name='Thinking_Out_Loud'),
	path('docs/songs/This_Is_The_Life.html', views.p116, name='This_Is_The_Life'),
	path('docs/songs/Touha.html', views.p117, name='Touha'),
	path('docs/songs/Toulavej.html', views.p118, name='Toulavej'),
	path('docs/songs/T�i_K��e.html', views.p119, name='T�i_K��e'),
	path('docs/songs/Ulica.html', views.p120, name='Ulica'),
	path('docs/songs/Umbrella.html', views.p121, name='Umbrella'),
	path('docs/songs/Untitled.html', views.p122, name='Untitled'),
	path('docs/songs/V�el�n.html', views.p123, name='V�el�n'),
	path('docs/songs/Ve�_m�_d�l,_cesto_m�.html', views.p124, name='Ve�_m�_d�l,_cesto_m�'),
	path('docs/songs/Viva_La_Vida.html', views.p125, name='Viva_La_Vida'),
	path('docs/songs/Vyml�cen�_Entry.html', views.p126, name='Vyml�cen�_Entry'),
	path('docs/songs/Vymyslen�.html', views.p127, name='Vymyslen�'),
	path('docs/songs/V_7_25.html', views.p128, name='V_7_25'),
	path('docs/songs/V_Lese.html', views.p129, name='V_Lese'),
	path('docs/songs/Waterloo.html', views.p130, name='Waterloo'),
	path('docs/songs/When_All_Is_Said_And_Done.html', views.p131, name='When_All_Is_Said_And_Done'),
	path('docs/songs/When_Youre_Gone.html', views.p132, name='When_Youre_Gone'),
	path('docs/songs/With_Or_Without_You.html', views.p133, name='With_Or_Without_You'),
	path('docs/songs/Wonderwall.html', views.p134, name='Wonderwall'),
	path('docs/songs/Zal�ben�.html', views.p135, name='Zal�ben�'),
	path('docs/songs/Zanedban�_Sex.html', views.p136, name='Zanedban�_Sex'),
	path('docs/songs/Zombie.html', views.p137, name='Zombie'),
	path('docs/songs/Better_Together.html', views.p138, name='Better_Together'),
	path('docs/songs/Brandy_Youre_A_Fine_Girl.html', views.p139, name='Brandy_Youre_A_Fine_Girl'),
	path('docs/songs/Let_My_Love_Open_The_Door.html', views.p140, name='Let_My_Love_Open_The_Door'),
	path('docs/songs/Mandy.html', views.p141, name='Mandy'),
	path('docs/songs/Mmm_Mmm_Mmm_Mmm.html', views.p142, name='Mmm_Mmm_Mmm_Mmm'),
	path('docs/songs/Sweet_Child_O_Mine.html', views.p143, name='Sweet_Child_O_Mine'),
	path('docs/songs/Take_It_Easy.html', views.p144, name='Take_It_Easy'),
	path('docs/songs/The_Weight.html', views.p145, name='The_Weight'),
	path('docs/songs/Waiting_On_The_World_To_Change.html', views.p146, name='Waiting_On_The_World_To_Change'),
	path('docs/songs/House_Of_Memories.html', views.p147, name='House_Of_Memories'),
	path('docs/songs/Love_Again.html', views.p148, name='Love_Again'),
	path('docs/songs/Matfyz�k_Na_Discu.html', views.p149, name='Matfyz�k_Na_Discu'),
	path('docs/songs/Sweater_Weather.html', views.p150, name='Sweater_Weather'),
	path('docs/songs/The_Middle.html', views.p151, name='The_Middle'),
	path('docs/songs/The_Saga_Begins.html', views.p152, name='The_Saga_Begins'),
	path('docs/songs/Breakfast_At_Tiffanys.html', views.p153, name='Breakfast_At_Tiffanys'),
	path('docs/songs/Dont_Go_Breaking_My_Heart.html', views.p154, name='Dont_Go_Breaking_My_Heart'),
	path('docs/songs/Jdevozem.html', views.p155, name='Jdevozem'),
	path('docs/songs/Not_Fair.html', views.p156, name='Not_Fair'),
]
# for i in range(len(songBook.songsLst)):
#     urlpatterns.append(path('docs/songs/%s.html'%songBook.songsLst, render('1970.html'), name='home'))

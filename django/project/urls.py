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
	path('docs/songs/1_Signální.html', views.p1, name='1_Signální'),
	path('docs/songs/Accidentally_In_Love.html', views.p2, name='Accidentally_In_Love'),
	path('docs/songs/Africa.html', views.p3, name='Africa'),
	path('docs/songs/Anděl.html', views.p4, name='Anděl'),
	path('docs/songs/Ani_K_Stáru.html', views.p5, name='Ani_K_Stáru'),
	path('docs/songs/Až_Mi_Bude_Pětašedesát.html', views.p6, name='Až_Mi_Bude_Pětašedesát'),
	path('docs/songs/Bad_Bad_Leroy_Brown.html', views.p7, name='Bad_Bad_Leroy_Brown'),
	path('docs/songs/Baroko.html', views.p8, name='Baroko'),
	path('docs/songs/Batalion.html', views.p9, name='Batalion'),
	path('docs/songs/Bára.html', views.p10, name='Bára'),
	path('docs/songs/Behind_Blue_Eyes.html', views.p11, name='Behind_Blue_Eyes'),
	path('docs/songs/Bláznova_Ukolébavka.html', views.p12, name='Bláznova_Ukolébavka'),
	path('docs/songs/Blíženci.html', views.p13, name='Blíženci'),
	path('docs/songs/Boli_Sme_Raz_Milovaní.html', views.p14, name='Boli_Sme_Raz_Milovaní'),
	path('docs/songs/Boulevard_Of_Broken_Dreams.html', views.p15, name='Boulevard_Of_Broken_Dreams'),
	path('docs/songs/Budu_Všechno_Co_Si_Budeš_Přát.html', views.p16, name='Budu_Všechno_Co_Si_Budeš_Přát'),
	path('docs/songs/Cant_Help_Falling_In_Love.html', views.p17, name='Cant_Help_Falling_In_Love'),
	path('docs/songs/Cesta.html', views.p18, name='Cesta'),
	path('docs/songs/Cesta_Z_Města.html', views.p19, name='Cesta_Z_Města'),
	path('docs/songs/Chci_Zas_V_Tobě_Spát.html', views.p20, name='Chci_Zas_V_Tobě_Spát'),
	path('docs/songs/Co_Z_Tebe_Bude.html', views.p21, name='Co_Z_Tebe_Bude'),
	path('docs/songs/Čarodějnice_Z_Amesbury.html', views.p22, name='Čarodějnice_Z_Amesbury'),
	path('docs/songs/Černí_andělé.html', views.p23, name='Černí_andělé'),
	path('docs/songs/Darmodej.html', views.p24, name='Darmodej'),
	path('docs/songs/Dej_Mi_Víc_Své_Lásky.html', views.p25, name='Dej_Mi_Víc_Své_Lásky'),
	path('docs/songs/Demons.html', views.p26, name='Demons'),
	path('docs/songs/Dlouhej_Kouř.html', views.p27, name='Dlouhej_Kouř'),
	path('docs/songs/Dobrák_Od_Kosti.html', views.p28, name='Dobrák_Od_Kosti'),
	path('docs/songs/Dont_Look_Back_In_Anger.html', views.p29, name='Dont_Look_Back_In_Anger'),
	path('docs/songs/Do_Nebe.html', views.p30, name='Do_Nebe'),
	path('docs/songs/Drive_By.html', views.p31, name='Drive_By'),
	path('docs/songs/Drobná_Paralela.html', views.p32, name='Drobná_Paralela'),
	path('docs/songs/Duše_Z_Gumy.html', views.p33, name='Duše_Z_Gumy'),
	path('docs/songs/Fair_Play.html', views.p34, name='Fair_Play'),
	path('docs/songs/Get_Lucky.html', views.p35, name='Get_Lucky'),
	path('docs/songs/Good_Riddance_Time_Of_Your_Life.html', views.p36, name='Good_Riddance_Time_Of_Your_Life'),
	path('docs/songs/Grónská_písnička.html', views.p37, name='Grónská_písnička'),
	path('docs/songs/Hallelujah.html', views.p38, name='Hallelujah'),
	path('docs/songs/Hero.html', views.p39, name='Hero'),
	path('docs/songs/Hey_Soul_Sister.html', views.p40, name='Hey_Soul_Sister'),
	path('docs/songs/Hey_There_Delilah.html', views.p41, name='Hey_There_Delilah'),
	path('docs/songs/Hlídač_Krav.html', views.p42, name='Hlídač_Krav'),
	path('docs/songs/Hlupák_Váhá.html', views.p43, name='Hlupák_Váhá'),
	path('docs/songs/Holky_To_Objektivně_Lehčí_Maj.html', views.p44, name='Holky_To_Objektivně_Lehčí_Maj'),
	path('docs/songs/Hollywood_Hills.html', views.p45, name='Hollywood_Hills'),
	path('docs/songs/Honey_Honey.html', views.p46, name='Honey_Honey'),
	path('docs/songs/Hotel_California.html', views.p47, name='Hotel_California'),
	path('docs/songs/Hrobar.html', views.p48, name='Hrobar'),
	path('docs/songs/Hruška.html', views.p49, name='Hruška'),
	path('docs/songs/Im_A_Believer.html', views.p50, name='Im_A_Believer'),
	path('docs/songs/Im_Yours.html', views.p51, name='Im_Yours'),
	path('docs/songs/Jarní_Tání.html', views.p52, name='Jarní_Tání'),
	path('docs/songs/Jasná_Zpráva.html', views.p53, name='Jasná_Zpráva'),
	path('docs/songs/Jdou_Po_Mně_Jdou.html', views.p54, name='Jdou_Po_Mně_Jdou'),
	path('docs/songs/Jožin_Z_Bažin.html', views.p55, name='Jožin_Z_Bažin'),
	path('docs/songs/Každý_Ráno.html', views.p56, name='Každý_Ráno'),
	path('docs/songs/Kdo_Vchází_Do_Tvých_Snů_Má_Lásko.html', views.p57, name='Kdo_Vchází_Do_Tvých_Snů_Má_Lásko'),
	path('docs/songs/Když_Nemůžeš_Tak_Přidej.html', views.p58, name='Když_Nemůžeš_Tak_Přidej'),
	path('docs/songs/Krátke_Lásky.html', views.p59, name='Krátke_Lásky'),
	path('docs/songs/Křídla_Z_Mýdla.html', views.p60, name='Křídla_Z_Mýdla'),
	path('docs/songs/Kupte_Si_Hřebeny.html', views.p61, name='Kupte_Si_Hřebeny'),
	path('docs/songs/Kutil.html', views.p62, name='Kutil'),
	path('docs/songs/Lachtani.html', views.p63, name='Lachtani'),
	path('docs/songs/Láska_Na_Vsi.html', views.p64, name='Láska_Na_Vsi'),
	path('docs/songs/Leaving_On_A_Jet_Plane.html', views.p65, name='Leaving_On_A_Jet_Plane'),
	path('docs/songs/Let_Her_Go.html', views.p66, name='Let_Her_Go'),
	path('docs/songs/Let_It_Be.html', views.p67, name='Let_It_Be'),
	path('docs/songs/Let_It_Go.html', views.p68, name='Let_It_Go'),
	path('docs/songs/Living_Next_Door_To_Alice.html', views.p69, name='Living_Next_Door_To_Alice'),
	path('docs/songs/Magdalena.html', views.p70, name='Magdalena'),
	path('docs/songs/Malá_Dáma.html', views.p71, name='Malá_Dáma'),
	path('docs/songs/Malování.html', views.p72, name='Malování'),
	path('docs/songs/Mamma_Mia.html', views.p73, name='Mamma_Mia'),
	path('docs/songs/Marie.html', views.p74, name='Marie'),
	path('docs/songs/Matfyzák_Na_Discu.html', views.p75, name='Matfyzák_Na_Discu'),
	path('docs/songs/Mám_Doma_Kočku.html', views.p76, name='Mám_Doma_Kočku'),
	path('docs/songs/Mám_Jizvu_Na_Rtu.html', views.p77, name='Mám_Jizvu_Na_Rtu'),
	path('docs/songs/Mikymauz.html', views.p78, name='Mikymauz'),
	path('docs/songs/Milenci_V_Texaskách.html', views.p79, name='Milenci_V_Texaskách'),
	path('docs/songs/Million_Reasons.html', views.p80, name='Million_Reasons'),
	path('docs/songs/Mimorealita.html', views.p81, name='Mimorealita'),
	path('docs/songs/Minulost.html', views.p82, name='Minulost'),
	path('docs/songs/Mrs_Robinson.html', views.p83, name='Mrs_Robinson'),
	path('docs/songs/Můj_Svět.html', views.p84, name='Můj_Svět'),
	path('docs/songs/Nagasaki_Hirošima.html', views.p85, name='Nagasaki_Hirošima'),
	path('docs/songs/Nechte_Zvony_Znít.html', views.p86, name='Nechte_Zvony_Znít'),
	path('docs/songs/Netušim.html', views.p87, name='Netušim'),
	path('docs/songs/Okno_Mé_Lásky.html', views.p88, name='Okno_Mé_Lásky'),
	path('docs/songs/On_Top_Of_The_World.html', views.p89, name='On_Top_Of_The_World'),
	path('docs/songs/Osmý_Den.html', views.p90, name='Osmý_Den'),
	path('docs/songs/Panic.html', views.p91, name='Panic'),
	path('docs/songs/Pažitka.html', views.p92, name='Pažitka'),
	path('docs/songs/Perfect.html', views.p93, name='Perfect'),
	path('docs/songs/Piano_Man.html', views.p94, name='Piano_Man'),
	path('docs/songs/Pocity.html', views.p95, name='Pocity'),
	path('docs/songs/Pohoda.html', views.p96, name='Pohoda'),
	path('docs/songs/Pompeii.html', views.p97, name='Pompeii'),
	path('docs/songs/Proklínám.html', views.p98, name='Proklínám'),
	path('docs/songs/Proměny.html', views.p99, name='Proměny'),
	path('docs/songs/Ráda_Se_Miluje.html', views.p100, name='Ráda_Se_Miluje'),
	path('docs/songs/Ring-O-Ding.html', views.p101, name='Ring-O-Ding'),
	path('docs/songs/Riptide.html', views.p102, name='Riptide'),
	path('docs/songs/Runaway_Train.html', views.p103, name='Runaway_Train'),
	path('docs/songs/Sáro.html', views.p104, name='Sáro'),
	path('docs/songs/Sbírka_Zvadlejch_Růží.html', views.p105, name='Sbírka_Zvadlejch_Růží'),
	path('docs/songs/Sbohem_Galánečko.html', views.p106, name='Sbohem_Galánečko'),
	path('docs/songs/Slzy_Tvý_Mámy.html', views.p107, name='Slzy_Tvý_Mámy'),
	path('docs/songs/Srdce_Jako_Knize_Rohan.html', views.p108, name='Srdce_Jako_Knize_Rohan'),
	path('docs/songs/Starý_Muž.html', views.p109, name='Starý_Muž'),
	path('docs/songs/Stitches.html', views.p110, name='Stitches'),
	path('docs/songs/Svaz_Českých_Bohémů.html', views.p111, name='Svaz_Českých_Bohémů'),
	path('docs/songs/Šaman.html', views.p112, name='Šaman'),
	path('docs/songs/Šrouby_A_Matice.html', views.p113, name='Šrouby_A_Matice'),
	path('docs/songs/Těšínská.html', views.p114, name='Těšínská'),
	path('docs/songs/Thinking_Out_Loud.html', views.p115, name='Thinking_Out_Loud'),
	path('docs/songs/This_Is_The_Life.html', views.p116, name='This_Is_The_Life'),
	path('docs/songs/Touha.html', views.p117, name='Touha'),
	path('docs/songs/Toulavej.html', views.p118, name='Toulavej'),
	path('docs/songs/Tři_Kříže.html', views.p119, name='Tři_Kříže'),
	path('docs/songs/Ulica.html', views.p120, name='Ulica'),
	path('docs/songs/Umbrella.html', views.p121, name='Umbrella'),
	path('docs/songs/Untitled.html', views.p122, name='Untitled'),
	path('docs/songs/Včelín.html', views.p123, name='Včelín'),
	path('docs/songs/Veď_mě_dál,_cesto_má.html', views.p124, name='Veď_mě_dál,_cesto_má'),
	path('docs/songs/Viva_La_Vida.html', views.p125, name='Viva_La_Vida'),
	path('docs/songs/Vymlácený_Entry.html', views.p126, name='Vymlácený_Entry'),
	path('docs/songs/Vymyslená.html', views.p127, name='Vymyslená'),
	path('docs/songs/V_7_25.html', views.p128, name='V_7_25'),
	path('docs/songs/V_Lese.html', views.p129, name='V_Lese'),
	path('docs/songs/Waterloo.html', views.p130, name='Waterloo'),
	path('docs/songs/When_All_Is_Said_And_Done.html', views.p131, name='When_All_Is_Said_And_Done'),
	path('docs/songs/When_Youre_Gone.html', views.p132, name='When_Youre_Gone'),
	path('docs/songs/With_Or_Without_You.html', views.p133, name='With_Or_Without_You'),
	path('docs/songs/Wonderwall.html', views.p134, name='Wonderwall'),
	path('docs/songs/Zalůbení.html', views.p135, name='Zalůbení'),
	path('docs/songs/Zanedbaný_Sex.html', views.p136, name='Zanedbaný_Sex'),
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
	path('docs/songs/Matfyzák_Na_Discu.html', views.p149, name='Matfyzák_Na_Discu'),
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

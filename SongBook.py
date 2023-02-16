#!/usr/bin/python
# -*- coding: utf-8 -*-

# Class to control Tomas songbook
from calendar import c
import urllib.request
import os
import re
from pathlib import Path


class SongBook:
    def __init__(self,songsDir,songBookTex):
        '''initialization function -- load all songs, give info about song book'''

        self.songsDir = songsDir
        self.songBookTex = songBookTex
        self.loadSongs()
        # self.info()
    
    def loadSongs(self):
        '''load songs function -- update songs list and number of songs'''

        self.songs = []
        songsLst = os.listdir(self.songsDir)
        nSongs = len(songsLst)
        self.songsLst = []
        for i in range(nSongs):
            nazev = songsLst[i].split('.')[0]
            if (('00-title' == nazev or 'index' == nazev or 'ZZ-endsongs' == nazev)):
                pass
            else:
                self.songsLst.append(nazev)
        self.songsLst = sorted(self.songsLst)
        self.nSongs = len(self.songsLst)
    
    def info(self):
        '''give info about songbook'''

        print('Song book by Tomas\nnumber of songs: %d\nsongs: %s'%(self.nSongs,self.songsLst))
    
    def giveIntro(self):
        '''Write start of the program'''

        print('Control program for songbook by Tomas\n')
    
    def askIfQuit(self):
        '''Prepare questions on what to do'''

        wTD = (input('\nWhat you would like to do?\n'+
                            '\t["A"] Add song.\n'+ 
                            '\t["S"] Show info about songbook\n'
                            '\t["C"] Compile songbook\n'
                            '\t["O"] Open songbook\n'
                            '\t["Q"] Quit\n'
                ))
        if wTD == 'Q':
            return True
        else:
            if 'A' in wTD:
                self.addSong()
                self.createSongBook()
                self.loadSongs()
                self.info()
            elif 'S' in wTD:
                self.info()
            elif 'C' in wTD:
                self.createSongBook()
                self.loadSongs()
            elif 'O' in wTD:
                os.system('open %s.pdf'%self.songBookTex)
            else:
                print('I dont understand you')
    
    def createSongBook(self):
        '''create songbook'''
        print('\n not important stuff from here')
        os.system('./link-doc.sh %s.pdf > log'%self.songBookTex)
        os.system('texlua ./songidx.lua titleidx.sxd titleidx.sbx > log')
        # os.system('./songidx titleidx.sxd titleidx.sbx > log')
        os.system('pdflatex --shell-escape %s.tex > log'%self.songBookTex)
        os.system('texlua ./songidx.lua titleidx.sxd titleidx.sbx > log')
        # os.system('./songidx titleidx.sxd titleidx.sbx > log')
        os.system('pdflatex --shell-escape %s.tex > log'%self.songBookTex)
        print('end of not important stuff\n')

    def addSong(self):
        '''function to add song into the songbook'''

        # default parameters
        songAdded = False
        owner = ''          # default owner --->me
        firstWord = '<div class="js-store"'
        lastWord = '<'
        capo = ''
        transpose = 0
        listOfPosibilities = ['Outro','Intro','Bridge','Chorus','Verse']

        # prepare page to load
        pageStrW = input('Link for song: ')
        # page = urllib.request.urlopen(pageStrW)

        req = urllib.request.Request(
            url=pageStrW, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        page = urllib.request.urlopen(req)
        pageStr = (page.read()).decode('utf-8')


        # name of the song
        try:
            nameI = pageStr.find("tag.setTargeting('song'")
            nameIF = pageStr[nameI:].find(")")
            name = pageStr[nameI:nameI+nameIF].replace("tag.setTargeting('song'",'').split('"')[1]

            # artist
            nameI = pageStr.find("tag.setTargeting('artist',")
            nameIF = pageStr[nameI:].find(")")
            artist = pageStr[nameI:nameI+nameIF].replace("tag.setTargeting('artist',",'').split('"')[1]
        
        except:
            byArtI = pageStr.find('"byArtist": {')
            byArtE = pageStr[byArtI:].find("}")
            nameI = pageStr[byArtI:].find('"name":"')
            nameE = pageStr[nameI+byArtI+8:].find('"')
            artist = pageStr[nameI+byArtI:8+nameI+byArtI+nameE].replace('"name":"','')
            # print(artist)
            byArtI = byArtI + byArtE
            nameI = pageStr[byArtI:].find('"name":"')
            nameE = pageStr[nameI+byArtI+8:].find('"')
            name = pageStr[nameI+byArtI:8+nameI+byArtI+nameE].replace('"name":"','')
            # print(name)
            # artist = 
            # print([m.start() for m in re.finditer("}", pageStr[byArtI:])])

        # prepare raw text
        # delete bordel
        toDel = pageStr.split(' ')
        for i in range(len(toDel)):
            canWanish = True
            for pos in listOfPosibilities:
                if (pos in toDel[i]):
                    canWanish = False
            if 'quot' in toDel[i] and canWanish:
                pageStr = pageStr.replace(toDel[i],'')
        cuttedText = pageStr.replace('&','').replace('iacute;','í').replace('oacute;','ó').replace('uacute;','ú').replace('aacute;','á').replace('eacute;','é').replace('yacute;','ý').replace('scaron;','š').replace('Scaron;','Š').replace('ocirc;','o').replace('auml;','a').replace('rsquo;',"'")

        while not songAdded:            
            #find indices of the first and last Word
            zacatekI = cuttedText.find(firstWord)
            konecI = cuttedText[zacatekI+1:].find(lastWord)

            # cut the text according to data 
            myStr = cuttedText[zacatekI+1:zacatekI+konecI]
            # print(myStr,zacatekI,konecI)
            # print(myStr,cuttedText,zacatekI,konecI)
            
            # prepare lst of individual lines
            i = 0
            strHere = ''
            myStrLst = []
            while i < len(myStr)-1:
                if myStr[i] == '\\' and myStr[i+1] == 'n':
                    strHereFin = ''
                    while strHere[0] == ' ':
                        strHere = strHere[1:]
                    
                    for j in range(len(strHere)-1):
                        if not ((strHere[j] == '\\' and strHere[j+1] == 'r')or(strHere[j-1] == '\\' and strHere[j] == 'r')):
                            strHereFin += strHere[j]
                    strHereFin = strHereFin.replace('[tab]','').replace('[/tab]','')
                    myStrLst.append(strHereFin)
                    strHere = ''
                    i = i + 2
                else:
                    strHere += myStr[i]
                    i = i + 1
            myStrLst.append(strHere)
            
            # go through cycle
            finLst = []
            chordsL = False
            playingNow = False
            for i in range(len(myStrLst)):
                line = myStrLst[i]
                # print('line',line)
                lineFin = ''
                if '[ch]' in line:
                    chords = []
                    chordsI = []
                    pocitAkordy = 0
                    for j in range(len(line)):
                        if '[' == line[j] and 'c' == line[j+1]:
                            chords.append((line[j+4:j+4+line[j+4:].find('[')]))
                            chordsI.append(j-pocitAkordy*9)
                            pocitAkordy += 1
                            chordsL = True
                elif (chordsL and chords != []) or ('[:' in line):
                    pocitAkordy = 0
                    if len(line) >= chordsI[-1]:
                        for j in range(len(line)):
                            if pocitAkordy < len(chordsI):
                                if j == chordsI[pocitAkordy]:
                                    lineFin += '\\[' + chords[pocitAkordy] + ']' + line[j]
                                    pocitAkordy += 1
                                else:
                                    lineFin += line[j]
                            else:
                                lineFin += line[j]
                    else:
                        for j in range(chordsI[-1]+10):
                            if pocitAkordy < len(chords):
                                if j == chordsI[pocitAkordy]:
                                    if len(line) > j:
                                        lineFin += '\\[' + chords[pocitAkordy] + ']' + line[j]
                                    else:
                                        lineFin += '\\[' + chords[pocitAkordy] + ']' 
                                    pocitAkordy += 1
                                else:
                                    if len(line) > j:
                                        lineFin += line[j]
                                    else:
                                        lineFin += ' '
                            else:
                                lineFin += ' '
                    chordsL = False
                    lineFin = lineFin + '\\brk'
                elif 'Verse' in line:
                    if playingNow != False:
                        if playingNow == 'verse':
                            lineFin = '\\endverse\n\\beginverse'
                        elif playingNow == 'chorus':
                            lineFin = '\\endchorus\n\\beginverse'
                        else:
                            lineFin = '}\\endverse\n\\beginverse'
                    else:
                        lineFin = '\\beginverse'
                    playingNow = 'verse'
                
                elif 'Chorus' in line:
                    if playingNow != False:
                        if playingNow == 'verse':
                            lineFin = '\\endverse\n\\beginchorus'
                        elif playingNow == 'chorus':
                            lineFin = '\\endchorus\n\\beginchorus'
                        else:
                            lineFin = '}\\endverse\n\\beginchorus'
                    else:
                        lineFin = '\\beginchorus'
                    playingNow = 'chorus'
                
                else:
                    for posI in range(len(listOfPosibilities)):
                        if listOfPosibilities[posI] in line:
                            if playingNow != False:
                                if playingNow == 'verse':
                                    lineFin = '\\endverse\n\\beginverse*{\\nolyrics [%s]: '%listOfPosibilities[posI]
                                elif playingNow == 'chorus':
                                    lineFin = '\\endchorus\n\\beginverse*{\\nolyrics [%s]: '%listOfPosibilities[posI]
                                else:
                                    lineFin = '}\\endverse\n\\beginverse*{\\nolyrics [%s]: '%listOfPosibilities[posI]
                            else:
                                lineFin = '\\beginverse*{\\nolyrics %s: '%listOfPosibilities[posI]
                            playingNow = listOfPosibilities[posI]
                finLst.append(lineFin)
           
            # now control the chords
            finLst2 = []
            i = 0
            while i < len(finLst):
                # print(i)
                line = finLst[i].replace('&','')
                if line == '' or line == ' ' or line == 'n' or line == '\n':
                    i = i+1
                elif 'Intro' in finLst[i]:
                    buffer = ''
                    for j in range(len(finLst)-i-1):
                        if not '}' in finLst[j+i+1]:
                            buffer += finLst[j+i]
                        else:
                            break
                    finLst2.append(buffer.replace('rsquo;',"'"))
                    i = i + j
                else:
                    finLst2.append(line.replace('rsquo;',"'"))
                    i = i + 1
        

            finLst = finLst2

            charLst = ['ě','š','č','ř','ž','ý','á','í','é','ú','ů','Ě','Š','Č','Ř','Ž','Ý','Á','Í','É','Ů','Ú']
            unicodeLst = []
            for chari in range(len(charLst)):
                # unicodeLst.append([charLst[chari], ord(charLst[chari]),u'%s'%ord(charLst[chari]).encode('utf-8')])
                # unicodeLst.append([charLst[chari], str(charLst[chari].encode('unicode_escape')).replace("b'\\\\",'\\').replace("'",'')])
                # print(str(charLst[chari]),str(charLst[chari].encode('unicode_escape')).replace("b'\\\\",'\\').replace("'",'').replace('x','u00'))
                jak = str(charLst[chari])
                co = str(charLst[chari].encode('unicode_escape')).replace("b'\\\\",'\\').replace("'",'').replace('x','u00')
                artist = artist.replace(co,jak)
                name = name.replace(co,jak)
                nameF = name.replace(co,jak)


                
                # artist = artist.replace(str(charLst[chari].encode('unicode_escape')).replace("b'\\\\",'\\').replace("'",''),)
            #     artist = artist.replace('%'%uni,unichr(i))
            #     name = name.replace('\\u00ed','í').replace('\\u00e1','á').replace('\\u00fa','ů').replace('\\u0159','ř').replace('\\u0161','š')
            #     nameF = name.replace('\\u00ed','i').replace('\\u00e1','a').replace('\\u00fa','u').replace('\\u0159','r').replace('\\u0161','s')

            # artist = str(artist.replace('\\\\','\\'))
            # artist = str(artist.decode('utf-8'))
            # artist = artist.replace('\\u00ed','í').replace('\\u00e1','á').replace('\\u00fa','ů').replace('\\u0159','ř').replace('\\u0161','š')
            # name = name.replace('\\u00ed','í').replace('\\u00e1','á').replace('\\u00fa','ů').replace('\\u0159','ř').replace('\\u0161','š')
            # nameF = name.replace('\\u00ed','i').replace('\\u00e1','a').replace('\\u00fa','u').replace('\\u0159','r').replace('\\u0161','s')

            print('\nI have prepared song %s by %s, capo %s'%(name,artist,capo))
            print('First line = %s\nPre-Last line = %s\nLast line = %s\nowner = %s'%(finLst[0],finLst[-2],finLst[-1],owner))
            
            wTD = input('Do you want to change:'  
                            + '\n\t["1"]. word' 
                            + '\n\t["l"]. (last) word' 
                            + '\n\t["s"] name of the song' 
                            + '\n\t["i"] name of the author/interpret' 
                            + '\n\t["c"] capo'
                            + '\n\t["t"] transpose'
                            + '\n\t["o"] owner'
                            + '\nor ["n"] nothing?')
            if wTD == 'n':
                with open(Path(self.songsDir).joinpath(owner,nameF.replace(' ','_')+".tex"),'w') as fl:
                    fl.writelines('\\sclearpage')
                    fl.writelines('\\beginsong{%s}[by={%s}]\n'%(name,artist))
                    if playingNow == False:
                        fl.writelines('\\beginverse')
                        playingNow = 'verse'
                    if not capo == '':
                        fl.writelines('\\capo{%s}\n'%capo)
                    if not transpose == 0:
                        fl.writelines('\\transpose{%d}\n'%transpose)
                    for i in range(len(finLst)):
                        fl.writelines(finLst[i]+'\n')
                    if playingNow == 'verse' or playingNow == 'chorus':
                        fl.writelines('\\end%s'%playingNow)
                    else:
                        fl.writelines('}\\endverse')
                    fl.writelines('\\endsong')
                songAdded = True
            else:
                if '1' in wTD:
                    firstWord = input('Write the first word: ')
                if 'l' in wTD:
                    lastWord = input('Write the last word: ')
                if 's' in wTD:
                    name = input('Write name of the song: ')
                if 'i' in wTD:
                    artist = input('Write interpret/author of the song: ')
                if 'c' in wTD:
                    capo = input('Write capo: ')
                if 't' in wTD:
                    transpose = int(input('Write transposition: '))
                if 'o' in wTD:
                    ownS = (input('Write owner ("H"onzik, "D"omca or "L"ucka): '))
                    if 'H' in ownS:
                        owner = 'ŽŽ_HonzikSongs/' 
                    elif 'D' in ownS:
                        owner = 'ŽŽ_DomcaSongs/' 
                    elif 'L' in ownS:
                        owner = 'ŽŽ_LuckaSongs/' 


    def createHTML(self,htmlDir):
        # prepare headers
        # my be eventually moved to a file
        htmlHead = r'''<!DOCTYPE html>
            <html lang="en">

            <head>
            <title>\1</title>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="../style.css">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <script src="../transpose.js"></script>
            </head>
            <body>
            <div class="song">
            <div id="control">
            <div id ="return">
            <a href="../index.html">Index</a>
            </div>
            <div id="trans_control">
            <button onclick="transpose(+1)">Transpose +1</button><br>
            <div class="trans" id="trans" style="text-align:center">0</div><br>
            <button onclick="transpose(-1)">Transpose -1</button>
            </div>
            </div>

            '''

        htmlDir = Path(htmlDir)

        if not htmlDir.joinpath("songs").exists():
            print(f"Creating new directory: {htmlDir}")
            os.makedirs(htmlDir.joinpath("songs"),exist_ok=True)

        with open(htmlDir.joinpath("index.html"),"w", encoding='utf-8') as index:
            index.write('''<!DOCTYPE html>
                <html lang="en">
                <head>
                <link rel="stylesheet" href="./style.css">
                <title>Tomíkův zpěvník</title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                </head>
                <body>
                <h2 style="text-align:center">Tomíkův zpěvník</h3>
                <h3 style="text-align:center">&#127925; Seznam písniček &#127925;</h3>
                <div class="list_container">
                <div class="song_list">
                '''
            )
            #Convert all songs to html 
            songCount = 0
            print("Converting songs...")
            for songFile in self.songsLst:
                try:
                    with open(Path(self.songsDir).joinpath(f"{songFile}.tex"),"r", encoding='utf-8') as tex:
                        content=tex.read()

                    content = re.sub(r'\\beginverse', '<p class="verse"><br>', content)
                    content = re.sub(r'\\endverse', '</p class="verse">', content)
                    content = re.sub(r'\\sclearpage\\beginsong{(.*)}\[by={(.*)}\]', htmlHead+r'<h1 id="song_name">\1</h1>\n<h3 id="author">\2</h3><div class="songtext"><div class="song_container">', content,1)
                    content = re.sub(r'\\\[(.)(#*)([^\]]*)\]',r'<span class="chord" tone="\1\2" type="\3"><span class="innerchord">\1\2\3</span></span>',content)
                    content = re.sub(r'\\brk',r'<br>',content)
                    content += "</div></div></div></body></html>"
                    content = re.sub(r'\\beginchorus', '<p class="chorus"><br>', content)
                    content = re.sub(r'\\endchorus', '</p class ="chorus">', content)
                    content = re.sub(r'\\capo{([^}]*)}', r'<div id="capo">CAPO \1 </div>', content)
                    content = re.sub(r'{\\nolyrics([^}]*)}', r'<span class="nolyrics">\1</span>', content)
                    content = re.sub(r'\\endsong', '', content)

                    with open(htmlDir.joinpath("songs",f"{songFile}.html"),"w", encoding='utf-8') as html:
                        html.write(content)

                    index.write(f'<p class="song_ref"><a href="./songs/{songFile}.html">{re.sub("_"," ",songFile)}</a></p>\n')

                    songCount +=1
                except FileNotFoundError:
                    print(f"Song not found: {songFile}")

            index.write("</div></div></body></html>")

            print(f"{songCount} songs converted to html")


# if ran separately, launch songbook
if __name__ == "__main__":
    songsDir = './songs/'
    songBookTex = 'Songbook'

    # create song book
    songBook = SongBook(songsDir,songBookTex)

    # introduction
    songBook.giveIntro()
    while True:
        if songBook.askIfQuit():
            break
    
    songBook.createHTML("docs")
    # songBook.createSongBook()
    # songBook.addSong()
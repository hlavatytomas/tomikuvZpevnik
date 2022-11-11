from SongBook import *

songsDir = './songs/'
songBookTex = 'Songbook'

# create song book
songBook = SongBook(songsDir,songBookTex)

# introduction
songBook.giveIntro()
while True:
    if songBook.askIfQuit():
        break
# songBook.createSongBook()
# songBook.addSong()
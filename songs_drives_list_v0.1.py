import os
import vlc
import webbrowser as wr
path = ""
songs = []
dirs = []
dcounts = []
scounts = []
p = vlc.MediaPlayer(" ", 'r');
p.play();
def dirList(c):
    global dcounts;
    global path;
    x = 1
    for z in os.listdir(c):
        print x, z
        dirs.append(z)
        dcounts.append(x)
        x += 1
    dno = input("Enter directory number to open ")
    if dno in dcounts:
        print '\nOpening {'+ dirs[dno-1] +'}\n'
        dirList(path+dirs[dno-1]+'\\')
    main()
def songList(pathc):
    co = 1
    for i in os.listdir(pathc):
        if '.mp3' in i:
            print co, i
            songs.append(i)
            scounts.append(co)
            co += 1
    if len(scounts) == 0:
        print "Empty"
    else:
        songno = input("Enter song no. to play")
        if songno in scounts:
            playSongs(pathc+songs[songno-1])
    main()

def playSongs(songname):
    if ".mp3" in songname:
        global p
        p.stop();
        p = vlc.MediaPlayer(songname, 'r')
        print "\nPlaying {"+songname +'}\n'
        emptyAll()
        p.play()
    else:
        wr.open(songname)

def emptyAll():
    del songs[:]
    del scounts[:]
    del dirs[:]
    del dcounts[:]

    
def main():
    global path
    drives_name = [chr(d_name) + "" for d_name in range(65,90)
                   if os.path.exists(chr(d_name)+":")]
    getPath = raw_input('  '.join(map(str, drives_name)))
    path = getPath.upper()+":\\"
    for i in os.listdir(path):
        if '.mp3' in i:
            pass
        else:
            dirs.append(i)
    ls = input("1)songs \n2)open directories\n")
    if ls == 1:
        songList(path)

    if ls == 2:
        dirList(path)
main()

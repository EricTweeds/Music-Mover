import os
import shutil
inputName = "Music"
outputName = "Songs"

def MusicGetter(inputName,outputName):
    music = os.listdir() #TODO: Make this a user input location
    #TODO: user input destination, incorporate that below as well
    records = []
    singers = []
    allSongs = []
    count = 0 #TODO: Make this only count ones successfully copied

    for folder in music:
        if os.path.isdir(folder) and folder == inputName:
            artists = os.listdir(folder)
            for artist in artists:
                artist = folder + "/" + artist
                singers.append(artist)

    for artist in singers:
        if os.path.isdir(artist):
            albums = os.listdir(artist)
            for album in albums:
                album = artist + "/" + album
                records.append(album)

        else:
            #checks for music file in improper location
            print("ERROR Unexpected location for file:", artist)
            allSongs.append(artist)

    for album in records:
        if os.path.isdir(album):
            songs = os.listdir(album)
            #print (songs)
            for song in songs:
                song = album + "/" + song
                allSongs.append(song)
        else:
            #checks for music file in improper location
            print("ERROR Unexpected location for file:", album)
            allSongs.append(album)

    for song in allSongs:
        #print (song)
        if ".m4a" in song:
            try:
                shutil.copy(song, outputName) #TODO: Check file type
            except OSError as err:
                #Prevents crash when running the code twice in a row
                print("OS error: {0}".format(err))
            else:
                count += 1
        else:
            print(song, "is not an audio file")

    print (count, "songs were moved")
    print ("Complete")

def fileGetter(cfolder, files):
    """
    :param cfolder: directory
    :param files: array[string]
    :return: array[string]
    """
    directory = os.listdir(cfolder)
    for item in directory:
        if os.path.isdir(cfolder+"/"+item):
            fileGetter(cfolder+"/"+item, files)
        else:
            files.append(item)
    return files

if __name__ == '__main__':
    #MusicGetter(inputName, outputName)
    array = []
    print(fileGetter(inputName, array))


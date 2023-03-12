# mp3 플레이어 클래스 만들고 노래 등록 후 재생
import random
from time import sleep


class Player:
    def __init__(self):
        self.songList = []
        self.isLoop = False

    def addSong(self, song):
        self.songList.append(song)

    def play(self):
        cnt = 0
        if self.isLoop:
            while self.isLoop:
                for song in self.songList:
                    cnt += 1
                    song.printSongInfo()
                    sleep(song.time)

                self.setIsLoop(int(input('반복 (1), 종료 (0) : ')))

        else:
            for song in self.songList:
                song.printSongInfo()
                sleep(song.time)

    def suffle(self):
        random.shuffle(self.songList)

    def setIsLoop(self, loop):
        self.isLoop = loop


class Song:

    def __init__(self, title, singer, time):
        self.title = title
        self.siger = singer
        self.time = time

    def printSongInfo(self):
        print(f'{self.title} - {self.siger} [{self.time}]')


s1 = Song('Butterfly', 'Numcha', 4)
s2 = Song('Youth', 'Jade', 3)
s3 = Song('slam', '10-FEET', 4)
s4 = Song('Weekend', 'TAEYEON', 3)
s5 = Song('Ditto', '뉴진스', 2)

player = Player()
player.addSong(s1)
player.addSong(s2)
player.addSong(s3)
player.addSong(s4)
player.addSong(s5)

player.setIsLoop(True)
player.suffle()
player.play()

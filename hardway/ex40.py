class Song(object):
    def __init__(self, title, author, lyrics):
        self.title = title
        self.author = author
        self.lyrics = lyrics
    
    def sing(self):
        print(f"{self.title} - {self.author}")
        print('-'*20)
        for line in self.lyrics:
            print(line)
        print()


lyrics_welcome_home = [
    "Welcome to where time stands still",
    "No one lives, no one will",
    "Moon is full, never seems to change",
]

lyrics_kanade = [
    "Aisatsu no mae tsunagu te to te",
    "itsumono zawameki, atarashii kaze",
    "akaruku miokuru, hazu datta no ni",
    "umaku waraezu ni, kimi wo miteita",
]

welcome_home = Song("Welcome Home", "Metallica", lyrics_welcome_home)
kanade = Song("Kanade", "Sukima Switch", lyrics_kanade)
welcome_home.sing()
kanade.sing()
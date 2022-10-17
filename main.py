class Artist:
    def __init__(self,namn:str):
        self.__Namn = namn
        self.__Album = []
    def AddAlbum(self, album):
        self.__Album.append(album)
    # def CreateAlbum(self, albumname, albumreleaseyear ):
    #     self.__Album.append(Album(albumname,albumreleaseyear))
class Album:
    def __init__(self,namn:str, year:int):
        self.__Namn = namn
        self.__Year = year
        self.__Songs = []
    def AddSong(self, song):
        self.__Songs.append(song)
    def GetTotalLength(self):
        summa = 0
        for song in self.__Songs:
            summa = summa + song.GetLength()
        return summa
class Song:
    def __init__(self,namn:str, length:int):
        self.__Namn = namn
        self.__Length = length
    def GetLength(self):
        return self.__Length

art = Artist("Stefan")
#art.CreateAlbum("Sånger från Pythonskogen", 1980)
album1 = Album("Sånger från Pythonskogen", 1980)
art.AddAlbum(album1)
album2 = Album("Hej hopp", 1990)
art.AddAlbum(album2)

song1 = Song("Song1", 12)
album1.AddSong(song1)
song2 = Song("Song2", 11)
album1.AddSong(song2)
album2.AddSong(song2)
song3 = Song("Song3", 13)
album2.AddSong(song3)

print(art)


#Raise own Exceptions
# (usecase - def __init__ )
# usecase SetAge(self, int)
def CalculateSalary(hourlySalary:int, hoursWorked:int ) -> int:
    if hoursWorked < 0:
        raise ValueError("Hours worked cant be less than 0")
    salary = hourlySalary * hoursWorked
    if hoursWorked > 10:
        salary = salary * 1.2
    return salary

try:
    a = CalculateSalary(10,-5)
    print(a)
except ValueError:
    print("dsda")




while True:
    try:
        tal1Input = input("Ange tal 1:")
        tal1 = int(tal1Input)
        tal2Input = input("Ange tal 2:")
        tal2 = int(tal2Input)
        tal3 = tal1 / tal2
        print(tal3)
        break
    except ValueError:
        print("Verkar inte vara ett tal")
    except ZeroDivisionError:
        print("Tal2 får inte vara 0")
    except:
        print("Ngt jätteknas - mail skickat till utvecklaren så ska den få pisk!")

# while True:
#     try:
#         tal1Input = input("Ange tal 1:")
#         tal1 = int(tal1Input)
#         break
#     except:
#         print("Ange siffror tack")


# while True:
#     try:
#         tal2Input = input("Ange tal 2:")
#         tal2 = int(tal2Input)
#         break
#     except:
#         print("Ange siffror tack")

# try:
#     tal3 = tal1 / tal2
#     print(tal3)
# except:    
#     print("Ngt fick fel")

from pprint import pprint

class Garba:
    def __init__(self, dancer_name, age, experience_level, favorite_song, costume_color, team_name):
        self.__dancer_name = dancer_name
        self.__age = age
        self.__experience_level = experience_level
        self.__favorite_song = favorite_song
        self.__costume_color = costume_color
        self.__team_name = team_name

    @property
    def dancer_name(self) -> str:
        return self.__dancer_name
    
    @property
    def age(self) -> int:
        return self.__age
    
    @property
    def experience_level(self) -> str:
        return self.__experience_level
    
    @property
    def favorite_song(self) -> str:
        return self.__favorite_song
    
    @property
    def costume_color(self) -> str:
        return self.__costume_color
    
    @property
    def team_name(self) -> str:
        return self.__team_name
    
    @team_name.deleter
    def team_name(self) -> None:
        del self.__team_name
    
team = Garba("Arin", 20, "Professional", "Maro Chand", "White", "Disco Garba")

# print(team.__dict__)
pprint(team.__dict__)   # it only shows the used made attributes

pprint(Garba.__dict__)  # it shows the class attributes and methods

del team.team_name
pprint(team.__dict__)  # it shows the class attributes and methods

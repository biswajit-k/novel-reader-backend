from enum import Enum


# Novel
class NovelStatus(Enum):
    ONGOING = 'ongoing'
    COMPLETED = 'completed'
    DROPPED = 'dropped'

class NovelType(Enum):
    MANGA = 'manga'
    WEB_NOVEL = 'web novel'
    MANHWA = 'manhwa'
    COMIC = 'comic'

class NovelGenre(Enum):
    ACTION = "action"
    ADVENTURE = "adventure"
    ROMANCE = "romance"
    FANTASY = "fantasy"
    COMEDY = "comedy"
    SCI_FI = "sci-fi"
from enum import Enum


class MusicState(Enum):
    STOPPED = 0
    PLAYING = 1
    SWITCHING = 2
    PAUSED = 3
    DEAD = 4


class EntryState(Enum):
    PROCESSING = 0
    DOWNLOADED = 1
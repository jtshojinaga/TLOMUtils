from enum import Enum

class Mutations(Enum):
    # name - value
    # 'name' is what displays on discord
    # WARNING: if the names here do not match EXACTLY what
    # is in the config.json file, it will not work!
    # the value here can be anything though
    all = "all"
    albinism = "albinism"
    melanism = "melanism"
    piebaldism = "piebaldism"
    leucism = "leucism"
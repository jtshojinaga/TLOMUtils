from enum import Enum
class Mutations(Enum): # The values as a percentage. I.E, 10.0 = 10%
    # They CANNOT have the same value!
    leucism = 2.0 # Default: 2.0
    piebaldism = 5.0 # Default: 5.0
    albinism = 10.0 # Default: 10.0
    melanism = 10.5 # Default: 10.5
    all = 0.0
    #test = 100.0

class AllowedSpecies(Enum):
    deinosuchus = 1
    kaprosuchus = 2
    dracoviper = 3
    dominus = 4
    golugore = 5
    andrewsarchus = 6
    madrehorn = 7
    mammuthus = 8
    cerataspida = 9
    bonapartenykus = 10
    citipati = 11
    halszkaraptor = 12
    ocepechelon = 13
    noviana = 14
    moraquile = 15
    glowplume = 16
    thalasrex = 17
    nyctatyrannus = 18
    ankylorhiza = 19
    helicoprion = 20
    megalania = 21
    ophis = 22
    smilodon = 23
    griffin = 24
    lisowicia = 25
    dimetrodon = 26
    diplocaulus = 27
    salamander = 28
    hibbertopterus = 29
    xiphactinus = 30
    archelon = 31
    livyatan = 32
    inostrancevia = 33
    squalicorax = 34

class Conditions(Enum):
    dwarfism = 0.6 # Default: 0.6
    immune_deficiency = 0.7 # Default: 0.7
    blindness = 1.0 # Default: 1.0
    deafness = 1.1 # Default: 1.1
    muscular_weakness = 1.2 # Default: 1.2
    hypersomnia = 5.0 # Default: 5.0
    asthma = 7.0 # Default: 7.0
    infertility = 10.0 # Default: 10.0
    severe_allergy = 12.0 # Default: 12.0
    chronic_pain = 14.0 # Default: 14.0
    insomnia = 15.0 # Default: 15.0
    colorblindness = 18.0 # Default: 18.0
    severe_phobia = 20.0 # Default: 20.0
    #example_condition = 100.0
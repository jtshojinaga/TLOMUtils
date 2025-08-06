from enum import Enum
class Mutations(Enum): # The values as a percentage. I.E, 10.0 = 10%
    # They CANNOT have the same value!
    leucism = 10.0 # Default: 10.0
    piebaldism = 12.0 # Default: 12.0
    albinism = 15.0 # Default: 15.0
    melanism = 15.5 # Default: 15.5
    all = 0.0
    #test = 100.0

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

class Illnesses(Enum):
    Chronic_Wasting_Disease = 0.8
    rabies = 0.9
    haemorrhagic_fever = 1.0
    amoebiasis = 2.0
    anaplasmosis = 4.0
    meningitis = 5.0
    pneumonia = 7.0
    influenza = 10.0
    rain_rot = 12.0
    the_common_cold = 25.0
    #The_Black_Plague = 100.0

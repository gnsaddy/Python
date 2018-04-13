def dc_marvel(input_list):
    input_list = ['Dark claw', 'Hyena']
    return input_list


hero_villian = ['Batman', 'Joker', 'Volverine', 'Sabertooth']
dc_marvel(hero_villian)
print("DC & Marvel_Superhero & Villian:")
print(hero_villian)
print(dc_marvel(hero_villian))

''' Both the list are pointing to different object reference.
Function used PASS BY REFERENCE Methodology i.e
call by reference object'''

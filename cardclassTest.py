class Card:
    def __init__(card, name, creaturetype, creatureclass1, creatureclass2, desc, attack, defence, alignment):
        card.name = name
        card.creaturetype = creaturetype
        card.creatureclass1 = creatureclass1
        card.creatureclass2 = creatureclass2
        card.desc = desc
        card.attack = attack
        card.defence = defence
        card.alignment = alignment

kknight = Card("K-Knight",
               "Light",
               "Good Boi",
               "Warrior",
               "K-Knight is the latest in a long line of pedigree servants to the forces of good. Revered by many as the very best of bois, K-Knight's loyality to the cause of defending peace, justice and his favourite squeaker toy is unyielding.",
               1800,
               2000,
               3000)

armgenthippo = Card("Armoured Gentleman Hippo",
                    "Light",
                    "Noble",
                    "Warrior",
                    "Both gentleman and physical embodiment of might, this noble beast gives his all to defending chivalry and those less mighty than himself.",
                    3000,
                    3500,
                    2000)

bushmaster = Card("Bush Master",
                    "Dark",
                    "Sorcerer",
                    "Ninja",
                    "A living shadow and master of sorcery, Bush Master may be small, but do not dismiss him as weak, lest you meet with swift end by his hand.",
                    2000,
                    500,
                    50)

bearceo = Card("Bear CEO",
                    "Business",
                    "Boss",
                    "Warrior",
                    "It's no small task climbing to the top of the corporate ladder, and it's a task made no smaller by being the mother of two mischievous cubs. Bear CEO, however, has taken that and more in her stride to become the most influential business person in the land.",
                    3500,
                    3000,
                    1000)

salamanager = Card("Salamanager",
                    "Business",
                    "Boss",
                    "",
                    "Amphibious Ltd may not be a leading organisation, but it's one that Salamanager has built up from nothing, and as such, he's extremely proud of it. It's for this reason and many others that he has refused countless buy-out proposals from Bear CEO (not least because she insists on paying him in salmon).",
                    500,
                    200,
                    1400)

tarantulunch = Card("Tarantulunch",
                    "Bug",
                    "Arachnid",
                    "Food",
                    "A gruesome abonimation of tarantula and burger, for whose existance the one responsible probably ought to be severely punished.",
                    500,
                    200,
                    1400)



print(kknight.desc)
print(armgenthippo.alignment)
print(armgenthippo.name)

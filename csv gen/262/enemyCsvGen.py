from random import randint

name = """Bobby
Archimbald
Steven
Logan
Garen
Dondre
Balthassar
Waller
Brendan
Harper
Edmund
Valerius
Emerson
Torben
Noreis
Hayo
Laurenz
Lauryn
Ulli
Hadley
Tinchen
Armine
Liliane
Brielle
Jacey
Damaris
Laetitia
Allesha
Gisela
Collette
Kasandra
Kristiane
Arabela
Terrill
Valere
Igor
Ivan"""
adjective="""giant
agile
evil
wretched
vengeful
diabolical
dreaded
gloomy
colossal
crimson
putrid
dreadful
cursed
devilish
bloody
bone
old
elder
hairy
undead
grisly
bloodthirsty
wailing
howling
horrible
enraged
putrid"""

job="""knight
witch
warlock
wizard
butcher
lord
captain
cannibal
king
ghost
troll
goblin
sprite
cyclops
orc
dragon
ogre
pest
zombie
hybrid
gremling
skeleton
hag
behemoth
vampire"""

creature="""warthog
creature
dragon
ogre
spider
bat
cyclops
orc
sprite
demon 
leech
centar
goblin
pest
snake
vulture
troll
giant
mole
zombie
ghost
feind
scorpian
gremling
skeleton
yak
wailer
figure
howler
hag
behemoth
vampire
gargole
phaseling
acidling
bloodling
wretchling
vengeling
devilling
dreadling
gloomling
boneling
razorling
cavernling
horrorling
sorrowling
crownling
tranceling
phasespawn
acidspawn
bloodspawn
spawn
pest
vengespawn
devilspawn
dreadspawn
gloomspawn
bonespawn
razorpest
cavernspawn
bloodbeast
vengebeast
razorbeast
cavern beast
horrorbeast
beast
bloodseeker
boneseeker"""

def enemyGen(size):
    #2 kinds of name gen
    #name gen 1: [creature] (bloodbeast) (creature)
    #name gen 1.1: [adjective] [creature]
    #name gen 2: [name] the [job] (Igor the Evil) (name/job)
    #name gen 2.1: [name] the [adjective]  (Igor the Evil) (name/adjective)
    #name gen 2.2: [name] the [job]  (Igor the King) (name/job)
    #name gen 2.3: [name] the [adjective] [job]  (Igor the Evil King) (name/adjective/job)
    #name gen 3: the [adjectve] [job] (the evil knight)
    altGenFormat = "{} the {}"
    ret = "Name,Description,Health,Attack,Defense,Nocturnal?"
    retCount = 0
    while retCount<size:
        ret+='\n'
        #namegen
        randGen=randint(1, 3)
        if randGen==1:
            ret=ret+creatureGen()
        if randGen==2:
            ret=ret+personGen()
        if randGen==3:
            ret=ret+'the '+ adjectiveGen() + ' ' + jobGen()
        #description
        ret=ret+','
        #health
        ret = ret + ',' + str(randint(50,150))
        #attack
        ret = ret + ',' + str(randint(5,15))
        #defense
        ret = ret + ',' + str(randint(0,10))
        #nocturnal
        if randGen == 2:
            ret = ret + ',' + 'false'
        else:
            ret = ret + ',' + 'true'
        retCount=retCount+1
    return ret

def creatureGen():
    creatureArr=creature.split('\n')
    if randint(1,2)==1:
        return adjectiveGen() +' ' + creatureArr[randint(0,len(creatureArr)-1)]
    return creatureArr[randint(0, len(creatureArr)-1)]

def jobGen():
    jobArr=job.split('\n')
    ret = ''
    if randint(1,2)==1:
        return adjectiveGen() +' ' + jobArr[randint(0,len(jobArr)-1)]
    return jobArr[randint(0,len(jobArr)-1)]

def adjectiveGen():
    adjectiveArr=adjective.split('\n')
    return adjectiveArr[randint(0,len(adjectiveArr)-1)]

def personGen():
    nameArr = name.split('\n')
    if randint(1,2)==1:
        return  nameArr[randint(0,len(nameArr)-1)] + ' the ' + jobGen()
    return nameArr[randint(0,len(nameArr)-1)] + ' the ' + adjectiveGen() 


print(enemyGen(20))
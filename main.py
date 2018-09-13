from random import random, randint, uniform, shuffle, choice
from time import sleep
import winsound
fitness = 0
donebefore = []
donebeforefit = []
def fit(element,expected):
    returner = 0
    dur = 250
    correspondence1=['LE', 'LF', 'LG', 'LA', 'LB', 'C', 'D', 'E', 'F', 'G', 'HA', 'HB', 'HC', 'HD']
    correspondence2=[165, 175, 196, 220, 247, 262, 294, 330, 349, 392, 440, 494, 523, 587]
    if element not in donebefore:
        donebefore.append(element)
        a = str(element).replace("0","LB").replace("-1","LA").replace("9","HD").replace("10","HE").replace("-2","LA").replace("-3","LG").replace("-4","LF").replace("-5","LE").replace("1","C").replace("2","D").replace("3","E").replace("9","HD").replace("4","F").replace("5","G").replace("6","HA").replace("7","HB").replace("8","HC")[1:-1]
        a = a.split(", ")
        for noter in a:
            freq=correspondence2[correspondence1.index(noter)]
            winsound.Beep(freq,dur)
            sleep(0.05)
        
        returner = (int(input("How much do you like this music, on a scale of 1-10?")) / 10)
        fitness = returner
        donebeforefit.append(fitness)
        return returner
    else:
        return donebeforefit[donebefore.index(element)]

def generateIndividual():        #fine
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    ind = []
    for i in range(0, 16):
        ind.append(choice(a))
    return ind

def generateFirstPopulation(initialsize):
    firstPop=[]
    for i in range(initialsize):
        firstPop.append(generateIndividual())
    return firstPop

def getGenPerf(pop, expected):
    popPerf = []
    for i in range(len(pop)):
        popPerf.append(fit(pop[i], expected))
    return sorted(popPerf, reverse=True)

def breedChildren(parent1, parent2):
    baby = []
    for i in range(len(parent1)):
        baby.append(int((parent1[i] + parent2[i]) / 2))
    return baby

def breedPop(pop,kids,breedamount):
    breedPop = []
    for j in range(breedamount):
        r = randint(0, len(pop)-1)
        r2 = randint(0, len(pop)-1)
        for i in range(kids):
            breedPop.append(breedChildren(pop[r], pop[r2]))
    return breedPop
def select(luckies,best,pop,expected):

    selected = []
    alreadydone = []
    for i in range(luckies):
        selected.append(pop[randint(0, len(pop) - 1)])
        alreadydone.append(pop[randint(0, len(pop) - 1)])
    for j in range(best):
        a = getGenPerf(pop,expected)[j] #PROBLEM: This doesn't pass the populations with the highest fitness; it passes the highest fitnesses.
        for k in range(0, len(pop)):
            if fit(pop[k],expected) == a:
                selected.append(pop[k])
                break
                    
    shuffle(selected)
    return selected
def mutate(pop, mutations):
    for ind in range(len(pop)):
        for note in range(16):
            r=randint(-1, 1)
            if(mutations / 100 > random() and pop[ind][note] + r >= -1 and pop[ind][note] + r <= 10):
                if r==-1:
                    pop[ind][note] = int(pop[ind][note] + 1)
                else:
                    pop[ind][note] = int(pop[ind][note] - 1)
    return pop
def generateNextPop(pop, luckies, best, breedamount, kids, gens, expected, mutations):
    nextpop = select(luckies, best, pop, expected)
    allah = breedPop(nextpop, kids, breedamount)
    comb = nextpop + allah
    print(mutate(comb, mutations))
    return mutate(comb, mutations)
def start(size, luckies, best, breedamount, kids, gens, expected, mutations):
    historic = []
    historic.append(generateFirstPopulation(size))
    for i in range (gens):
        donebefore = []
        donebeforefit = []
        fitness = []
        historic.append(generateNextPop(historic[i],luckies,best,breedamount,kids,gens,expected,mutations))
    return historic
#flow: 
#program
expected = 10
size = 10
luckies = 1 
best = 3
kids = 2
gens = 5000
redofitness = True
mutations = 25
breedamount = int((size-best-luckies)/kids)

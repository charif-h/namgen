import random
import SubjectiveLogic as sl

def gen(a, b):
    return random.normalvariate((a+b)/2, abs(a-b)/2)

class Individu:
    def __init__(self, name):
        self.name = name
        self.power = random.randint(0, 100)
        self.social = random.randint(0, 100)
        self.agresivity = int(min(max(random.normalvariate(self.power, random.randint(5, 50)), 0), 100))
        self.opinions = {}

    def __str__(self):
        return self.name + " [power=" + str(self.power) + "%, sociable=" + str(self.social) + "%, agresivity=" + str(self.agresivity) + "%]"

    def __repr__(self):
        return str(self.name)

    def meet(self, other):
        op = sl.Opinion(base=gen(self.social, other.social)/100)
        if other.name in self.opinions.keys():
            op = self.opinions[other.name]
        #reaction = {"pos":1 + (self.social + 0.5*other.social)/2, "neg":1 + (self.agresivity + 0.5*other.agresivity)/2}
        reaction = {"pos":op.expectedValue(), "neg":1 - op.expectedValue()}
        choix = random.choices(list(reaction.keys()), reaction.values(), k=1)[0]
        if choix == "pos" :
            #op.positive_interaction(round(reaction["neg"]/reaction["pos"] + 0.5))
            op.positive_interaction(random.normalvariate(reaction["neg"], reaction["pos"]) + 1)
        else:
            #op.negative_interaction(round(reaction["pos"] / reaction["neg"] + 0.5))
            op.negative_interaction(random.normalvariate(reaction["pos"], reaction["neg"]) + 1)
        self.opinions[other.name] = op

        action = random.choices(["love", "fight", "null"],
                                (self.social*op.expectedValue(), self.agresivity*(1-op.expectedValue()), op.uncertainity()),
                                k=1)[0]
        print(self.name, action, other.name)

        #trans = random.sample(list(other.opinions.keys()), random.randint(len(other.opinions.keys())))
        #print(trans)


def meet(i1, i2):
    if i1.name != i2.name:
        i1.meet(i2)
        i2.meet(i1)
        print(i1, i1.opinions)
        print(i2, i2.opinions)
    print()
    '''p = ["unite", "kill", "Null"]
    pu = (i1.social + i2.social)/2
    pk = (i1.agresivity + i2.agresivity)/2
    pn = max(100 - pu - pk, 0)
    choix = random.choices(p, (pu, pk, pn), k=1)[0]
    if choix == "kill":
        win = random.choices([i1, i2], weights=(i1.power, i2.power), k=1)
        return choix + ": " + str(win[0]) + " won on " + str(i1) + " " + str(i2)
    return choix + " " + str(i1) + " " + str(i2)'''

def meets(C1, C2):
    p = ["unite", "fight", "Null"]
    pu = (C1.getSocial() + C2.getSocial) / 2
    pk = (C1.getAgresivity() + C2.getAgresivity()) / 2
    pn = max(100 - pu - pk, 0)
    choix = random.choices(p, (pu, pk, pn), k=1)[0]
    if choix == "fight":
        print("**** FIGHT **** " + C1.name + " against " + C2.name)
        avp1 = C1.getAvgPower()
        avp2 = C2.getAvgPower()
        for c in C1.members:
            stdev = abs(c.power - avp1)
            chance = min(max(random.normalvariate(c.power, stdev), 0), 100)
            if(chance < avp2):
                print(c + " of the clan " + C1.name + " has been killed")
                C1.members.splice(c, 1)
        for c in C2.members:
            stdev = abs(c.power - avp2)
            chance = min(max(random.normalvariate(c.power, stdev), 0), 100)
            if (chance < avp1):
                print(c + " of the clan " + C2.name + " has been killed")
                C2.members.splice(c, 1)
    elif choix == "unite":
        print("**** UNITE **** " + C1.name + " against " + C2.name)
        C1.members.append(C2.members)



class Clan:
    def __init__(self, members, name = ""):
        self.members = members
        if name == "":
            cons = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "QU", "R", "S", "T", "V", "X", "Z"]
            voy = ["A", "E", "I", "O", "U", "Y"]
            self.name = random.choice(cons) + random.choice(voy) + random.choice(cons)

    def getSocial(self):
        s = 1
        for m in self.members:
            s = s*(1-m.social/100.0)
        return 100*(1-s)

    def getAgresivity(self):
        s = 1
        for m in self.members:
            s = s*(1-m.agresivity/100.0)
        return 100*(1-s)

    def getAvgPower(self):
        v = 0
        for m in self.members:
            v += m.power
        return v/len(self.members)
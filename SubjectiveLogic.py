class Opinion():
    def __init__(self, posint = 0, negint = 0, w=2, base = 0.5):
        self.posint = posint
        self.negint = negint
        self.w = w
        self.base = base

    def __str__(self):
        return str(self.expectedValue())[0:4]

    def __repr__(self):
        return str(self.expectedValue())[0:4]
               #+ " [" + str(self.believe()) + ", " + str(self.disbelieve()) + ", " + str(self.uncertainity()) + "]"

    def believe(self):
        return self.posint/(self.posint + self.negint + self.w)

    def disbelieve(self):
        return self.negint/(self.posint + self.negint + self.w)

    def uncertainity(self):
        return self.w/(self.posint + self.negint + self.w)

    def expectedValue(self):
        return self.believe() + self.base*self.uncertainity()

    def positive_interaction(self, p = 1):
        self.posint += p

    def negative_interaction(self, n = 1):
        self.negint += n
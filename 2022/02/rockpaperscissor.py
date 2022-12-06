class RPS:
    OP_ROCK = "A"
    OP_PAPER = "B"
    OP_SCISSOR = "C"
    ME_ROCK = "X"
    ME_PAPER = "Y"
    ME_SCISSOR = "Z"
    P_ROCK = 1
    P_PAPER = 2
    P_SCISSOR = 3

    def __init__(self, opponent, me):
        self.__opponent = opponent
        self.__me = me

    def __base_score(self, me):
        p = 0
        if (me == self.ME_ROCK and self.__opponent == self.OP_SCISSOR) or (me == self.ME_PAPER and self.__opponent == self.OP_ROCK) or (me == self.ME_SCISSOR and self.__opponent == self.OP_PAPER):
            p = 6
        elif (me == self.ME_ROCK and self.__opponent == self.OP_ROCK) or (me == self.ME_PAPER and self.__opponent == self.OP_PAPER) or (me == self.ME_SCISSOR and self.__opponent == self.OP_SCISSOR):
            p = 3
        return p

    def score_one(self):
        p = self.__base_score(self.__me)
        if self.__me == self.ME_ROCK:
            p = p + self.P_ROCK
        elif self.__me == self.ME_PAPER:
            p = p + self.P_PAPER
        elif self.__me == self.ME_SCISSOR:
            p = p + self.P_SCISSOR

        return p


    def __decide_move(self):
        me = self.ME_ROCK

        if self.__me == self.ME_ROCK:
            if self.__opponent == self.OP_ROCK:
                me = self.ME_SCISSOR
            elif self.__opponent == self.OP_SCISSOR:
                me = self.ME_PAPER
        elif self.__me == self.ME_PAPER:
            if self.__opponent == self.OP_SCISSOR:
                me = self.ME_SCISSOR
            elif self.__opponent == self.OP_PAPER:
                me = self.ME_PAPER
        elif self.__me == self.ME_SCISSOR:
            if self.__opponent == self.OP_ROCK:
                me = self.ME_PAPER
            elif self.__opponent == self.OP_PAPER:
                me = self.ME_SCISSOR

        return me

    def score_two(self):
        me = self.__decide_move()
        p = self.__base_score(me)

        if me == self.ME_ROCK:
            p = p + self.P_ROCK
        elif me == self.ME_PAPER:
            p = p + self.P_PAPER
        elif me == self.ME_SCISSOR:
            p = p + self.P_SCISSOR

        return p

    def __repr__(self):
        return '[{} vs {}]'.format(self.__opponent, self.__me)

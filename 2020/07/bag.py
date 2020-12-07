class Bag:
    def __init__(self, color):
        self.__color = color
        self.__can_contain = []

    def get_color(self):
        return self.__color

    def has_shiny_gold_bag(self):
        for b in self.__can_contain:
            if 'shiny gold' in b:
                return True
        return False

    def contain_other_bags(self):
        if len(self.__can_contain) == 0:
            return False
        return True

    def add_contained_bag(self, c, a):
        contained_bag = {}
        contained_bag[c] = a
        self.__can_contain.append(contained_bag)

    def __repr__(self):
        return 'Color: {}, contains {}'.format(self.__color, self.__can_contain)

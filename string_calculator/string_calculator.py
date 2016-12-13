from functools import reduce


class StringCalculator():

    def add(self, addends):
        if addends == "":
            return 0
        parsed_addends = self.replace_delimiter(addends)
        return self.sum(parsed_addends)

    def replace_delimiter(self, addends):
        return addends.replace("\n", ",")

    def sum(self, addends):
        return reduce(lambda x, y: x + y, self.map_to_integers(addends))

    def map_to_integers(self, addends):
        return [int(addend) for addend in addends.split(',')]

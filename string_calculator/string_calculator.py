from functools import reduce


class StringCalculator():

    def add(self, addends):
        parsed_addends = addends.replace("\n", ",")
        if parsed_addends == "":
            return 0
        addends = self.map_to_addends(parsed_addends)
        return self.calculate_sum(addends)

    def map_to_addends(self, addends):
        return [int(addend) for addend in addends.split(',')]

    def calculate_sum(self, addends):
        return reduce(lambda x, y: x + y, addends)

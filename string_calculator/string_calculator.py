class StringCalculator():

    def __init__(self, addend_payload):
        self.addend_payload = addend_payload.replace("\n",",")

    def add(self):
        if self.addend_payload == "": return 0
        addends = self.map_to_addends(self.addend_payload)
        return self.calculate_sum(addends)

    def map_to_addends(self, payload):
        return map(lambda x: int(x),payload.split(','))

    def calculate_sum(self,addends):
        return reduce(lambda x, y: x + y, addends)

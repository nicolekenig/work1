class bitwiseInverter:
    # Inverter is NOT gate
    in1 = 0
    output = 0

    def __init__(self, in1):
        self.in1 = in1

    def get_output(self):
        return ~self.in1

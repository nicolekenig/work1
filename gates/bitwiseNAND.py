class bitwiseNAN:
    in1 = 0
    in2 = 0
    output = 0

    def __init__(self, in1, in2):
        self.in1 = in1
        self.in2 = in2

    def get_output(self):
        return ~(self.in1 & self.in2)



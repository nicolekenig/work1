class OR:
    in1 = 0
    in2 = 0
    output = 0

    def __init__(self, in1, in2):
        self.in1 = in1
        self.in2 = in2

    def get_output(self):
        if (self.in1 == 1) or (self.in2 == 1):
            return 1  # True
        return 0  # False

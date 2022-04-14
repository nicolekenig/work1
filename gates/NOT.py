class NOT:
    in1 = 0
    output = 0

    def __init__(self, in1):
        self.in1 = in1

    def get_output(self):
        if self.in1 == 0:
            return 1
        else:
            return 0



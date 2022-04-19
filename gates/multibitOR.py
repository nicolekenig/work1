from gates.OR import OR


class multibitOR:
    inputs = []
    len = 0
    output = 0
    gate_name = ''

    def __init__(self, inputs, gate_name=''):
        self.gate_name = gate_name
        self.len = len(inputs)
        self.inputs = inputs
        self.calculate()

    def calculate(self):
        or_gate = OR(self.inputs[0], self.inputs[1])
        output = or_gate.get_output()
        for x in range(2, self.len):
            or_gate = OR(self.inputs[x], output)
            output = or_gate.get_output()

        self.set_output(output)

    def set_inputs(self, inputs):
        self.len = len(inputs)
        self.inputs = inputs
        self.calculate()

    def set_output(self, output):
        self.output = output

    def get_output(self):
        return self.output

    def get_gate_name(self):
        return self.gate_name




from gates.INVERTER import INVERTER
from gates.NOR import NOR
from gates.multibitOR import multibitOR


class multibitNOR:
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
        or_gate = multibitOR(self.inputs)
        out = or_gate.get_output()
        output_nor_gate = INVERTER(out).get_output()
        self.set_output(output_nor_gate)

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







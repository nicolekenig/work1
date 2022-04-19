class BUFFER:
    # Inverter is NOT gate
    in1 = 0
    output = 0
    gate_name = ''

    def __init__(self, in1, gate_name=''):
        self.gate_name = gate_name
        self.in1 = in1

    def set_inputs(self, inputs):
        self.in1 = inputs

    def get_output(self):
        return self.in1

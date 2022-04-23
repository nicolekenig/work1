from gates.BUFFER import *
from gates.INVERTER import *
from gates.multibitAND import *
from gates.multibitNAND import *
from gates.multibitNOR import *
from gates.multibitOR import *
from gates.multibitXOR import *


class dataSystem:
    '''
    the class is the system itself
    :parameter sys_id: the sys_id according to what we read in the file
    :parameter sys_i: dict of the system input and there value
    :parameter sys_o: dict of the calculated output we did
    :parameter sys_gate_outputs_dict: dict of each gate in the system. the key is the gate output name (e.g z1/o1) and the
    value is an array of [array of the gate inputs, the gate object ifself, the gate output]
    :parameter sys_comps_dict: dict of the system components
    :parameter obs_output: dict of the observation output as we read in the observation file
    '''
    sys_id = ''
    sys_i = {}  # key: i1 , val : i1 value
    sys_o = {}  # key : o1, val : o1 value
    sys_gate_outputs_dict = {}  # key: gate_output (e.g z1) , val: (inputs, actual_gate)
    sys_comps_dict = {}  # key: gate_name,   val: gate_output_name
    obs_output = {}
    compare_outs = {}

    def __init__(self, sys_id, sys_i, sys_o, rest_of_file):
        self.sys_id = sys_id
        for i in sys_i:
            self.sys_i[i] = 0
        for o in sys_o:
            self.sys_o[o] = 0
        self.build_sys(rest_of_file)

    def build_sys(self, file_as_a_string):
        '''
        the func build the system itself according to the file from line 4 and until the and of the file.
        we split the line parameters, and according to the gate name and input we build the gate, connect the inputs
        and add array of [the gate inputs, the gate object , the gate output] to sys_gate_outputs_dict
        :param file_as_a_string: the file lines from line 4 until the end
        '''
        for line in file_as_a_string:
            # line = [[nand2,gate10,z1,i1,i3],
            line = self.convert_string_to_arr(line)
            gate_type_and_num_of_input = line[0]
            gate_type = gate_type_and_num_of_input[:-1]
            num_of_input = gate_type_and_num_of_input[-1]
            gate_name = line[1]
            gate_output_name = line[2]
            gate_inputs = line[3:]
            input_to_send = self.input_value(gate_inputs)
            gate = None
            self.sys_comps_dict[gate_name] = gate_output_name
            if gate_type == 'and':
                gate = multibitAND(inputs=input_to_send, gate_name=gate_name)
            elif gate_type == 'nand':
                gate = multibitNAND(inputs=input_to_send, gate_name=gate_name)
            elif gate_type == 'or':
                gate = multibitOR(inputs=input_to_send, gate_name=gate_name)
            elif gate_type == 'nor':
                gate = multibitNOR(inputs=input_to_send, gate_name=gate_name)
            elif gate_type == 'xor':
                gate = multibitXOR(inputs=input_to_send, gate_name=gate_name)
            elif gate_type == 'inverte':
                gate = INVERTER(in1=input_to_send[0], gate_name=gate_name)
            elif gate_type == 'buffe':
                gate = BUFFER(in1=input_to_send[0], gate_name=gate_name)

            self.sys_gate_outputs_dict[gate_output_name] = [gate_inputs, gate, gate.get_output()]

    def input_value(self, input_arr):
        '''
        the func convert from the input name to its value
        :param input_arr: the input name e.g [i1,i3,...] / [i3,z1,..]
        :return: input_to_send: array of the input value
        '''
        # input_arr =
        input_to_send = []
        for i_name in input_arr:
            if 'i' in i_name:
                input_to_send.append(self.sys_i[i_name])
            elif 'z' in i_name:
                input_to_send.append(self.sys_gate_outputs_dict[i_name][2])
            elif 'o' in i_name:
                input_to_send.append(self.sys_gate_outputs_dict[i_name][2])

        return input_to_send

    def convert_string_to_arr(self, s):
        '''
        the func convet the read line as a string to array
        :param s: line from the file e.g [[nand2,gate10,z1,i1,i3]
        :return: s: s as an array e.g [nand2, gate10, z1, i1, i3]
        '''
        s = s.replace('[', '')
        s = s.replace(']', '')
        s = s.replace('.', '')
        s = s.split(',')
        s[-1] = s[-1].replace('\n', '')
        return s

    def build_obs(self, obs_arr):
        '''
        the func update the inputs value in sys_i and the observation output in obs_output ,according to the observation
        :param obs_arr: the observation input and output values
        '''
        # obs_arr = self.convert_string_to_arr(obs_arr)
        for obs in obs_arr:
            if 'i' in obs:
                if obs.startswith('-'):
                    self.sys_i[obs[1:]] = 0
                else:
                    self.sys_i[obs] = 1
            elif 'o' in obs:
                if obs.startswith('-'):
                    self.obs_output[obs[1:]] = 0
                else:
                    self.obs_output[obs] = 1

    def initialize_sys_dict(self, obs_arr):
        self.sys_i = {}
        self.sys_o = {}
        for obs in obs_arr:
            if obs.startswith('-'):
                obs = obs[1:]
            if 'i' in obs:
                self.sys_i[obs] = 0
            if 'o' in obs:
                self.sys_o[obs] = 0

    def run(self, obs_arr):
        '''
        the func run the input observation value on the system, update the output in sys_gate_outputs_dict and
        in sys_o
        :param obs_arr: the observation input and output values
        '''
        self.initialize_sys_dict(obs_arr)
        self.build_obs(obs_arr)
        for out in self.sys_gate_outputs_dict.keys():
            # inputs = self.input_value(self.sys_gate_outputs_dict[out][0])
            # (self.sys_gate_outputs_dict[out][1]).set_inputs(inputs)
            # update_output = (self.sys_gate_outputs_dict[out][1]).get_output()
            # self.sys_gate_outputs_dict[out][2] = update_output
            self.bubbling(out)

        for out in self.sys_o.keys():
            self.sys_o[out] = self.sys_gate_outputs_dict[out][2]

    def run_diagnosis(self, node_output_gate):
        for out in self.sys_gate_outputs_dict.keys():
            # out is the node we check
            if out not in node_output_gate:
                self.bubbling(out)
            else:
                if self.sys_gate_outputs_dict[out][2] == 0:
                    self.sys_gate_outputs_dict[out][2] = 1
                else:
                    self.sys_gate_outputs_dict[out][2] = 0

        as_obs = []
        for out in self.sys_o.keys():
            self.sys_o[out] = self.sys_gate_outputs_dict[out][2]
            is_as_obs = self.sys_o[out] == self.obs_output[out]
            as_obs.append(is_as_obs)

        if False in as_obs:
            return False
        else:
            return True

    def bubbling(self, out):
        inputs = self.input_value(self.sys_gate_outputs_dict[out][0])
        (self.sys_gate_outputs_dict[out][1]).set_inputs(inputs)
        update_output = (self.sys_gate_outputs_dict[out][1]).get_output()
        self.sys_gate_outputs_dict[out][2] = update_output

    def get_sys_output(self):
        return self.sys_o

    def compare_output_to_obs_output(self):
        for out in self.sys_o:
            self.compare_outs[out] = ["sys out: ", self.sys_o[out], " obs out: ", self.obs_output[out], " result: ",
                                      self.sys_o[out] == self.obs_output[out]]
        return self.compare_outs

    def get_sys_comps_dict(self):
        return self.sys_comps_dict

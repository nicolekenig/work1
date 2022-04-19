import os

from dataSystem import dataSystem
PATH_DATA_SYS = 'data_for_exercises/circuits/Data_Systems'
PATH_DATA_OBS = 'data_for_exercises/circuits/Data_Observations'


def readFiles():
    files = os.listdir(PATH_DATA_SYS)
    for file_name in files:
        if file_name.startswith('c17'):
            print("file_name: ", file_name)
            buildCitcuit(PATH_DATA_SYS+'/'+file_name)
            # inf = open(PATH_DATA_SYS+'/'+file_name)
            # inf = inf.re
            # print(inf)
def convertStringToArr(s):
   s = s.replace('[', '')
   s = s.replace(']', '')
   s = s.replace('.','')
   s = s.split(',')
   return s

def buildCitcuit(file_path):
    f = open(file_path)
    sys_id = f.readline()
    sys_i = f.readline()
    sys_i = convertStringToArr(sys_i)
    print(sys_i)
    sys_o = f.readline()
    sys_o = convertStringToArr(sys_o)
    sys_o_num = []
    sys_gate_outputs_dict = {}  #key: gate_output (e.g z1) , val: value of z1

    dataSystem(sys_id, sys_i, sys_o, f)

    #
    # for line in f:
    #     line = convertStringToArr(line)
    #     gate_type_and_num_of_input = line[0]
    #     gate_type = gate_type_and_num_of_input[:-1]
    #     gate_name = line[1]
    #     num_of_input = gate_type_and_num_of_input[-1]
    #     gate_output_name = line[2]
    #     gate_inputs = line[3:]
    #
    #     sys_gate_outputs_dict[gate_output_name] = 0
    #
    #     for i in gate_inputs:
    #         for index in range(num_of_input):
    #
    #         if gate_type == 'and':
    #             and_gate = multibitAND(inputs=gate_inputs, gate_name=gate_name)
    #         elif gate_type == 'nand':
    #             nand_gate = multibitNAND(inputs=gate_inputs, gate_name=gate_name)
    #         elif gate_type == 'or':
    #             or_gate = multibitOR(inputs=gate_inputs, gate_name=gate_name)
    #         elif gate_type == 'nor':
    #             nor_gate = multibitNOR(inputs=gate_inputs, gate_name=gate_name)
    #         elif gate_type == 'xor':
    #             xor_gate = multibitXOR(inputs=gate_inputs, gate_name=gate_name)
    #         elif gate_type == 'inverter':
    #             inverter_gate = INVERTER(in1=gate_inputs, gate_name=gate_name)
    #         elif gate_type == 'buffer':
    #             buffer_gate = BUFFER(in1=gate_inputs, gate_name=gate_name)
    #
    #     print("gate_inputs:", gate_inputs)


def buildObs(file_path):
    f = open(file_path)
    sys_id = f.readline()
    sys_i = f.readline()
    sys_i = f.readline()
    sys_i = sys_i.replace('[', '')
    sys_i = sys_i.replace(']', '')
    sys_i = sys_i.split(',')
    print(sys_i)
    sys_i_num = []
    for i in sys_i:
        if i.startswith('-'):
            sys_i_num.append(0)
        else:
            sys_i_num.append(1)
    print('sys_i_num: ', sys_i_num)
    sys_o = f.readline()
    sys_o_num = []
    system = []

    for line in f:
        line = line.replace('[', '')
        line = line.replace(']', '')
        line = line.split(',')
        gate_type_tmp = line[0]
        gate_name = line[1]
        gate_type = gate_type_tmp[:-1]
        # print("gate type:", gate_type)
        gate_expected_output = line[2]
        gate_inputs = line[3:]
        print("gate_inputs:", gate_inputs)
if __name__ == '__main__':
    readFiles()

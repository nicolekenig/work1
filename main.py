import os

from dataSystem import dataSystem
from diagnosis import diagnosis

PATH_DATA_SYS = 'data_for_exercises/circuits/Data_Systems'
PATH_DATA_OBS = 'data_for_exercises/circuits/Data_Observations'
SYS1 = ''
systems = {}


def read_data_system_files(name_prefix):
    files = os.listdir(PATH_DATA_SYS)
    for file_name in files:
        if file_name.startswith(name_prefix):
            f = open(PATH_DATA_SYS + '/' + file_name)
            sys_id = f.readline().replace('.', '')
            sys_id = sys_id.replace('\n', '')
            sys_i = f.readline()
            sys_i = convert_string_to_arr(sys_i)
            sys_o = f.readline()
            sys_o = convert_string_to_arr(sys_o)
            systems[name_prefix] = dataSystem(sys_id, sys_i, sys_o, f)


def read_data_observation_files(name_prefix):
    files = os.listdir(PATH_DATA_OBS)
    for file_name in files:
        if file_name.startswith(name_prefix):
            f = open(PATH_DATA_OBS + '/' + file_name)
            diagnos = diagnosis(sys_id=name_prefix)
            for line in f:
                line = convert_string_to_arr(line)
                sys_id = line[0]
                obs_num = line[1]
                in_and_out_obs = line[2:]
                systems[sys_id].run(in_and_out_obs)
                ans = systems[sys_id].compare_output_to_obs_output()
                diagnos.set_obs_dict(obs_num, ans)
                diagnosis_ans = diagnos.run_bfs(systems[sys_id], systems[sys_id].get_sys_comps_dict())
                # print("Observation num ", obs_num, " - ", ans)
                print("diagnosis_ans: ", diagnosis_ans)
            diagnos.print_obs()

def convert_string_to_arr(s):
    s = s.replace('[', '')
    s = s.replace(']', '')
    s = s.replace('.', '')
    s = s.replace(')', '')
    s = s.replace('(', '')
    s = s.split(',')
    s[-1] = s[-1].replace('\n', '')
    return s

if __name__ == '__main__':
    print("*********** system c17 ***********")
    read_data_system_files('c17')
    read_data_observation_files('c17')
    print()
    # print("*********** system 74181 ***********")
    # read_data_system_files('74181')
    # read_data_observation_files('74181')
    # print()
    # print("*********** system 74182 ***********")
    # read_data_system_files('74182')
    # read_data_observation_files('74182')
    # print()
    # print("*********** system 74283 ***********")
    # read_data_system_files('74283')
    # read_data_observation_files('74283')
    # print()

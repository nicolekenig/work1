import os
import time

import pandas as pd
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
    ans_arr = [['System Name','Observation no.', 'Number of Diagnoses', 'Minimal Cardinality', 'Runtim e (ms)']]
    ans_dict ={
        'System Name':{},
        'Observation no.':{},
        'Number of Diagnoses':{},
        'Minimal Cardinality':{},
        'Maximal Cardinality': {},
        'Runtim e (ms)':{}
    }
    line_num = 0
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
                print("Observation num ", obs_num, " - ", ans)
                diagnos.set_obs_dict(obs_num, ans)
                start_time = time.time()
                diagnosis_ans = diagnos.run_bfs(systems[sys_id], systems[sys_id].get_sys_comps_dict())
                end_time = time.time()
                # without timeout
                ans_dict['System Name'][line_num] = sys_id
                ans_dict['Observation no.'][line_num] = obs_num
                ans_dict['Number of Diagnoses'][line_num] = len(diagnosis_ans)
                ans_dict[ 'Minimal Cardinality'][line_num] =  len(diagnosis_ans[0])
                ans_dict['Maximal Cardinality'][line_num] = '--'
                ans_dict['Runtim e (ms)'][line_num] = end_time-start_time
                line_num += 1
                # with timeout
                # ans_dict['System Name'][line_num] = sys_id
                # ans_dict['Observation no.'][line_num] = obs_num
                # ans_dict['Number of Diagnoses'][line_num] = len(diagnosis_ans)
                # ans_dict['Minimal Cardinality'][line_num] = len(diagnosis_ans[0])
                # ans_dict['Maximal Cardinality'][line_num] = len(diagnosis_ans[-1])
                # ans_dict['Runtim e (ms)'][line_num] = '--'
                # line_num += 1
                print("diagnosis_ans: ", diagnosis_ans)
                print()
            # diagnos.print_obs()
    data = pd.DataFrame(ans_dict)
    data.to_csv("output_c17.csv")

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
    # lst = ["a", "b", "c"]
    # ans = list(combinations(lst, 2))
    # print(ans)
    print("*********** system c17 ***********")
    read_data_system_files('c17')
    read_data_observation_files('c17')
    print()
    # print("*********** system 74181 ***********")
    # read_data_system_files('74181')
    # p1 = Process(target=read_data_observation_files('74181'))
    # p1.start()
    # p1.join(timeout=120)
    # p1.terminate()
    # print()
    # print("*********** system 74182 ***********")
    # read_data_system_files('74182')
    # read_data_observation_files('74182')
    # print()
    # print("*********** system 74283 ***********")
    # read_data_system_files('74283')
    # read_data_observation_files('74283')
    # print()

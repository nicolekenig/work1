import time
from itertools import combinations

class diagnosis:
    sys_id = ''
    obs_dict = {}  # key: obs_num, val: obs
    def __init__(self, sys_id):
        self.sys_id = sys_id

    def set_obs_dict(self, obs_num, obs_ans):
        self.obs_dict[obs_num] = obs_ans

    def print_obs(self):
        for obs in self.obs_dict:
            print("obs num: ", obs, " ", self.obs_dict[obs])

    def run_bfs(self, data_sys, sys_comps_dict):
        list_of_gates = [*sys_comps_dict]
        graph = {}  # key:gate_name, val: [[gates to check together]]
        visited = []
        queue = []
        diagnosis = []
        diagnosis = self.bfs(list_of_gates, graph, visited, queue, diagnosis, data_sys)
        return diagnosis

    def bfs(self, list_of_gates, graph, visited, queue, diagnosis, data_sys):
        # visited.append(list_of_gates[0])
        for node in list_of_gates:
            queue.append([node])
        end_time = time.time() + 120
        while queue:
            s = queue.pop(0)
            node_outputs_gate = self.get_output_gates(s, data_sys)
            is_healthy = data_sys.run_diagnosis(node_outputs_gate)
            if not is_healthy:
                diagnosis.append(s)
                list_of_gates = self.remove_from_list(s, list_of_gates)

            if len(queue) == 0:
                size = len(s)+1
                to_add = list(combinations(list_of_gates, size))
                if to_add is not s:
                    queue = queue + to_add
            curr_time = time.time()
            if curr_time > end_time:
                break
        return diagnosis

    def get_output_gates(self, nodes, data_sys):
        outputs = []
        for node in nodes:
            output_gate = data_sys.sys_comps_dict[node]
            outputs.append(output_gate)

        return outputs

    def remove_from_list(self, nodes, list_of_gates):
        for node in nodes:
            if node in list_of_gates:
                list_of_gates.remove(node)
        return list_of_gates

    def combinationUtil(self,arr,data,start,end,index, r):
        # Current combination is ready
        # to be printed, print it
        if index == r:
            for j in range(r):
                print(data[j], end=" ")
            return

        # replace index with all
        # possible elements. The
        # condition "end-i+1 >=
        # r-index" makes sure that
        # including one element at
        # index will make a combination
        # with remaining elements at
        # remaining positions
        i = start
        while (i <= end and end - i + 1 >= r - index):
            data[index] = arr[i]
            self.combinationUtil(arr, data, i + 1,
                            end, index + 1, r);
            i += 1


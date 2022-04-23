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
        node = list_of_gates
        diagnosis = self.bfs(list_of_gates, graph, visited, queue, diagnosis, data_sys, list_of_gates[0])
        return diagnosis

    def bfs(self, list_of_gates, graph, visited, queue, diagnosis, data_sys, node):
        visited.append(node)
        queue.insert(list_of_gates)

        while queue:
            s = [queue.pop(0)]
            node_outputs_gate = self.get_output_gates(s, data_sys)
            is_healthy = data_sys.run_diagnosis(node_outputs_gate)
            if is_healthy:
                diagnosis.append(node)
                list_of_gates = self.remove_from_list(s, list_of_gates)

            for gate in list_of_gates:
                if (gate not in s) and (gate not in visited):
                    if not is_healthy:
                        if gate is list_of_gates:
                            tmp = gate
                        else:
                            if (gate is list and s not in gate) or (gate is not list):
                                tmp = [gate]
                                tmp = tmp + s
                                node_to_add = tmp
                                tmp = None
                    else:
                        node_to_add = gate
                    # graph[node_to_add] = []
                    visited.append(gate)
                    queue.append(node_to_add)

        return diagnosis

    def get_output_gates(self, nodes, data_sys):
        outputs = []
        for node in nodes:
            outputs.append(data_sys.sys_comps_dict[node])

        return outputs

    def remove_from_list(self, nodes, list_of_gates):
        for node in nodes:
            list_of_gates.remove(node)
        return list_of_gates

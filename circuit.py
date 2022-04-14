class circuit:
    name = ''
    and_arr = []
    nand_arr = []
    or_arr = []
    xor_arr = []
    not_arr = []
    nor_arr = []
    xnor_arr = []
    {"gane_name": object gate}
    # ------------------------------ Set func ------------------------------
    def set_name(self,name):
        self.name = name

    def set_and_arr(self,and_gate):
        self.and_arr.append(and_gate)

    def set_nand_arr(self,nand_gate):
        self.nand_arr.append(nand_gate)

    def set_or_arr(self,or_gate):
        self.or_arr.append(or_gate)

    def set_xor_arr(self,xor_gate):
        self.xor_arr.append(xor_gate)

    def set_not_arr(self,not_gate):
        self.not_arr.append(not_gate)

    def set_nor_arr(self,nor_gate):
        self.nor_arr.append(nor_gate)

    def set_xnor_arr(self,xnor_gate):
        self.xnor_arr.append(xnor_gate)

    # ------------------------------ Get func ------------------------------
    def get_name(self):
        return self.name

    def get_and_gate_by_index(self,index):
        return self.and_arr[index]

    def get_nand_gate_by_index(self,index):
        return self.nand_arr[index]

    def get_or_gate_by_index(self,index):
        return self.or_arr[index]

    def get_xor_gate_by_index(self,index):
        return self.xor_arr[index]

    def get_not_gate_by_index(self,index):
        return self.not_arr[index]

    def get_nor_gate_by_index(self,index):
        return self.nor_arr[index]

    def get_xnor_gate_by_index(self,index):
        return self.xnor_arr[index]




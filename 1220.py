f = open("input/1220.txt", "r")

t = open("input/1220test.txt", "r")


def instructions(f):

    dict = {}

    for line in f:
        l = line.split(" -> ")
        dest = l[1].strip("\n").split(",")

        d_list = []

        for d in dest:
            d_list.append(d.strip())

        if l[0] == "broadcaster":
            dict["broadcaster"] = ("b", d_list)

        else:
            dict[l[0][1:]] = (l[0][0], d_list)

    return dict


INST = instructions(t)


class FlipFlop:
    def __init__(self, name):
        self.name = name
        self.state = 0
        self.pulse_state = 0
        self.dests = INST[name][1]

    def send_pulse(self):
        d = []
        for i in self.dest:
            m = build_module(i)
            module_state = m.receive_pulse(self.state)
            d.append(module_state)
        return d

    def receive_pulse(self, pulse_type):
        if pulse_type == 0:
            if self.state == 0:
                self.state = 1
                # self._send_pulse(1)
                self.pulse_state = 1
            elif self.state == 1:
                self.state = 0
                # self._send_pulse(0)
                self.pulse_state = 0

class Con:
    def __init__(self, name):
        self.name = name        
        # list of connected modules types
        self._connected = []
        self.dests = INST[name][1]
        self.state = 0

    def send_pulse(self):
        d = []
        if all(i.pulse_state == 1 for i in self._connected):
            pulse_type = 0
        else:
            pulse_type = 1
        for i in self.dest:
            m = build_module(i)
            module_state = m.receive_pulse(pulse_type)
            d.append(module_state)
        return d

    def receive_pulse(self, pulse_type):
        self.state = pulse_type    
        for m in self._connected:
            m.receive_pulse(pulse_type)
        return self
        # self._send_pulse()


class Broadcaster:
    def __init__(self):
        self.name = "broadcaster"
        self.state = 0
        self.dests = INST[self.name][1]

    def send_pulse(self):
        for d in self.dests:
            d.receive_pulse(self.state)

    def receive_pulse(self, pulse_type):
        self.state = pulse_type
        # self._send_pulse(pulse_type)

    
def build_module(name):

    mod_type = INST[name][0]

    if mod_type == "%":
        return FlipFlop(name)
    elif mod_type == "&":
        return Con(name)
    else:
        return Broadcaster()


def receive_pulse(module, pulse_type):

    inst = INST[module.name]
    print(inst[1])

    modules = []

    for i in inst[1]:
        print(i)
        type = INST[i][0]
        m = build_module(i)
        modules.append(m)

    for m in modules:
        m.receive_pulse(pulse_type)

    # for m in modules:
    #     print(m.name, m.state, m.pulse_state)

    return modules


def send_pulse(module, modules):
    # module in current state and destination list

    for m in modules:
        if m.name in module.dests:
            m.receive_pulse(module.state)

    #returns state of module after sending pulse




# print(pulse(Broadcaster(), 0))    

def build_all_modules():

    modules = []

    for k in INST:
        m = build_module(k)
        modules.append(m)

    return modules



def initialize_dests(module, modules):

    for m in modules:
        print(m.name, INST[module.name][1])
        if m.name in INST[module.name][1]:
            print("found connection")
            module.dests.append(m)     
    return modules       


def get_module(name, modules):

    for m in modules:
        if m.name == name:
            return m


def press():

    modules = build_all_modules()

    # add button logic
    pulse_type = 0
    b = Broadcaster()
    print("dests", b.dests)
    queue = b.dests

    b.receive_pulse(pulse_type)
    print(b.state)

    send_pulse(b, modules)

    for m in modules:
        print(m.name, m.state, m)

    # queue 
    while len(queue) != 0:
        for _, q in enumerate(queue):
            # get module w name
            m = get_module(q, modules)

            print(m.name, m.state, m)

            send_pulse(m, modules)
            for d in m.dests:
                queue.append(d)
            queue.pop(0)

    for m in modules:
        print(m.name, m.state, m)


            # XCXC flatten list
            # for e in enqueue:
            #     print("enqueing", e)
            #     queue.append(e)
            # queue.pop(i)
            # print("queue", queue)
            # XCXC get pulse type

        print(queue)
    

    


    # queue = b.send_pulse()
    # dests = INST[b][1]

    # dests receive pulses
    # for m in modules, for d in dests:
    #     if m.name == d:
    #         m.receive_pulse(pulse_type)




    # check module type
    # send to destinations
        # check module type of destination
    # XCXC check current queue for modules and send signal to them
        # create instance of destination modules
        # receive pulses
    # queue pulses to send




    # return queue





# print(build_all_modules())
    
print(press())



         
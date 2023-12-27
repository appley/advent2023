f = open("input/1220.txt", "r")

t = open("input/1220test2.txt", "r")


def instructions(f):

    dict = {}

    for line in f:
        l = line.split(" -> ")
        dest = l[1].strip("\n").split(",")

        d_list = []

        for d in dest:
            d_list.append(d.strip())

        if l[0] == "broadcaster":
            dict["broadcaster"] = ("br", d_list)

        else:
            dict[l[0][1:]] = (l[0][0], d_list)

        dict["rx"] = ("ou", d_list)  # remove after test

    return dict


INST = instructions(f)


def build_connections(con):

    cons = []

    for k, v in INST.items():
        if con in v[1]:
            cons.append(k)
    
    return cons


class FlipFlop:
    def __init__(self, name):
        self.name = name
        self.state = 0
        self.dests = INST[name][1]
        self.pulse_queue = []

    def send_pulse(self): 
        pass

    def receive_pulse(self, module, pulse_type):
        if pulse_type == 1:
            return False
        if pulse_type == 0:
            if self.state == 0:
                self.state = 1
            elif self.state == 1:
                self.state = 0
                self.pulse_state = 0
        return True


class Con:
    def __init__(self, name):
        self.name = name        
        # list of connected modules types
        self.dests = INST[name][1]
        self._connected = {}
        for c in build_connections(self.name):
            self._connected[c] = 0
        self.state = 0

    def send_pulse(self):
        d = []
        if all(v == 1 for _, v in self._connected.items()):
            self.state = 0
        else:
            self.state = 1

    def receive_pulse(self, module, pulse_type):
        self._connected[module.name] = pulse_type
        self.state = pulse_type
        print("connected modules for ", self.name, self._connected)
        return True


class Broadcaster:
    def __init__(self):
        self.name = "broadcaster"
        self.state = 0
        self.dests = INST[self.name][1]

    def send_pulse(self):
        pass

    def receive_pulse(self, pulse_type):
        self.state = pulse_type
        return True


class Output:
    def __init__(self, name):
        self.name = name
        self.state = 0
        self.dests = []
    
    def send_pulse(self):
        pass

    def receive_pulse(self, module, pulse_type):
        return True


def build_module(name):

    mod_type = INST[name][0]

    if mod_type == "%":
        return FlipFlop(name)
    elif mod_type == "&":
        return Con(name)
    elif mod_type == "br":
        return Broadcaster()
    else:
        return Output(name)


def build_all_modules():

    modules = []

    for k in INST:
        m = build_module(k)
        modules.append(m)

    return modules


def get_module(name, modules):

    for m in modules:
        if m.name == name:
            return m


def button(modules):

    high = 0
    low = 1
    queue = []

    def send_and_receive(module, dests):


    # start broadcaster
    start_pulse_type = 0
    b = get_module("broadcaster", modules)
    b.receive_pulse(start_pulse_type)

    # send pulse from broadcaster and set inital state of receiving modules
    for d in b.dests:
        b.send_pulse()
        low = low + 1

        dest = get_module(d, modules)

        if dest.receive_pulse(b, b.state) == True:  # generalize this to encompass code in loop
            queue.append(d)

    # send pulses from queue 
    for _, q in enumerate(queue):
        # get module w name
        m = get_module(q, modules) # get sending module
        print("found module preparing to send pulses", m.name, m.state, m)

        for d in m.dests:
            m.send_pulse()
            if m.state == 0:
                low = low + 1
            else:
                high = high + 1

            dest = get_module(d, modules)
            if not dest:
                dest = build_module(d)

            print("sending pulse from ", m.name, "--> ", dest.name, m.state)
            if dest.receive_pulse(m, m.state) == True:
                queue.append(d)
    
    return (high, low)


def press(num):

    high = 0
    low = 0

    modules = build_all_modules()

    for _ in range(num):
        b = button(modules)
        high = high + b[0]
        low = low + b[1]

    return high * low


if __name__ == "__main__":


    print(press(1000))
         
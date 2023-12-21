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
print(INST)


class FlipFlip:
    def __init__(self, name):
        self.name = name
        self.state = 0
        self.pulse_state = 0

    def _send_pulse(self, pulse_type):
        if pulse_type == 0:
            return 0
        if pulse_type == 1:
            return 1

    def receive_pulse(self, pulse_type):
        if pulse_type == 0:
            if self.state == 0:
                self.state = 1
                self._send_pulse(1)
                self.pulse_state = 1
            if self.state == 1:
                self.state = 0
                self._send_pulse(0)
                self.pulse_state = 0


class Con:
    def __init__(self, name, state):
        self.name = name        
        # list of connected modules types
        self._connected = []

    def receive_pulse(self, pulse_type):      
            for m in self._connected:
                m.receive_pulse(pulse_type)
            self._send_pulse()

    def _send_pulse(self, dest):
        if all(i.pulse_state == 1 for i in self._connected):
            return (0, dest)
        else:
            return (1, dest)
        

class Broadcaster:
    def __init__(self):
        self.name = "broadcaster"

    def _send_pulse(self, pulse_type, dest):
        return (pulse_type, dest)

    def receive_pulse(self, pulse_type):
        self._send_pulse(pulse_type)


    
def build_module(mod_type, name):

    print(mod_type)

    if mod_type == "%":
        return FlipFlip(name)
    elif mod_type == "&":
        return Con(name)
    else:
        return Broadcaster()


def pulse(module, pulse_type):

    inst = INST[module.name]
    print(inst[1])

    modules = []

    for i in inst[1]:
        print(i)
        type = INST[i][0]
        m = build_module(type, i)
        modules.append(m)

    for m in modules:
        m.receive_pulse(pulse_type)

    # for m in modules:
    #     print(m.name, m.state, m.pulse_state)

    return modules


print(pulse(Broadcaster(), 0))


def press():

    pulse_type = 0
    start_modules = pulse(Broadcaster(), pulse_type)
    queue = start_modules.copy()

    while len(queue) != 0:
        for q in queue:
            type = "" # XCXC
            # XCXC get pulse type
            pulse(q, )


    # check module type
    # send to destinations
        # check module type of destination
        # create instance of destination modules
        # receive pulses
    # queue pulses to send

    







         
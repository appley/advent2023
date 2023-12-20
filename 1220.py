f = open("input/1220.txt", "r")

INST = ""


class FlipFlip:
    def __init__(self, name, state):
        self.name = name
        self.state = state

    def send_pulse(pulse_type):
        if pulse_type == 0:
            return 0
        if pulse_type == 1:
            return 1

    def receive_pulse(self, pulse_type):
        if pulse_type == 0:
            if self.state == 0:
                self.state = 1
                self.send_pulse(1)
            if self.state == 1:
                self.state = 0
                self.send_pulse(0)


class Con:
    def __init__(self, name, state):
        self.name = name
        self.state = state
        
        # list of connected modules types
        self._connected = []

    def receive_pulse(module, pulse_type)     
        self._connected

    def send_pulse(self, type):

        if all(i == 0 for i in self._connected)





def instructions(f):

    dict = {}

    for line in f:
        l = line.split(" -> ")
        dest = l[1].strip("\n").split(",")

        d_list = []

        for d in dest:
            d_list.append(d)

        if l[0] == "broadcaster":
            dict["broadcaster"] = d_list

        else:
            dict[l[0][1:]] = (l[0][0], d_list)

    return dict


def flip(pulse, curr_state):

    if pulse == 1:
        return (curr_state, False)
    
    elif curr_state == 0:
        # turn on, high pulse
        return (1, 1)
    
    else:
        # turn off, low pulse
        return(0, 0)
    

def con(pulse, curr_state):

    





def pulse(key, dest):

    inst = INST[key]
    type = inst[0]

    for i in inst[1]:
        if type == 






print(instructions(f))




         
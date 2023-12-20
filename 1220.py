f = open("input/1220.txt", "r")

INST = ""


class FlipFlip:
    def __init__(self, name):
        self.name = name
        self.state = 0
        self.pulse_state = 0

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
                self.pulse_state = 1
            if self.state == 1:
                self.state = 0
                self.send_pulse(0)
                self.pulse_state = 0


class Con:
    def __init__(self, name, state):
        self.name = name        
        # list of connected modules types
        self._connected = []

    def receive_pulse(self, module)          
            for m in self._connected:
                if m.name == module.name:
                    self._connected.remove(m)
            self._connected.append(module)

    def send_pulse(self, dest):
        if all(i.pulse_state == 1 for i in self._connected):
            return 0
        else:
            return 1
        

class Broadcaster:
    def __init__(self):
        pass

    def send_pulse(self, pulse_type, dest):
        return pulse_type

    def receive_pulse(self, pulse_type):
        self.send_pulse(pulse_type)


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


print(instructions(f))

def press(instruction):

    queue = []

    # check module type
    # send to destinations
        # check module type of destination
        # create instance of destination modules
        # receive pulses
    # queue pulses to send











# def flip(pulse, curr_state):

#     if pulse == 1:
#         return (curr_state, False)
    
#     elif curr_state == 0:
#         # turn on, high pulse
#         return (1, 1)
    
#     else:
#         # turn off, low pulse
#         return(0, 0)
    

# def con(pulse, curr_state):

    
def build_module(mod_type, name):

    if mod_type == "%":
        return FlipFlip(name)
    elif mod_type == "&":
        return Con(name)
    else:
        return Broadcaster()




# def pulse(key, dest):

#     inst = INST[key]
#     type = inst[0]

#     for i in inst[1]:







         
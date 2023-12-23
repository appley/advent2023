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

    return dict


INST = instructions(t)


class FlipFlop:
    def __init__(self, name):
        self.name = name
        self.state = 0
        self.dests = INST[name][1]
        self.pulse_queue = []

    def send_pulse(self): #, pulse_type):
        # pulse_type = self.pulse_queue[0] # get type of pulse to send
        # self.pulse_queue.pop(0) # dequeue pulse
        # return pulse_type

        pass

    def receive_pulse(self, module, pulse_type):
        if pulse_type == 1:
            # if self.state == 0:
            #     self.state = 1
            # elif self.state == 1:
            #     self.state = 0
                # self._send_pulse(0)
            return False
        if pulse_type == 0:
            if self.state == 0:
                self.state = 1
                # self.pulse_queue.append(1)
            elif self.state == 1:
                self.state = 0
                # self._send_pulse(0)
                self.pulse_state = 0
                # self.pulse_queue.append(0)
        return True

class Con:
    def __init__(self, name):
        self.name = name        
        # list of connected modules types
        self.dests = INST[name][1]
        self._connected = {}
        self.state = 0

    def send_pulse(self):
        d = []
        if all(v == 1 for _, v in self._connected.items()):
            # print("starting state for ", self.name, "to", self.state)
            self.state = 0
            # print("setting state for ", self.name, "to", self.state)
        else:
            self.state = 1
            # print("setting state for ", self.name, "to", self.state)


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
        # for d in self.dests:
        #     d.receive_pulse(self.state)

    def receive_pulse(self, pulse_type):
        self.state = pulse_type
        return True
        # self._send_pulse(pulse_type)

    
def build_module(name):

    mod_type = INST[name][0]

    if mod_type == "%":
        return FlipFlop(name)
    elif mod_type == "&":
        return Con(name)
    else:
        return Broadcaster()


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


# def send_pulse(module, modules):
#     # module in current state and destination list

#     # count = 0

#     for m in modules:
#         if m.name in module.dests:
#             print("sending pulse from ", module.name, "to", m.name, module.state)
#             m.send_pulse()
#             # count = count + 1

#             # receiving module receives pulse and changes its state accordingly
#             pulsed = m.receive_pulse(module, module.state)
#             print("pulsed ", pulsed, m.name, module.state)


#             # print("count ", m.state)
    
#     return pulsed # count, m.state


def button():

    high = 0
    low = 0

    modules = build_all_modules()

    # start broadcaster
    start_pulse_type = 0
    b = Broadcaster()
    queue = []
    b.receive_pulse(start_pulse_type)

    # send pulse from broadcaster and set inital state of receiving modules

    for d in b.dests:
        b.send_pulse()

        dest = get_module(d, modules)
        print(dest.name, dest)

        new_state = dest.receive_pulse(b, b.state)
        if new_state == True:

            queue.append(d)

    print(queue)


    # send_pulse(b, modules)

    # send pulses from queue 
    for _, q in enumerate(queue):
        # get module w name
        m = get_module(q, modules) # get sending module

        print("found module preparing to send pulses", m.name, m.state, m)

        # module sends pulse to destination modules and dests receive pulse
        # s = send_pulse(m, modules)

        for d in m.dests:
            m.send_pulse()

            dest = get_module(d, modules)
            print(d, dest)

            print("sending pulse from ", m.name, "--> ", dest.name, m.state)
            if dest.receive_pulse(m, m.state) == True:

                queue.append(d)
                print("adding to queue", d)
                print(queue)







        # if a destination received a pulse and needs to send a pulse it returns True
        # if s:  

        #     print("PULSE ", m.name)

            # if s[2] == 0:
            #     low = low + s[1]

            # else:
            #     high = high + s[1]

            # appending destinations to send queue
            # for d in m.dests:
                # print("dests", m.dests) # append next sender
                # print("appending ", d)
                # queue.append(d)  # append to send queue
                # print("counting dest", d)
                # print("module state", m.state)
                # if m.state == 0:
                #     low = low + 1
                # else:
                #     high = high + 1
        # send_pulse(m, modules)

    for m in modules:
        print(m.name, m.state, m)

    return (high, low)



print(button())
def press(num):

    for i in range(num):
        button()




         
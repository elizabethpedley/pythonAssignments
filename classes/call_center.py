
class Call(object):
    def __init__(self, id, name, num, time, reason):
        self.id = id
        self.caller_name = name
        self.caller_number = num
        self.call_time = time
        self.reason = reason
    
    def __eq__(self, other):
        return self.call_time == other.call_time
    def __lt__(self, other):
        return self.call_time < other.call_time

    def display(self):
        attributes = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        for attribute in attributes:
            print attribute+ ': ' + str(getattr(self, attribute))

class Call_center(object):
    def __init__(self):
        self.calls = []
        self.queue = len(self.calls)

    def new_call(self, id, name, num, time, reason):
        self.calls.append(Call( id, name, num, time, reason))
        self.calls = sorted(self.calls)
        return self
    
    def remove(self):
        self.calls.pop(0)
        return self
    
    def call_queue(self):
        print 'There are {} calls in the queue'.format(len(self.calls))
        for i in range(len(self.calls)):
            print self.calls[i]['caller_name']
            print self.calls[i]['caller_number']
        return self
    
    def finish_call_by_number(self, num):
        indx = None
        for i in range(len(self.calls)):
            if self.calls[i]['caller_number'] == num:
                indx = i
                break
        if indx is not None:
            self.calls.pop(i)
        else:
            print 'There are no calls with thats number'
    def show_calls(self):
        for call in self.calls:
            print call.call_time, call.id, call.caller_number, call.caller_name


chicago = Call_center()
chicago.new_call(22, 'bob', '555-555-5555', 1455, 'unhappy')
chicago.new_call(22, 'bob', '555-555-5555', 1023, 'unhappy')
chicago.new_call(22, 'bob', '555-555-5555', 1423, 'unhappy')
chicago.new_call(22, 'bob', '555-555-5555', 23, 'unhappy')

# chicago.show_calls()
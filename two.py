import sys
import linecache
import inspect

JANKY_NAMESPACE_MANAGER = {}

class Box(object):
    def __init__(self, obj, name):
        self.obj = obj
        self.name = name
        self.assignments = 1
        self.nabbed = "hehehe"
        JANKY_NAMESPACE_MANAGER[name] = self

    # def lift(self):
    #     if isinstance(self.obj, Box):
    #         return self.obj
    #     else:
    #         return self

    # def __getattr__(self, attr):
    #     return self.obj.attr

    # def __setattr__(self, attr, value):
    #     self.obj.attr = value

    def __repr__(self):
        return self.name + "(assigned " + str(self.assignments) + " times)"

class Tracer(object):

    def __init__(self, program):
        self.program = program

    def traceit(self, frame, event, arg):
        if event == 'line':
            linenum = frame.f_lineno
            linetext = linecache.getline(self.program, linenum)
            print 'line', linenum, linetext
        
            is_assignment = "=" in linetext and "==" not in linetext

            if is_assignment:
                self.mark_for_deletion(frame, linetext)

        return self.traceit

    def mark_for_deletion(self, frame, linetext):
        print inspect.getframeinfo(frame)
        rhs = linetext[linetext.index("=")+1:]
        names = rhs.split()
        print "side effecting!", names
        print "locals are", frame.f_locals.keys()
        print "globals are ", frame.f_globals.keys()
        local_objs = [name for name in names if name in frame.f_locals.keys() + frame.f_globals.keys()]
        for name in local_objs:
            if name not in JANKY_NAMESPACE_MANAGER:
                box = Box(frame.f_locals[name], name)
                frame.f_locals[name] = box
                print box
            else:
                JANKY_NAMESPACE_MANAGER[name].assignments += 1
                print "jankily counted"

    # def delete(self):
    

def greet():
    name = raw_input("Enter your name: ")
    print "hello,", name
    
    name_copy = name
    
    print name

    other_copy = name

    print name



def assign_only_once():    
    trace_obj = Tracer(__file__)
    sys.settrace(trace_obj.traceit)

if __name__ == '__main__':
    program_name = __file__

    assign_only_once()
    
    greet()








# next to pursue
# GC, can we reference count and delete references
# inspect module, can we capture assignments and do something
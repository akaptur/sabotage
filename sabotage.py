import sys
import linecache
import inspect

JANKY_NAMESPACE_MANAGER = {}

def vprint(*args):
    verbose_mode = False
    if verbose_mode:
        print(args)
    else:
        pass

class Box(object):
    def __init__(self, obj, name):
        self.obj = obj
        self.name = name
        self.assignments = 1
        self.nabbed = "hehehe"
        JANKY_NAMESPACE_MANAGER[name] = self

    def __repr__(self):
        raise NameError("this message has self-destructed.")

class Tracer(object):
    def __init__(self, program):
        self.program = program

    def traceit(self, frame, event, arg):
        if event == 'line':
            linenum = frame.f_lineno
            linetext = linecache.getline(self.program, linenum)
            vprint( 'line', linenum, linetext )

            is_assignment = "=" in linetext and "==" not in linetext

            if is_assignment:
                self.mess_up_on_assignment(frame, linetext)

        return self.traceit

    def mess_up_on_assignment(self, frame, linetext):
        vprint( inspect.getframeinfo(frame) )
        rhs = linetext[linetext.index("=")+1:]
        names = rhs.split()
        vprint( "side effecting!", names )
        vprint( "locals are", frame.f_locals.keys() )
        vprint( "globals are ", frame.f_globals.keys() )
        local_objs = [name for name in names if name in frame.f_locals.keys() + frame.f_globals.keys()]
        for name in local_objs:
            if name not in JANKY_NAMESPACE_MANAGER:
                box = Box(frame.f_locals[name], name)
                frame.f_locals[name] = box
                vprint( box )
            else:
                JANKY_NAMESPACE_MANAGER[name].assignments += 1
                vprint( "jankily counted" )


def assignment(orig_file):
    trace_obj = Tracer(orig_file)
    sys.settrace(trace_obj.traceit)

if __name__ == '__main__':
    program_name = __file__

    sabotage_assignment(program_name)

    greeting = "Hello"

    print greeting










# next to pursue
# GC, can we reference count and delete references
# inspect module, can we capture assignments and do something
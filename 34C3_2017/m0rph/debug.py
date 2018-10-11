# coding: utf-8
import gdb

class PrintRaxBreakpoint(gdb.Breakpoint):
    def __init__(self, spec):
        super().__init__(spec, gdb.BP_BREAKPOINT, internal=False)

    def stop(self):
        gdb.execute("p/x $rax")
        return true

gdb.execute("file morph")
#gdb.Breakpoint("*0x0000555555554a76")
PrintRaxBreakpoint("*0x0000555555554B95")
arg = 'A' * 23
gdb.execute("r " + arg)
gdb.execute("c")
gdb.execute("del br")

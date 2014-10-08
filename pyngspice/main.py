'''
Created on Oct 7, 2014

@author: martin
'''



from ctypes import *
from callbacks import *
import sys
import binascii


def init():
    
    ngspice_lib = cdll.LoadLibrary("/usr/local/lib/libngspice.so")
    
    ngspice_lib.ngSpice_Init(pSendChar,pSendStat,pControlledExit,pSendData,pSendInitData,None,0)
    
    return ngspice_lib
    #ngspice_lib.ngSpice_Command(c_char_p(("source " + "/home/martin/Apps/geda/bms/spice.net").encode()))  # + sys.argv[0]))


    #ngspice_lib.ngSpice_Command(c_char_p("bg_run".encode()))

    #ngspice_lib.ngSpice_Command(c_char_p("quit".encode()))
    
def ng_command(command, ngspice_lib):
    
    ngspice_lib.ngSpice_Command(c_char_p(command.encode()))
    
    
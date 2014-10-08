'''
Created on Oct 7, 2014

@author: martin
'''



from ctypes import *
from callbacks import *
import sys
import binascii


def init(path_to_lib):
    ''' standard library path on Linux: /usr/local/lib/libngspice.so '''
    
    ngspice_lib = cdll.LoadLibrary(path_to_lib)
    
    ngspice_lib.ngSpice_Init(pSendChar,pSendStat,pControlledExit,pSendData,pSendInitData,None,0)
    
    return ngspice_lib

    
def ng_command(command, ngspice_lib):
    
    ngspice_lib.ngSpice_Command(c_char_p(command.encode()))
    
    
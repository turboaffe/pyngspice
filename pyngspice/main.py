'''
Created on Oct 7, 2014

@author: martin
'''



import ctypes
import callbacks
import binascii


class Ngspice():
    

    def __init__(self, path_to_lib="/usr/local/lib/libngspice.so"):
        
        self.path_to_lib = path_to_lib
        

    def init(self):
        ''' standard library path on Linux: /usr/local/lib/libngspice.so '''
        
        self.ngspice_lib = ctypes.cdll.LoadLibrary(self.path_to_lib)
        
        self.ngspice_lib.ngSpice_Init(callbacks.pSendChar,callbacks.pSendStat,
                                      callbacks.pControlledExit,callbacks.pSendData,
                                      callbacks.pSendInitData,None,0)
    
        
    def ng_command(self, command):
        
        self.ngspice_lib.ngSpice_Command(ctypes.c_char_p(command.encode()))
    
    
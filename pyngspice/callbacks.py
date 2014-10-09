'''
Created on Oct 7, 2014

@author: martin
'''

import ctypes
import ngtypes
import binascii

### callback functions ###

def SendChar(p_output, lib_id, p_request=0):
    ''' Sending output from stdout, stderr to caller. '''
    print(ctypes.cast(p_output, ctypes.c_char_p).value.decode('ascii'))

    
def SendStat(p_sim_stat, lib_id, p_request=0):
    ''' sending simulation status to caller, e.g. the string ’tran 34.5%’. '''
    
    print(ctypes.cast(p_sim_stat, ctypes.c_char_p).value.decode('ascii'))
    
    
def ControlledExit(exit_status, unloading, exit_upon_quit, lib_id, p_request=0):
    ''' asking for a reaction after controlled exit. '''

    print(exit_status)


def SendData(p_vecvaluesall, nr_of_structs, lib_id, p_request=0):
    ''' send back actual vector data. '''

    #print(p_vecvaluesall)
    
    
def SendInitData(p_vecinfoall, lib_id, p_request=0):
    ''' send back initialization vector data. '''
    
    print("SendInitData:")    
    print(p_vecinfoall.contents.name.decode('ascii'))
    print(p_vecinfoall.contents.title.decode('ascii'))
    print(p_vecinfoall.contents.date.decode('ascii'))
    print(p_vecinfoall.contents.type.decode('ascii'))
    print(p_vecinfoall.contents.veccount)
    
    print("Available vectors:")
    for x in range(0, p_vecinfoall.contents.veccount):
        print(p_vecinfoall.contents.vecs[x].contents.vecname.decode('ascii'))

    
    
pSendChar       = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p)(SendChar)
pSendStat       = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p)(SendStat)
pControlledExit = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_bool, ctypes.c_bool, ctypes.POINTER(ctypes.c_int))(ControlledExit)
pSendData       = ctypes.CFUNCTYPE(None, ctypes.POINTER(ngtypes.Vecvaluesall), ctypes.c_int, ctypes.c_int, ctypes.c_void_p)(SendData)
pSendInitData   = ctypes.CFUNCTYPE(None, ctypes.POINTER(ngtypes.Vecinfoall), ctypes.c_int, ctypes.c_void_p)(SendInitData) 
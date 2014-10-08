'''
Created on Oct 7, 2014

@author: martin
'''
from ctypes import *
from ngtypes import *
import binascii

### callback functions ###

def SendChar(p_output, lib_id, p_request=0):
    ''' Sending output from stdout, stderr to caller. '''
    print(cast(p_output, c_char_p).value)

    
def SendStat(p_sim_stat, lib_id, p_request=0):
    ''' sending simulation status to caller, e.g. the string ’tran 34.5%’. '''
    
    print(cast(p_sim_stat, c_char_p).value)
    
    
def ControlledExit(exit_status, unloading, exit_upon_quit, lib_id, p_request=0):
    ''' asking for a reaction after controlled exit. '''

    print(exit_status)


def SendData(p_vecvaluesall, nr_of_structs, lib_id, p_request=0):
    ''' send back actual vector data. '''

    #print(p_vecvaluesall)
    
    
def SendInitData(p_vecinfoall, lib_id, p_request=0):
    ''' send back initialization vector data. '''
    
    print("SendInitData:")    
    print(p_vecinfoall.contents.name)
    print(p_vecinfoall.contents.title)
    print(p_vecinfoall.contents.date)
    print(p_vecinfoall.contents.type)
    print(p_vecinfoall.contents.veccount)
    
    print("Available vectors:")
    for x in range(0, p_vecinfoall.contents.veccount):
        print(p_vecinfoall.contents.vecs[x].contents.vecname)

    
    
pSendChar       = CFUNCTYPE(c_char_p, c_int, c_void_p)(SendChar)
pSendStat       = CFUNCTYPE(c_char_p, c_int, c_void_p)(SendStat)
pControlledExit = CFUNCTYPE(c_int, c_bool, c_bool, POINTER(c_int))(ControlledExit)
pSendData       = CFUNCTYPE(None, POINTER(Vecvaluesall), c_int, c_int, c_void_p)(SendData)
pSendInitData   = CFUNCTYPE(None, POINTER(Vecinfoall), c_int, c_void_p)(SendInitData) 
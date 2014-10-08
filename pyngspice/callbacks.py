'''
Created on Oct 7, 2014

@author: martin
'''
from ctypes import *
from ngtypes import *
import binascii

#typedef int (SendChar)(char*, int, void*)
# 



def SendChar(p_output, lib_id, p_request=0):
     
    print(cast(p_output, c_char_p).value)

    
def SendStat(p_sim_stat, lib_id, p_request=0):
    
    print(cast(p_sim_stat, c_char_p).value)
    
    
def ControlledExit(exit_status, unloading, exit_upon_quit, lib_id, p_request=0):
    
    print(exit_status)


def SendData(p_vecvaluesall, nr_of_structs, lib_id, p_request=0):

    print(p_vecvaluesall)
    
    
def SendInitData(p_vecinfoall, lib_id, p_request=0):
    
    print("SendInitData:")    
    print(p_vecinfoall.contents.name)
    print(p_vecinfoall.contents.title)
    print(p_vecinfoall.contents.date)
    print(p_vecinfoall.contents.type)
    print(p_vecinfoall.contents.veccount)
    
    print(p_vecinfoall.contents.vecs[0].contents.number)
    print(p_vecinfoall.contents.vecs[0].contents.vecname)
    print(p_vecinfoall.contents.vecs[0].contents.is_real)

    
    #print(binascii.b2a_uu(p_vecinfoall.contents.name))




#CMPFUNC = CFUNCTYPE(POINTER(Vecinfoall), c_int, c_void_p)
#argh = CMPFUNC(SendInitData)

pSendChar       = CFUNCTYPE(c_char_p, c_int, c_void_p)(SendChar)
pSendStat       = CFUNCTYPE(c_char_p, c_int, c_void_p)(SendStat)
pControlledExit = CFUNCTYPE(c_int, c_bool, c_bool, POINTER(c_int))(ControlledExit)
pSendData       = CFUNCTYPE(None, c_void_p, c_int, c_int, c_void_p)(SendData)
pSendInitData   = CFUNCTYPE(None, POINTER(Vecinfoall), c_int, c_void_p)(SendInitData) 
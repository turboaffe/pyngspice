'''
Created on Oct 8, 2014

@author: martin
'''

from ctypes import *


class Vecinfo(Structure):
    #_pack_=2
    _fields_ = [('number', c_int),       #number of vector , as postion in the linked list of vectors , starts with 0
                ('vecname', c_char_p),     #name of the actual vector
                ('is_real', c_bool),     #TRUE if the actual vector has real data
                ('pdvec', c_void_p),     #a void pointer to struct dvec *d , the actual vector
                ('pdvecscale', c_void_p) #a void pointer to struct dvec *ds ,the scale vector
                ]

class Vecinfoall(Structure):
    #_pack_=2
    
    _fields_ = [('name', c_char_p),     
                ('title', c_char_p),  
                ('date', c_char_p),    
                ('type', c_char_p),   
                ('veccount', c_int),    
                ('vecs', POINTER(POINTER(Vecinfo))) #the data as an array of vecinfo with length equal to the number of vectors in the plot
                ]
 

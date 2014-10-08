'''
Created on Oct 8, 2014

@author: martin
'''

from ctypes import *


class Vecinfo(Structure):
    _fields_ = [('number', c_int),       # number of vector , as postion in the linked list of vectors , starts with 0
                ('vecname', c_char_p),   # name of the actual vector
                ('is_real', c_bool),     # TRUE if the actual vector has real data
                ('pdvec', c_void_p),     # a void pointer to struct dvec *d , the actual vector
                ('pdvecscale', c_void_p) # a void pointer to struct dvec *ds ,the scale vector
                ]

class Vecinfoall(Structure):
    _fields_ = [('name', c_char_p),     
                ('title', c_char_p),  
                ('date', c_char_p),    
                ('type', c_char_p),   
                ('veccount', c_int),    
                ('vecs', POINTER(POINTER(Vecinfo))) #the data as an array of vecinfo with length equal to the number of vectors in the plot
                ]
 
class Vecvalues(Structure):
    _fields_ = [('name', c_char_p),     # name of a specific vector
               ('creal', c_double),     # actual data value
               ('cimag', c_double),     # actual data value
               ('is_scale', c_bool),    # if "name" is the scale vector
               ('is_complex', c_bool)   # if the data are complex numbers
               ]
 
class Vecvaluesall(Structure):
    ''' Pointer vecvaluesall to be found as parameter to callback function SendData.'''
    _fields_ = [('veccount', c_int),    # number of vectors in plot
                ('vecindex', c_int),    # index of actual set of vectors, i.e. the number of accepted datapoints
                ('vecsa', POINTER(POINTER(Vecvalues))) # values of actual set of vectors, indexed from 0 to veccount − 1
                ]


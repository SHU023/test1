


"""
Created on 2019/03/04

@author: shu777

"""

import visa

import math

import time

import sys



class GS200():

    #### This class implements the GS200 ####

    def __init__(self, ip, options={}):

        rm = visa.ResourceManager()

        self.inst = rm.open_resource(ip)



    def currentSet(self, current=0, OUTPUT=0):

        """

        Parameters

        ----------

        chassis : str

            'n0' or 'n1'



        current : float

            Unit is [A].



        output : int

            0 = OFF

            1 = ON



        Returns

        -------

        """

        if OUTPUT == 1:

            a = max([math.ceil(abs(current*1320)), 1])

            vol_limit = min([a, 10])
            
            #最大値と最小値
        



            self.inst.write(':SOUR:PROT:VOLT {}'.format(vol_limit))



            if abs(current) <= 1e-3:

                self.inst.write(':SOUR:RANG 1E-3')

            elif abs(current) > 1e-3 and abs(current) <= 10e-3:

                self.inst.write(':SOUR:RANG 10E-3')

            else:

                self.inst.write(':SOUR:RANG 100E-3')

        

            self.inst.write(':SOUR:LEV {}'.format(current))

            time.sleep(0.02)

            self.inst.write(':OUTP ON')

        else:

            self.inst.write(':OUTP OFF')

    

    def close(self):

        self.currentSet()

        return self.inst.close()



if __name__ == '__main__':

    ip = 'TCPIP0::192.168.2.14::inst0::INSTR'

    GS200 = GS200(ip)

    GS200.currentSecurrentSet(current=0.001, OUTPUT=1)
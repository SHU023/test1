
#created on 2019/9/17　@auther SHU
#python visa 使い方
import time
import visa
rm =visa.ResourceManager()
rm.list_resources()
instr=rm.open_resource('USB0::0x2A8D::0x0201::MY57700883::0::INSTR')


instr.write("MEAS:RES?")
instr.write("MEAS:CURR:DC?")
instr.write("MEAS:VOLT:DC?")

print(instr.query("*IDN?"))

'''
instr.write("CONF:CURR:DC 100 mA")
instr.write("CONF:VOLT:DC 100 mV")
instr.write("MEAS:VOLT:DC 100 mV")
instr.write("MEAS:CURR:DC 100 mA")
instr.write("TRIG:COUN 10")
instr.write("TRIG:SOUR EXT;SLOP POS")
instr.write("READ?")
'''


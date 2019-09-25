
#created on 2019/9/17　@auther SHU
#python visa 使い方

import visa
rm =visa.ResourceManager()
rm.list_resources()
inst=rm.open_resource('USB0::0x2A8D::0x0201::MY57700883::0::INSTR')
print(inst.query("*IDN?"))



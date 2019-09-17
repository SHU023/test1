
#created on 2019/9/17　@auther SHU
#python visa 使い方

#モジュールを入れる
#visaを使う前の呪文
#接続機器全て表示
#使用デバイスの指定writeはデバイスに命令、readは読み込み、queryは両方である
#（）の中身はSCPIプログラム
import visa
rm =visa.ResourceManager()
rm.list_resources()
inst=rm.open_resource('USB0::0x2A8D::0x0201::MY57700883::0::INSTR')
print(inst.query("*IDN?"))


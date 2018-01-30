from ControlCAN import *
from Storage import *
from multiprocessing import Process
import msvcrt


def main():
    sql = StorageToSQL()
    can = ControlCAN()
    can.opendevice()
    can.initcan()
    can.startcan()
    while 1:
        if kbq(): break
        num = can.receive()
        sql.copy(num, can.receivebuf)
        # sql.storage(num)
    del can
    del sql


def kbq():
    if msvcrt.kbhit():
        ret = ord(msvcrt.getch())
        if ret == 113 or ret == 81:  # q or Q
            return 1
    else:
        return 0


def debug():
    for f, t in Req._fields_:
        a = getattr(VCI_INIT_CONFIG, f)
        print(a)

    a = input("设备型号：1.USBCAN1(默认);2.USBCAN2;3.USBCAN2E-U;请输入:")
    if a == 1:
        devicetype = 3
    elif a == 2:
        devicetype = 4
    elif a == '':
        print(type(a))
        print(a)


if __name__ == "__main__":
    main()

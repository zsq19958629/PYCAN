# PYCAN
利用 ctypes 和周立功提供的 dll 文件实现利用 Python 控制 ZLG USBCAN 的功能。
- CANstruct.py 为对照手册定义的相关结构体
- ControlCAN.py 为对照手册定义的相关函数
- 支持的 CAN 卡为 USBCAN1、USBCAN2、USBCAN2E-U,其他CAN卡应可使用但未经测试
- 支持的函数为 opendevice、initcan、startcan、resetcan、readboardinfo、receive、transmit、readerrinfo、setreference、getreceivenum
- 工程自带周立功官网提供的64位库文件，需要使用64位 Python 调用，如需32位 Python 调用32位库文件，请下载 [zlg-can CAN_lib.rar](http://www.zlg.cn/data/upload/software/Can/CAN_lib.rar) 并替换
- 如需CANFD功能，可使用Github上另一项目 [zlgcan_py](https://github.com/guochuangjian/zlgcan_py)

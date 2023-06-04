import machine
import network
from time import sleep

lan = network.LAN(mdc=machine.Pin(23), mdio=machine.Pin(18), power=None, 
                  phy_type=network.PHY_LAN8720, phy_addr=1,
                  ref_clk=machine.Pin(17), ref_clk_mode=machine.Pin.OUT)
lan.active(True)
while(1):
    print(lan.ifconfig())
    sleep(0.5)

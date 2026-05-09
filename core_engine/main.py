# Main logic for Oasis Project 
from machine import Pin, I2C, RTC
import ssd1306
import time

# 1. Hardware Init
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
rtc = RTC()

# 2. Set Test Time (4:59:58 AM - 给你2秒准备看变化)
rtc.datetime((2026, 5, 9, 5, 4, 59, 58, 0)) 

while True:
    t = rtc.datetime()
    h, m, s = t[4], t[5], t[6]
    
    oled.fill(0)
    # Display Clock
    oled.text("TIME: {:02d}:{:02d}:{:02d}".format(h, m, s), 10, 5)
    
    # 用简单的横线代替方块 (通用性最强)
    oled.text("-" * 15, 5, 20)
    
    # 3. Growth Window Logic (5:00 AM)
    if h == 5:
        # 当 5 点时，显示内容变多并闪烁，效果同样硬核
        oled.text("!! GROWTH BOOST !!", 0, 35)
        oled.text("PUMPING WATER...", 5, 50)
    else:
        oled.text("STATUS: STABLE", 10, 35)
        oled.text("WAITING FOR DAWN", 5, 50)
        
    oled.show()
    time.sleep(1)

import machine, display, time, math, network, utime
import net as bsnet
import util as bsutil

tft = display.TFT()
tft.init(tft.ST7789,bgr=False,rot=tft.LANDSCAPE, miso=17,backl_pin=4,backl_on=1, mosi=19, clk=18, cs=5, dc=16)
tft.setwin(40,52,320,240)
for i in range(0,241):
    color=0xFFFFFF-tft.hsb2rgb(i/241*360, 1, 1)
    tft.line(i,0,i,135,color)
tft.set_fg(0x000000)
tft.ellipse(120,67,120,67)
tft.line(0,0,240,135)

txt="1221 Watt"

tft.font(tft.FONT_Comic)
tft.text(120-int(tft.textWidth(txt)/2),67-int(tft.fontSize()[1]/2),txt,0xFFFFFF)

def text(msg):
    tft.clear(tft.GREEN)
    tft.text(120-int(tft.textWidth(msg)/2),67-int(tft.fontSize()[1]/2),msg,0xFFFFFF)

text("connnecting")
text("connnecting2")

PROXY_HOST = "http://meter.nnapz.com/meter/"
PROXY_PORT = 8081

utime.sleep_ms(1500)
text("connnecting3")
while True:
    try:
        print("Starting WiFi ...")

        wlaninfo = bsnet.connectBS()
        if (wlaninfo):
            text(wlaninfo)

        bsnet.setTime()

        bsnet.mailHome("[SP-2] Started ","WLAN: " + wlaninfo + "\nFlash Mem Size: " + str(machine.heap_info())
                       + "\nFlash Id: " + str(machine.unique_id()) + "\nRead from " + PROXY_HOST + " PORT " + str(PROXY_PORT))
        #bsutil.blink(2, 'slow')

        break
    except Exception as e:
        text(str(e))
        print("Error connecting to WLAN: " + str(e))


#tft.clear(tft.BLUE)
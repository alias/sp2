import umail
import machine
import time, utime

def disconnectBS():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if wlan.isconnected():
        wlan.disconnect()


def connectBS():
    """connect to my network """
    import network
    wlan = network.WLAN(network.STA_IF)
    _ = wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        attempt_counter=60
        wlan.connect('bs', '***')
        while not wlan.isconnected():
            utime.sleep_ms(100)
            print(str(attempt_counter))
            attempt_counter -=1
            if attempt_counter == 0:     # 10 sec
                break
        if attempt_counter > 0:
            return str(wlan.ifconfig())

        return "False"

    #print('network config:', wlan.ifconfig())


def mailHome(subject , message, user='bs@oekobox-online.de', to='jknopf@gmx.de'):
    """Wlan should be connected here"""
    #print("Mail:", message)
    smtp = umail.SMTP('mail.your-server.de', 587, username=user, password='Obox3obox3_!')
    smtp.to(to)
    smtp.write("From: \"ESP Home\" <" + user + ">" + "\r\n")
    smtp.write("Subject: " + subject + "\r\n")
    smtp.write("To: " + to + "\r\n\r\n")
    smtp.write(message)
    smtp.send()
    smtp.quit()

def setTime():
    """Set Internet time, its GMT"""
    rtc = machine.RTC()
    print("Synchronize time from NTP server ...")
    rtc.ntp_sync(server="hr.pool.ntp.org")
    tmo = 100
    while not rtc.synced():
        utime.sleep_ms(100)
        tmo -= 1
        if tmo == 0:
            break


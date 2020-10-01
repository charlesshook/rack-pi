from gpiozero import Button
from gpiozero import LED
from subprocess import check_call
from signal import pause
import time
import subprocess
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import psutil

def shutdown():
    check_call(['sudo', 'shutdown', 'now'])

def reboot():
    check_call(['sudo', 'reboot'])

def main():
    poweredOnIndicator = LED("BOARD16")
    poweredOnIndicator.on()

    button = Button("BOARD5", hold_time=3)

    button.when_released = reboot
    button.when_held = shutdown

    i2c = busio.I2C(SCL, SDA)
    disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c)

    disp.fill(0)
    disp.show()

    width = disp.width
    height = disp.height
    image = Image.new("1", (width, height))

    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    padding = -2
    top = padding
    bottom = height - padding
    x = 0

    font = ImageFont.load_default()

    while True:

        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        cmd = "hostname"
        HOSTNAME =  subprocess.check_output(cmd, shell = True)
        cmd = "hostname -I | cut -d\' \' -f1"
        IP = subprocess.check_output(cmd, shell = True )
            
        CPU = "{:3.0f}".format(psutil.cpu_percent())
        svmem = psutil.virtual_memory()
        MemUsage = "{:2.0f}".format(svmem.percent)

        draw.text((x, top),       "NAME: " + HOSTNAME.decode('UTF-8'), font=font, fill=255)
        draw.text((x, top+12),    "IP  : " + IP.decode('UTF-8'),  font=font, fill=255)
        draw.text((x, top+24),    "CPU : " + CPU + "% | MEM: " + MemUsage + "%", font=font, fill=255)

        disp.image(image)
        disp.show()
        time.sleep(1)

    pause()

if __name__ == "__main__":
    main()
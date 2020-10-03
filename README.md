# Rack Pi

<p>
Rack Pi has four main features.
<ol>
    <li>OLED Display that shows the host name, IP address, CPU usage and memory usage.</li>
    <li>Button that allows you to turn the raspberry pi, reboot the pi and shut down the pi. Works like the power button on a typical computer.</li>
    <li>LED to indicate when the raspberry pi is on.</li>
    <li>Switch that cuts power to the raspberry pi. Like the switch on a typical PSU for a computer.</li>
</ol>

The case used for the Rack Pi is from a project on Thingsverse. You can find the case at:
[Link to Case]("https://www.thingiverse.com/thing:3022136")
</p>

### Setup
On the raspberry pi add this line to the end of the file at /boot/config.txt file:
```dtoverlay=i2c-gpio,bus=3,i2c_gpio_delay_us=1,i2c_gpio_sda=0,i2c_gpio_scl=1```

Install on the  adafruit circutpyton ssd1306 package on the raspberry pi:
```sudo pip3 install adafruit-circuitpython-ssd1306```




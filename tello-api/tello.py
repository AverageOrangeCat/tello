#
#   project: tello.py
#   author: Noel Kueng
#

import socket
import sys
import select


class Tello:
    def __init__(self):
        self._sock = None
        self._local_address = ('0.0.0.0', 9000)
        self._tello_address = ('192.168.10.1', 8889)
        self._TIMEOUT_MAX = 15.0

        try:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self._sock.bind(self._local_address)
            self._sock.setblocking(False)
        except socket.error:
            print("Error: could not setup socket.")
            sys.exit(1)

    def _exec_command(self, command):
        command = command.encode(encoding="utf-8")
        self._sock.sendto(command, self._tello_address)

        ready = select.select([self._sock], [], [], self._TIMEOUT_MAX)

        if ready[0]:
            try:
                data = self._sock.recv(1518)
            except socket.error:
                print("Error: something went wrong during the response time.")
                print("Command: " + str(command.decode(encoding="utf-8").split("'")[0]))
                sys.exit(1)
        else:
            print("Error: timeout has been reached.")
            print("Command: " + str(command.decode(encoding="utf-8").split("'")[0]))
            sys.exit(1)

        data_str = str(data.decode(encoding="utf-8").rstrip())
        return data_str

    #
    #   Command:
    #   command
    #
    #   Description:
    #   entry SDK mode
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def command(self):
        out = self._exec_command("command")

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   takeoff
    #
    #   Description:
    #   Tello auto takeoff
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def takeoff(self):
        out = self._exec_command("takeoff")

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   land
    #
    #   Description:
    #   Tello auto land
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def land(self):
        out = self._exec_command("land")

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   streamon
    #
    #   Description:
    #   Set video stream on
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def streamon(self):
        out = self._exec_command("streamon")

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   streamoff
    #
    #   Description:
    #   Set video stream off
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def streamoff(self):
        out = self._exec_command("streamoff")

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   emergency
    #
    #   Description:
    #   Stop all motors immediately
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def emergency(self):
        out = self._exec_command("emergency")

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   up
    #
    #   Description:
    #   Tello fly up with distance x cm
    #   x: 20-500
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def up(self, x=0):
        out = self._exec_command("up " + str(x))

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   down
    #
    #   Description:
    #   Tello fly down with distance x cm
    #   x: 20-500
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def down(self, x=0):
        out = self._exec_command("down " + str(x))

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   left
    #
    #   Description:
    #   Tello fly left with distance x cm
    #   x: 20-500
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def left(self, x=0):
        out = self._exec_command("left " + str(x))

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   right
    #
    #   Description:
    #   Tello fly right with distance x cm
    #   x: 20-500
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def right(self, x=0):
        out = self._exec_command("right " + str(x))

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   forward
    #
    #   Description:
    #   Tello fly forward with distance x cm
    #   x: 20-500
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def forward(self, x=0):
        out = self._exec_command("forward " + str(x))

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   back
    #
    #   Description:
    #   Tello fly back with distance x cm
    #   x: 20-500
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def back(self, x=0):
        out = self._exec_command("back " + str(x))

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   cw
    #
    #   Description:
    #   Tello rotate x degree clockwise
    #   x: 1-3600
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def cw(self, x=0):
        out = self._exec_command("cw " + str(x))

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   ccw
    #
    #   Description:
    #   Tello rotate x degree counter-clockwise
    #   x: 1-3600
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def ccw(self, x=0):
        out = self._exec_command("ccw " + str(x))

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   flip
    #
    #   Description:
    #   Tello fly flip x
    #   l (left)
    #   r (right)
    #   f (forward)
    #   b (back)
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def flip(self, x="f"):
        out = self._exec_command("flip " + str(x))

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   go
    #
    #   Description:
    #   Tello fly to x y z in speed (cm/s)
    #   x: 20-500
    #   y: 20-500
    #   z: 20-500
    #   speed: 10-100
    #   mid: m1-m8
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def go(self, x=0, y=0, z=0, speed=0, mid=None):
        if mid is None:
            out = self._exec_command("go " + str(x) + " " + str(y) + " " + str(z) + " " + str(speed))
        else:
            out = self._exec_command("go " + str(x) + " " + str(y) + " " + str(z) + " " + str(speed) + " " + str(mid))

        if out == "ok":
            return True
        elif out == "error No valid marker":
            return False
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   curve
    #
    #   Description:
    #   Tello fly a curve defined by the current and two given coordinates with speed (cm/s)
    #   If the arc radius is not within the range of 0.5-10 meters, it responses false
    #   x1, x2: 20-500
    #   y1, y2: 20-500
    #   z1, z2: 20-500
    #   speed: 10-60
    #   mid: m1-m8
    #   x/y/z can’t be between -20 – 20 at
    #   the same time .
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def curve(self, x1=0, y1=0, z1=0, x2=0, y2=0, z2=0, speed=0, mid=None):
        if mid is None:
            out = self._exec_command(
                "curve " + str(x1) + " " + str(y1) + " " + str(z1) + " " + str(x2) + " " + str(y2) + " " + str(
                    z2) + " " + str(speed))
        else:
            out = self._exec_command(
                "curve " + str(x1) + " " + str(y1) + " " + str(z1) + " " + str(x2) + " " + str(y2) + " " + str(
                    z2) + " " + str(speed) + " " + str(mid))

        if out == "ok":
            return True
        elif out == "error No valid marker":
            return False
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   jump
    #
    #   Description:
    #   Fly coordinates x, y and z of Mission Pad 1,
    #   and recognize coordinates 0, 0, z of Mission Pad 2
    #   and rotate to the yaw value.
    #   x:  -500-500
    #   y:  -500-500
    #   z:  -500-500
    #   speed: 10-100 (cm/s)
    #   mid: m1-m8
    #   Note x, y and z can't be set between -20-20 simultaneously.
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def jump(self, x=0, y=0, z=0, speed=0, yaw=0, mid1="mid1", mid2="mid2"):
        out = self._exec_command(
            "jump " + str(x) + " " + str(y) + " " + str(z) + " " + str(speed) + " " + str(yaw) + " " + str(
                mid1) + " " + str(mid2))

        if out == "ok":
            return True
        elif out == "error No valid marker":
            return False
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   mon
    #
    #   Description:
    #   Enable mission pad detection (both forward and downward detection).
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def mon(self):
        out = self._exec_command("mon")

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   moff
    #
    #   Description:
    #   Disable mission pad detection.
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def moff(self):
        out = self._exec_command("moff")

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   mdirection
    #
    #   Description:
    #   x = 0/1/2
    #
    #   0:  Enable downward detection only.
    #   1:  Enable forward detection only.
    #   2:  Enable both forward and downward detection.
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def mdirection(self, x=0):
        out = self._exec_command("mdirection" + str(x))

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   ap
    #
    #   Description:
    #   Set the Tello to station mode and connect to a new access point with the ssid and the password.
    #
    #   ssid = update Wi-Fi name
    #   passwd = update Wi-Fi password
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def ap(self, ssid="ssid", passwd="passwd"):
        out = self._exec_command("ap" + str(ssid) + " " + str(passwd))

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   speed
    #
    #   Description:
    #   set speed to x cm/s
    #   x: 10-100
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def speed(self, x=0):
        out = self._exec_command("speed " + str(x))

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   rc
    #
    #   Description:
    #   Send RC control via four channels.
    #   a: left/right (-100~100)
    #   b: forward/backward (-100~100)
    #   c: up/down (-100~100)
    #   d: yaw (-100~100)
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def rc(self, a=0, b=0, c=0, d=0):
        out = self._exec_command("rc " + str(a) + " " + str(b) + " " + str(c) + " " + str(d))

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   wifi
    #
    #   Description:
    #   Set Wi-Fi with SSID password
    #
    #   Possible Response:
    #   - ok
    #   - error
    #

    def wifi(self, ssid="ssid", passwd="passwd"):
        out = self._exec_command("wifi " + str(ssid) + " " + str(passwd))

        if out == "ok":
            return True
        else:
            print(out)
            sys.exit(1)

    #
    #   Command:
    #   speed?
    #
    #   Description:
    #   get current speed (cm/s)
    #
    #   Possible Response:
    #   - x: 1-100
    #

    def get_speed(self):
        return self._exec_command("speed?")

    #
    #   Command:
    #   battery?
    #
    #   Description:
    #   get current battery percentage
    #
    #   Possible Response:
    #   - x: 0-100
    #

    def get_battery(self):
        return self._exec_command("battery?")

    #
    #   Command:
    #   time?
    #
    #   Description:
    #   get current fly time (s)
    #
    #   Possible Response:
    #   - time
    #

    def get_time(self):
        return self._exec_command("time?")

    #
    #   Command:
    #   height?
    #
    #   Description:
    #   get height (cm)
    #
    #   Possible Response:
    #   - x: 0-3000
    #

    def get_height(self):
        return self._exec_command("height?")

    #
    #   Command:
    #   temp?
    #
    #   Description:
    #   get temperature (℃)
    #
    #   Possible Response:
    #   - x: 0-90
    #

    def get_temp(self):
        return self._exec_command("temp?")

    #
    #   Command:
    #   attitude?
    #
    #   Description:
    #   get IMU attitude data
    #
    #   Possible Response:
    #   - pitch roll yaw
    #

    def get_attitude(self):
        return self._exec_command("attribute?")

    #
    #   Command:
    #   baro?
    #
    #   Description:
    #   get barometer value (m)
    #
    #   Possible Response:
    #   - x
    #

    def get_baro(self):
        return self._exec_command("baro?")

    #
    #   Command:
    #   acceleration?
    #
    #   Description:
    #   get IMU angular acceleration data (0.001g)
    #
    #   Possible Response:
    #   - x y z
    #

    def get_acceleration(self):
        return self._exec_command("acceleration?")

    #
    #   Command:
    #   tof?
    #
    #   Description:
    #   get distance value from TOF（cm）
    #
    #   Possible Response:
    #   - x: 30-1000
    #

    def get_tof(self):
        return self._exec_command("tof?")

    #
    #   Command:
    #   wifi?
    #
    #   Description:
    #   get Wi-Fi SNR
    #
    #   Possible Response:
    #   - snr
    #

    def get_wifi(self):
        return self._exec_command("wifi?")

    #
    #   Command:
    #   sdk?
    #
    #   Description:
    #   Obtain the Tello SDK version.
    #
    #   Possible Response:
    #   - snr
    #

    def get_sdk(self):
        return self._exec_command("sdk?")

    #
    #   Command:
    #   sn?
    #
    #   Description:
    #   Obtain the Tello serial number.
    #
    #   Possible Response:
    #   - snr
    #

    def get_sn(self):
        return self._exec_command("sn?")

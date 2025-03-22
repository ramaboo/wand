import network

class WiFi:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password

    def connect(self):
        sta_if = network.WLAN(network.WLAN.IF_STA)
        if not sta_if.isconnected():
            print('Connecting to network...')
            sta_if.active(True)
            sta_if.connect(self.ssid, self.password)
            while not sta_if.isconnected():
                pass
        print('IP: ', sta_if.ipconfig('addr4'))

    def disconnect(self):
        print("Disconnecting ...")
        sta_if = network.WLAN(network.WLAN.IF_STA)
        sta_if.disconnect()

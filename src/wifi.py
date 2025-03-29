import network

class WiFi:
    WIFI_SSID = '8bitbunny'
    WIFI_PASSWORD = 'ass4trash'
    
    # WIFI_SSID = 'PIZZAGATE'
    # WIFI_PASSWORD = 'makeartnotwar'

    def __init__(self, ssid=WIFI_SSID, password=WIFI_PASSWORD):
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
        print('IP: ', sta_if.ipconfig('addr4')[0])

    def disconnect(self):
        print('Disconnecting from network...')
        sta_if = network.WLAN(network.WLAN.IF_STA)
        sta_if.disconnect()

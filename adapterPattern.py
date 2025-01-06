
class RoundPinCharger:
    def connect_to_round_pin(self):
        print(f"connected to round pin charger")

class USBCPinCharger:
    def connect_to_usb_pin(self):
        print(f"connected to usb pin charger")


class ChargerAdapter:
    def __init__(self, usbc_charger):
        self.usbc_charger = usbc_charger
    
    def connect_round_pin(self):
        return self.usbc_charger.connect_to_usb_pin()

if __name__ == '__main__':
    round_pin_charger = RoundPinCharger()
    round_pin_charger.connect_to_round_pin()
    
    usbc_charger = USBCPinCharger()
    adapter = ChargerAdapter(usbc_charger)
    adapter.connect_round_pin()        
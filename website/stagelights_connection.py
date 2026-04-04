from lotus_lamp import LotusLamp, DeviceConfig

# Light Congifuration
config = DeviceConfig(
    name="Stage Lights",
    address="XX:XX:XX:XX:XX:XX"  # Lamp BLE address
)
lamp = LotusLamp(device_config=config)
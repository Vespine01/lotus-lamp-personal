from lotus_lamp import LotusLamp, DeviceConfig

# Light Configuration
config = DeviceConfig(
    name="StagelightRight",
    address="BE:16:FF:00:01:A5"  # Lamp BLE address
)
lamp1 = LotusLamp(device_config=config)

# Light Configuration
config = DeviceConfig(
    name="StagelightLeft",
    address="BE:16:FF:00:0B:5A"  # Lamp BLE address
)
lamp2 = LotusLamp(device_config=config)
from lotus_lamp import LotusLamp, DeviceConfig

# Option 1: Provide config directly (no setup needed)
config = DeviceConfig(
    name="Stage Lights",
    address="XX:XX:XX:XX:XX:XX"  # Your lamp's BLE address
)
lamp = LotusLamp(device_config=config)

# Option 2: Create lotus_lamp_config.json in your project
# Then just use: lamp = LotusLamp()
import asyncio
from lotus_lamp import LotusLamp


async def connect_lamps():
    """Simpler example with error handling"""

    print("=" * 40)
    print("Stagelights Connection Log")
    print("=" * 40)
    print()

    # List of lamp names from your config
    lamp_names = ["StagelightRight", "StagelightLeft"]

    # Connect to all lamps
    lamps = []
    for name in lamp_names:
        try:
            lamp = LotusLamp(device_name=name)
            if await lamp.connect():
                lamps.append(lamp)
                print(f"✓ Connected to {name}")
            else:
                print(f"✗ Failed to connect to {name}")

        except Exception as e:
            print(f"✗ Error with {name}: {e}")


    if not lamps:
        print("No lamps connected! Error with config or Bluetooth?")

        return

    
    print("Testing connection by setting all lamps to white...")
    await asyncio.gather(*[lamp.set_rgb(0, 0, 0) for lamp in lamps])
    await asyncio.gather(*[lamp.set_rgb(240, 240, 240) for lamp in lamps])

    print("=" * 40)
    print()
    
from lotus_lamp import LotusLamp
import asyncio

async def main():
    # Create lamp controller
    lamp = LotusLamp()

    # Connect to lamp
    await lamp.connect()

    # Set color to red
    await lamp.set_rgb(255, 0, 0)

    # Disconnect
    await lamp.disconnect()

asyncio.run(main())
import asyncio
from lotus_lamp import LotusLamp
from stagelights_connection import lamp

async def red():
    # Connect to lamp
    await lamp.connect()

    # Set color to red
    await lamp.set_rgb(255, 0, 0)

async def blue():
    # Connect to lamp
    await lamp.connect()

    # Set color to blue
    await lamp.set_rgb(0, 0, 255)

async def green():
    # Connect to lamp
    await lamp.connect()

    # Set color to green
    await lamp.set_rgb(0, 255, 0)

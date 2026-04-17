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

async def white():
    # Connect to lamp
    await lamp.connect()

    # Set color to white
    await lamp.set_rgb(255, 255, 255)

async def yellow():
    # Connect to lamp
    await lamp.connect()

    # Set color to yellow
    await lamp.set_rgb(255, 255, 0)

async def purple():
    # Connect to lamp
    await lamp.connect()

    # Set color to purple
    await lamp.set_rgb(128, 0, 128)

async def orange():
    # Connect to lamp
    await lamp.connect()

    # Set color to orange
    await lamp.set_rgb(255, 165, 0)

async def pink():
    # Connect to lamp
    await lamp.connect()

    # Set color to pink
    await lamp.set_rgb(255, 192, 203)

async def cyan():
    # Connect to lamp
    await lamp.connect()

    # Set color to cyan
    await lamp.set_rgb(0, 255, 255)

async def off():
    # Connect to lamp
    await lamp.connect()

    # Turn off lamp
    await lamp.set_rgb(0, 0, 0)

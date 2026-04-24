import asyncio
from lotus_lamp.controller import LotusLamp
import stagelight_connection

async def red():
    print("\nSetting all lamps to red...")
    lamp_names = ["StagelightRight", "StagelightLeft"]

    # Connect to all lamps
    lamps = []
    for name in lamp_names:
        lamp = LotusLamp(device_name=name)
        lamps.append(lamp)

    await asyncio.gather(*[lamp.set_rgb(255, 0, 0) for lamp in lamps])

async def blue():
    print("\nSetting all lamps to blue...")
    await asyncio.gather(*[lamp.set_rgb(0, 0, 255) for lamp in stagelight_connection.lamps])

async def green():
    print("\nSetting all lamps to green...")
    await asyncio.gather(*[lamp.set_rgb(0, 255, 0) for lamp in stagelight_connection.lamps])

async def white():
    print("\nSetting all lamps to white...")
    await asyncio.gather(*[lamp.set_rgb(255, 255, 255) for lamp in stagelight_connection.lamps])

async def yellow():
    print("\nSetting all lamps to yellow...")
    await asyncio.gather(*[lamp.set_rgb(255, 255, 0) for lamp in stagelight_connection.lamps])

async def purple():
    print("\nSetting all lamps to purple...")
    await asyncio.gather(*[lamp.set_rgb(128, 0, 128) for lamp in stagelight_connection.lamps])

async def orange():
    print("\nSetting all lamps to orange...")
    await asyncio.gather(*[lamp.set_rgb(255, 165, 0) for lamp in stagelight_connection.lamps])

async def pink():
    print("\nSetting all lamps to pink...")
    await asyncio.gather(*[lamp.set_rgb(255, 192, 203) for lamp in stagelight_connection.lamps])

async def cyan():
    print("\nSetting all lamps to cyan...")
    await asyncio.gather(*[lamp.set_rgb(0, 255, 255) for lamp in stagelight_connection.lamps])

async def off():
    print("\nTurning all lamps off...")
    await asyncio.gather(*[lamp.set_rgb(0, 0, 0) for lamp in stagelight_connection.lamps])

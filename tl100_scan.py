import asyncio
from bleak import BleakScanner

async def main():
    print("Suche nach Bluetooth-Geräten...")
    devices = await BleakScanner.discover()
    for d in devices:
        print(f"{d.name} - {d.address}")

asyncio.run(main())
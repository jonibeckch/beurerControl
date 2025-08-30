import asyncio
from bleak import BleakClient

address = "57:4C:42:C6:DD:83"  # MAC-Adresse deiner TL100

async def main():
    async with BleakClient(address) as client:
        print(f"Verbunden: {client.is_connected}")
        services = await client.get_services()
        for service in services:
            print(f"[Service] {service}")
            for char in service.characteristics:
                print(f"  [Char] {char} ({' '.join(char.properties)})")

asyncio.run(main())
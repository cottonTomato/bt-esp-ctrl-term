import sys
import asyncio
from bleak import BleakClient


esp_uuid = "13ba3f62-c58d-43e9-b127-a47bb86bef72"

char_uuid = {
    "A": "c54f2186-0d10-44c6-9a91-63a98b675999",
    "B": "b03f8c79-d53d-4158-be1d-7d878596db58",
}

operations = {"stA": 1, "stB": 2, "clA": 3, "clB": 4, "gtA": 5, "gtB": 6}


async def main(operation: int):
    async with BleakClient(esp_uuid) as client:
        match (operation):
            case 1:
                await client.write_gatt_char(char_uuid["A"], b"1", response=False)
            case 2:
                await client.write_gatt_char(char_uuid["B"], b"1", response=False)
            case 3:
                await client.write_gatt_char(char_uuid["A"], b"0", response=False)
            case 4:
                await client.write_gatt_char(char_uuid["B"], b"0", response=False)


if len(sys.argv) != 2:
    print("usage: {} <opreation>".format(sys.argv[0]))

operation = sys.argv[1]

if operation not in operations.keys():
    print("usage: invalid operation")
    sys.exit(1)

asyncio.run(main(operations[operation]))

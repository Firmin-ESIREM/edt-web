from requests import get
from asyncio import sleep


async def pull(elements):
    while True:
        for element in elements:
            x = get(element["url"])
            if x.status_code == 200:
                ics_content = x.content.decode("utf-8")
                with open(element["name"] + ".ics", 'w') as f:
                    f.write(ics_content)
        await sleep(300)

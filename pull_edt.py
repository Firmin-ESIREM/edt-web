from requests import get
from time import sleep


def pull(elements):
    while True:
        for element in elements:
            try:
                x = get(element["url"])
                if x.status_code == 200:
                    ics_content = x.content.decode("utf-8")
                    with open("ics/" + element["name"] + ".ics", 'w') as f:
                        f.write(ics_content)
            except:
                pass
        sleep(300)

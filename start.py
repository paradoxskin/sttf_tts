import requests
from tqdm import trange
from time import sleep
options = input("[?] [W]ork or [r]epear: ")
url = "https://translate.google.com/translate_tts?ie=UTF-8&&client=tw-ob&tl=zh-TW&q={}"
if options in ["r" , "R"]:
    with open("error.txt") as file:
        words = list(filter(lambda x: x!= "", file.read().split("\n")))
    for i in trange(len(words)):
        sp = words[i].split(":")
        (idx, one) = (sp[0], ":".join(sp[1:]))
        try:
            if one == "":
                continue
            resp = requests.get(url.format(one))
            with open(f"./output/{idx}.mpeg", "wb") as file:
                file.write(resp.content)
        except:
            with open("error.txt", "a+") as file:
                file.write(f"{idx}: {one}\n")
            flag = True
        sleep(.2)

else:
    with open("input.txt") as file:
        words = list(filter(lambda x: x!= "", file.read().split("\n")))
    with open("error.txt", "w") as file:
        pass
    flag = False
    for idx in trange(len(words)):
        one = words[idx]
        try:
            if one == "":
                continue
            resp = requests.get(url.format(one))
            with open(f"./output/{idx}.mpeg", "wb") as file:
                file.write(resp.content)
        except:
            with open("error.txt", "a+") as file:
                file.write(f"{idx}: {one}\n")
            flag = True
        sleep(.2)
    if flag:
        print("[x] something wrong")
    else:
        print("[+] done.")

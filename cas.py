from time import sleep
from rich import print 

def typing(text, delay, color):
    for i in text:print("[{}]{}".format(color, i), end="");sleep(delay)

def lyrics():
    lines = [
        ("ooh-oh\n", 0.4, 0.8),
        ("when you're all alone\n", 0.2, 0.7),
        ("i will reach for you\n", 0.2, 1),
        ("when you're feeling low\n", 0.2, 0.8),
        ("i will be there too\n", 0.2, 0.8),
    ]
    color = ["white"]
    for ex, (lyric, typing_delay, lyric_delay) in enumerate(lines):
        color = color[(ex // 4) % len(color)]
        typing(lyric, typing_delay, color)
        sleep(lyric_delay)

if __name__ == "__main__":
    lyrics()
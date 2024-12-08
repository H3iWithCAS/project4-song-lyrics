import sys
from time import sleep

def lyrics():
    lines = [
        ("know you're all that i want - this life", 0.10),
        ("i'll imagine we fell in love", 0.09),
        ("i'll nap under moonlight skies with you", 0.06),
        ("i think I'll picture us, you with the waves", 0.08),
        ("the ocean's colors on your face", 0.06),
        ("i'll leave my heart with your air", 0.08),
        ("so let me fly with you", 0.08),
        ("will you be forever with me?", 0.10)
    ]
    delays = [3, 0.5, 1.3, 0.5, 1.5, 1.5, 2, 3.5]

    for i, (line, delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(delay)
        sleep(delays[i])
        print('')

lyrics()            
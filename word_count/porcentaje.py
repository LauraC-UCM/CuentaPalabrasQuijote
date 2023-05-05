import random
import sys

def main(ratio):
    with open('quijote.txt') as infile:
        with open('quijote_s05.txt', 'w') as outfile:
            for line in infile:
                if random.random()<=ratio:
                    outfile.write(line)


if __name__=="__main__":
    
    ratio = random.random()
    main(ratio)

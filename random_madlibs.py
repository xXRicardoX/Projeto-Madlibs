from sample_madlibs import hp, code, Zombie, hungergames
import random

if __name__ == "__main__":
    m = random.choice([hp, code, Zombie, hungergames])
    m.madlib()
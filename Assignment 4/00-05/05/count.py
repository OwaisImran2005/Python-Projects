import random

DONE_LIKELIHOOD = 0.2 

def chaotic_counting():
    for i in range(10):
        if done():
            return
        curr_num = i + 1
        print(curr_num)

def done():
    """Returns True with a probability of DONE_LIKELIHOOD"""
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
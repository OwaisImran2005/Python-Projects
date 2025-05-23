def average(a: float, b: float):

    sum = a + b
    return sum / 2

def main():
    avg_1 = average(10, 15)
    avg_2 = average(8, 16)
    
    final = average(avg_1, avg_2)
    print("average1", avg_1)
    print("average2", avg_2)
    print("Final", final)
    


if __name__ == '__main__':
    main()
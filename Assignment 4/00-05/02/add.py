def add_many_numbers(numbers)-> int:
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number

    return total_so_far

def main():
    numbers: list[int] = [10, 20, 30, 40, 50]  
    sum_of_numbers: int = add_many_numbers(numbers)  
    print(sum_of_numbers)  
    

if __name__ == '__main__':
    main()
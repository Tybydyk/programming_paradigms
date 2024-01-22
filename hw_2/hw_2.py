#   the procedural paradigm
def multiplication_table(num):
    for i in range(1, n + 1):
        print('\n'.join([f'{i: >3} * {j: >3} = {i * j:>6}' for j in range(1, n + 1)]))
        print('')


if __name__ == '__main__':
    n = int(input("Enter a positive integer number from 1  to 999 : "))

    #   the structural paradigm
    print('The structural paradigm')
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f'{i: >3}  * {j: >3} = {i * j:>6}')
        print('')

    #   the procedural paradigm
    print('The procedural paradigm')
    multiplication_table(n)
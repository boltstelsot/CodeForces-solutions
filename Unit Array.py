for t in range(int(input())):
    n = int(input())
    l = input().split(' ')
    number_of_operations=0
    sum_plus = l.count('1')
    sum_minus = -l.count('-1')
    l_sum = sum_plus + sum_minus
    if l_sum<0:                                 #checking the first condition
        if len(l)&1 == 0:
            number_of_operations += -l_sum//2
            sum_plus += number_of_operations
            sum_minus += number_of_operations
        else:
            number_of_operations += (1-l_sum)//2
            sum_plus += number_of_operations
            sum_minus += number_of_operations
    if sum_minus % 2 == 1:                      #checking the second condition
        number_of_operations += 1

    print(number_of_operations)
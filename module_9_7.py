def is_prime(func):
    def three(*args):
        result_func = func(*args)
        is_prime = True
        for k in range(2, result_func):
            if result_func % k == 0:
                is_prime = False
                break
        if is_prime:
            print('Простое')
        else:
            print('Составное')
        return result_func
    return three

@is_prime
def sum_three(*args):
    sum_ = sum(args)
    return sum_

result = sum_three(2, 3, 6)
print(result)
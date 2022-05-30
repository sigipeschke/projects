def oper(x):
        if x%2 == 0:
            return x//2
        else:
            return 3*x+1
    
def main(x):
    iter = 0
    max_num = 0
    seq = []
    while x != 1:
        iter += 1
        seq.append(x)
        if x > max_num:
            max_num = x
        x = oper(x)
    print('Sequence terminated. A max value =', max_num, 'was reached in', iter, 'iterations.')
    print('The sequence consisted of', seq)
    

main(3)


    


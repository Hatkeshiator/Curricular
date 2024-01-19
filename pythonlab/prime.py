def isprime(num):
    ran = range(2, int(num ** (1/2)) + 1)
    prime = True
    #print(ran)
    for i in ran:
        if not prime:
            break
        #print("i =", i)
        for j in range(num):
            #print("  j =", j) 
            if i * j == num:
                #print('    ',i,'*',j,'=',i*j,'which is equal to',num)
                prime = False
                break
            #else:
                #print('    ',i,'*',j,'=',i*j)
    return prime

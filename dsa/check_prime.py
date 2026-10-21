def check_prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print("not prime")
                break
        else:
            print("prime")
            
n=4
(check_prime(n))
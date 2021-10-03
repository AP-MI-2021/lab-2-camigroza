def get_largest_prime_below(n):
    '''
    Gaseste ultimul numar prim mai mic decat un numar dat
    :param n: un numar natural
    :return: numarul cerut
    '''
    for i in range (n-1,1,-1):
        stop=0
        for j in range (2,n%2+1):
            if i%j==0:
                stop=1
        if stop==0:
            return(i)

def test_get_largest_prime_below():
    '''
    Functia de test
    '''
    assert get_largest_prime_below(20) == 19
    assert get_largest_prime_below(3) == 2
    assert get_largest_prime_below(100) == 97

a=int(input("Dati numarul: "))
while a!=-1:
    print (get_largest_prime_below(a))
    a=int(input("Dati alt numar: "))
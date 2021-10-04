def is_palindrome(n):
    '''
    Determina daca un numar dat este palindrom
    :param n: un numar natural
    :return: True, daca n este palindrom, False in caz contrar
    '''
    ogl=0
    c=n
    while n!=0:
        ogl=ogl*10+n%10
        n=n//10
    if c==ogl:
        return True
    else:
        return False

def test_is_palindrome():
    '''
    Functia de test
    '''
    assert is_palindrome(123) == False
    assert is_palindrome(12321) == True
    assert is_palindrome(5) == True
    assert is_palindrome(7887) == True
    assert is_palindrome(244) == False

a=int(input("Dati numarul: "))
while a!=-1:
    print (is_palindrome(a))
    a=int(input("Dati alt numar: "))



def get_largest_prime_below(n):
    '''
    Gaseste ultimul numar prim mai mic decat un numar dat
    :param n: un numar natural
    :return: numarul cerut
    '''
    for i in range (n-1,1,-1):
        stop=0
        for j in range (2,n//2+1):
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



def is_prime(n):
    '''
    Determina daca un numar este prim
    :param n: un numar natural
    :return: True, daca n este prim, False in caz contrar
    '''
    if n<2:
        return False
    else:
        stop=0
        for i in range (2,n//2+1):
            if n%i==0:
                stop=1
        if stop==0:
            return True
        else:
            return False

def is_superprime(n):
    '''
    Determina daca un numar este superprim
    :param n: un numar natural
    :return: True, daca n este superprime, False in caz contrar
    '''
    ok=0
    while n!=0:
        if is_prime(n) == False:
            ok=1
        n=n//10
    if ok==0:
        return True
    else:
        return False

def test_is_superprime():
    assert is_superprime(233) == True
    assert is_superprime(237) == False
    assert is_superprime(3) == True

a=int(input("Dati numarul: "))
while a!=-1:
    print (is_superprime(a))
    a=int(input("Dati alt numar: "))
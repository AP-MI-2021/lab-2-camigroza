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
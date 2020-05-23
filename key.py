import random

# Global Variable g
# Key Will be generated in form _p g _d
_g=2

def generatePrimeNumber():  

    # We are generating a prime number  (31 bit)
    # starting from 1, and ending to 1
    # It cannot start or end from 0
    # So we need to add 1 in start and 1 in end, and remaining 29 numbers can be any 1 or 0
    primeNumber = "1"
    # Fill remaining with any bit
    for i in range(29):
        primeNumber += str(random.randint(0, 1))
    # Add 1 to end of prime number
    primeNumber += "1"
    # Convert this number back to base 2
    primeNumber = int(primeNumber,2)
    # return the prime number
    return primeNumber


def isMillerRabin(n):

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1

    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(64):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break

        else:
            return False

    return True


# Below function generated the keys in form _p g d

def keyGenerator():
    # Let initially P = 10
    _p = 10
    # Check is _p is not millerRabin
    while not isMillerRabin(_p):
        # Add a temp variable 
        temp = 10

        while ((temp % 12) != 5) or (not isMillerRabin(temp)):
            temp = generatePrimeNumber()

        _p = (2 * temp) + 1
    # Get _d
    _d = random.randint(1, _p)

    _e2 = pow(_g, _d, _p)

    pubKey= str(_p) + " " + str(_g) + " " + str(_e2)
    priKey= str(_p) + " " + str(_g) + " " + str(_d)
    open("prikey.txt", 'w').write(priKey)
    open("pubkey.txt", 'w').write(pubKey)

    print ("Public key=", pubKey, "            Private key=", priKey)
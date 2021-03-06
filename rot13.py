import os
def dencrypt(s: str, n: int = 13):
    """
    https://en.wikipedia.org/wiki/ROT13

    >>> msg = "My secret bank account number is 173-52946 so don't tell anyone!!"
    >>> s = dencrypt(msg)
    >>> s
    "Zl frperg onax nppbhag ahzore vf 173-52946 fb qba'g gryy nalbar!!"
    >>> dencrypt(s) == msg
    True
    """
    out = ""
    for c in s:
        if "A" <= c <= "Z":
            out += chr(ord("A") + (ord(c) - ord("A") + n) % 26)
        elif "a" <= c <= "z":
            out += chr(ord("a") + (ord(c) - ord("a") + n) % 26)
        else:
            out += c
    return out


def main():
    os.system("clear")
    s0 = input("Enter message: ")

    s1 = dencrypt(s0, 13)
    print("Encrypted:", s1)



    s2 = dencrypt(s1, 13)
    print("Decrypted: ", s2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()

from numb3rs import validate

# def main():
#     test_valid()
#     test_invalid()
#     test_pattern()

def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True

def test_invalid():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("255.256.256.256") == False

def test_pattern():
    assert validate("cat") == False

# if __name__ == "__main__":
#     main()

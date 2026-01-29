from seasons import check_birth_date


def main():
    test_check_birth_date()

def test_check_birth_date():
    assert check_birth_date("1998-07-02") == (1998, 7, 2)
    assert check_birth_date("1998-7-2") == None
    assert check_birth_date("July 3, 1998") == None

if __name__ == "__main__":
    main()

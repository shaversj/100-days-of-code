from __init__ import Tour


def main():
    t1 = Tour('New York, NY', 'Lansing, MI', 'Sacramento, CA')
    t2 = Tour('New York, NY', 'Sacramento, CA')

    print(t1.__str__())
    print(t2.__str__())
    print()
    print(t1)
    print(t2)
    print()
    print(repr(t1))


if __name__ == '__main__':
    main()

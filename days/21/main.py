from __init__ import Tour


def main():
    t1 = Tour('New York, NY', 'Lansing, MI', 'Sacramento, CA')
    t2 = Tour('New York, NY', 'Sacramento, CA')

    print(t1.destination)
    print(t1.__str__())
    print(t2.__str__())
    print()
    print(t1)
    print(t2)
    print()
    print(repr(t1))
    print()
    # print("|".join(t1.destination))
    print(t1.distance())

    """
    print("t1: {}\nt2:{}\nt3:{}".format(t1,t2,t3))
    print("t1 distances: driving-{} km; biking-{} km; walking-{} km".format(
    round(t1.distance()/1000), round(t1.distance('bicycling')/1000), round(t1.distance('walking')/1000)))

    print("Using driving distances from here on.")
    t4 = t1 + t2
    print("t4:", t4)
    print("t4 driving distance:", round(t4.distance()/1000),"km") print("t4 == t1 + t2:", t4 == t1 + t2)

    """
    # print(t1)
    # print("t1 distances: driving-{} km; biking-{} km; walking-{} km".format(round(t1.distance()/1000), round(t1.distance('bicycling')/1000), round(t1.distance('walking')/1000)))


if __name__ == '__main__':
    main()

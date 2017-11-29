if __name__ == "__main__":
    initialvalue, time = map(int, raw_input().split())
    candiestoremove = map(int, raw_input().split())
    total = initialvalue
    replenished = 0
    for i in xrange(time-1):
        total = total - candiestoremove[i]
        if total < 5:
            replenished += initialvalue - total
            total = initialvalue

    print replenished

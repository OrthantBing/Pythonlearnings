if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    def second_largest(arr):
        count = 0
        m1 = m2 = float('-inf')
        for i in arr:
            if i == m1 or i == m2:
                continue
            count += 1
            if i > m1:
                if i > m2:
                    m2, m1 = i, m2
                else:
                    m1 = i
        return m1 if count >= 2 else None
    print second_largest(arr)




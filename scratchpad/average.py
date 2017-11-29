if __name__ == '__main__':
    n = int(raw_input())
    studentmarks = {}
    for _ in range(n):
        line = raw_input().split(" ")
        name, marks = line[0], line[1:]
        marks = map(int, marks)
        studentmarks[name] = marks

    query_name = raw_input()
    val = reduce((lambda x, y: x + y), studentmarks[query_name]) /5
    print "%.2f" % val
    
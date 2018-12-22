if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        sentence = input().split(".")
        reveresed = ".".join(map(lambda x: x[::-1], sentence))
        print (reveresed)

    
            

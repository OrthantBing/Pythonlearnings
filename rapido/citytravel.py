def finddistance(totalcities, citiestocheck, startlocation, distance):
    graph = dict()
    visited = dict()
    for c in totalcities:
        graph[c] = []
        visited[c] = False

    sortedcities = sorted(totalcities)
    # lets find what all places we can go from every location in the city
    for i in range(len(sortedcities)):
        j = i+1
        while j < len(sortedcities) and sortedcities[j] - sortedcities[i] <= distance:
            graph[sortedcities[i]].append(sortedcities[j])
            graph[sortedcities[j]].append(sortedcities[i])
            j += 1

    explore(graph, visited, startlocation)

    counter = 0
    for i in citiestocheck:
        if visited[i]:
            counter += 1

    return counter
    

def explore(adj, visited, node):
    print(adj, visited, node)
    visited[node] = True
    for n in adj[node]:
        if not visited[n]:
            explore(adj, visited, n)


if __name__ == '__main__':
    # Test case count
    t = int(input())
    # N, K, Q
    n, k, q = list(map(int, input().split()))
    array = list(map(int, input().split()))
    for _ in range(q):
        l, r, x = list(map(int, input().split()))
        citiestocheck = array[l-1:r]

        startlocation = array[x-1]
        # print(citiestocheck, startlocation, x)
        print(finddistance(array, citiestocheck, startlocation, k))

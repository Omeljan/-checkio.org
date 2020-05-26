'''
You are given the current stock prices. You have to find out which stocks cost more.
'''
def best_stock(data):
    best_list = list(data.items())
    best_list.sort(key = lambda i: i[1], reverse = True)
    return best_list[0][0]


if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

#These "asserts" are used foыr self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")

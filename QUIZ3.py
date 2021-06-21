prime_result= list(filter(
    None,
    [
        _list[-1] if all([False if _list[-1] != k and _list[-1] % k == 0 else _list[-1] for k in _list]) else None
        for _list in [[j for j in range(2, i+1)] for i in range(2, 1001)]
    ]
))

print(prime_result)
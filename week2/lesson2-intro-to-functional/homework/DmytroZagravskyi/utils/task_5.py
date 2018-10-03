def makeStats(p_list: list) -> set:
    return \
        (
            sum(list(map(lambda p: p['age'], p_list))),
            min(p_list, key=lambda p: p['age']),
            max(p_list, key=lambda p: p['age'])
        )


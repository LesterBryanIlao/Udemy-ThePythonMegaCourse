def mean(iterable):
    if isinstance(iterable, dict):
        return sum(iterable.values())/len(iterable)
    return sum(iterable)/len(iterable)

new_list = [1, 4, 6]
new_dict = {"one":1, "four": 4, "six": 6}
print(mean(new_list) + 10)
print(mean(new_dict) + 10)

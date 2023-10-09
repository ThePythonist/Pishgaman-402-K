scores = {
    "sakhteman dadeh": 18,
    "mohandesi narmafzar": 16,
    "vasaya": 13,
    "nazarie zabanha": 8,
    "mabani computer": 20,
}

for k, v in scores.items():
    if v >= 10:
        print(k, ": Passed :", v)
    else:
        print(k, ": Failed :", v)

avg = sum(scores.values()) / len(scores)
print(avg)
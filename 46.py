ages = {
    "sara": 18,
    "zeynab": 22,
    "meysam": 21,
    "jamshid": 45,
    "soheila": 20,
}

oldest = max(ages.values())

for i in ages:
    if ages[i] == oldest:
        print(i)

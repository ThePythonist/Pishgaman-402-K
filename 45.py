class_k = {
    "teacher": "sadeghi",
    "students": [1, 2, 3, 4, 5, 6, 7],
    "course": "python",
    "level": "intermediate",
    "academy": "takht jamshid",
}

key = input("Search any key : ")

if key in class_k:
    print(class_k[key])
else:
    print("Key Not Found")

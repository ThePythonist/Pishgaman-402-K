def make_files(n, f):
    for i in range(number):
        open(f"{i + 1}.{frmt}", "w")

    print("Done")


number = int(input("How many files ? "))
frmt = input("Enter the format of files : ")
make_files(number, frmt)

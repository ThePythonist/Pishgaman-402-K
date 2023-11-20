lines = open("words.txt").read().split("\n")
open("onelinewords.txt","w").writelines(lines)
print('Done')

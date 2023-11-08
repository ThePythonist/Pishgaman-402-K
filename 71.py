def sendwarning(phonenumber):
    product = "10Gb 7 Roozeh"
    percentage = 85
    text = f"Moshtarak gerami {phonenumber} shoma {percentage} darsad az basteye {product} masraf kardid"
    return text


phonenumbers = ["09936234040", "09216781030", "09190120567"]
msg = list(map(sendwarning, phonenumbers))
for i in msg:
    print(i)

input_main = input("Enter cells:")
list_main = list(input_main)
a = (list_main[0], list_main[1], list_main[2])
b = (list_main[3], list_main[4], list_main[5])
c = (list_main[6], list_main[7], list_main[8])
finalString = ' '.join(a)
finalString_2 = ' '.join(b)
finalString_3 = ' '.join(c)
print(f"""\
---------
| {finalString  } |
| {finalString_2} |
| {finalString_3} |
---------
""")

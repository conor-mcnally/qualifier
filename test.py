rows = [["Lemon", "second tag", 12],
        ["Sebastian", -13, "another tag"],
        ["conor conor", "and another one", 12],
        ["conor 2", "yep, again", 12],
        ["conor3", "t", 12]]

rows2 = [["Lemon", "second tag"],
        ["Sebastian", -13],
        ["conor conor", "and another one"],
        ["conor 2", "yep, again"],
        ["conor3", "t"]]

rows3 = [["Lemon"],
        ["Sebastian"],
        ["conor conor"],
        ["conor 2"],
        ["conor3"]]


labels=["User", "Messages", "Role"]
# Convert all entries to string
labels = list(map(str, labels))
rows = [[str(x) for x in a] for a in rows]


longestEntryLabel = max(labels, key=len)
maxLengthLabel = len(longestEntryLabel)
maxLengthRow = max(len(str(i)) for sublist in rows for i in sublist)
print("maxLengthRow =" , maxLengthRow)
maxLength = max(maxLengthLabel, maxLengthRow)

# print("Max Length Row:", maxLengthRow, "Max length label: ", maxLengthLabel, "Max Length: ", maxLength)

totalLenOfLabels = sum(len(i) for i in labels)

if len(labels) > 1:
    # Top Line
    print("┌" + ("─"*maxLength + "┬")*(len(labels)-1) + "─"*maxLength + "┐")

    # Left Wall
    print("│", end="")

    # Labels
    for i in labels:
        print(i + " "*(maxLength-len(str(i))) + "│", end="")

    # Divider
    print("\n├" + ("─"*maxLength + "┼")*(len(labels)-1) + "─"*maxLength + "┤")

    # Rows
    # for i in rows:
    #     for j in i:
    #         print("│" + str(j) + " "*(maxLength-len(str(j))) ,end="")

    # Left Wall
    print("│", end="")
    
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            print(rows[i][j] + " "*(maxLength-j) + "│", end = '')

elif len(labels) == 1:
    # Top Line
    print("┌" + ("─"*maxLength) + "┐")

    # Labels
    for i in labels:
        print(i + " "*(maxLength-len(str(i))) + "│", end="")

    # Divider
    print("\n├" + ("─"*maxLength + "┼")*(len(labels)-1) + "─"*maxLength + "┤")

    # Body

else:
    # Print just rows no labels included - so top line + rows + bottom line 
    print("")

# # Table Header
# print("┌" + ("─"*(totalLenOfLabels*int(1.3))*len(labels)) + "┐")

# # Labels
# for i in labels:
#     print("│", i, " "*(12-len(i)), "│")

# # Divider
# print("├" + "─"*(totalLenOfLabels) + "┤")

# # First entry

# # Rest of entries

# # Main items
# for items in rows:
#     print("│", items[0], " "*(12-len(str(items[0]))), "│",
#     items[1], " "*(12-len(str(items[0]))), "|",
#     items[2], " "*(12-len(str(items[0]))), "|"
#     )

# print()


# for item in rows:
#     for i in item:
#         columnWidth = maxLengthRow-len(str(i))
#         print("│", i, " "*columnWidth, "|")

# tableChars = "│ ─ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘"

# # Footer
# print("└" + "─"*(totalLenOfLabels*2) + "┘")

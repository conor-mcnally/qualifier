rows = [["Lemon", "second tag", 12],
        ["Sebastian", -13, "another tag"],
        ["conor conor", "and another one", 12],
        ["conor 2", "yep, again", 12],
        ["conor3", "t", 12]]

labels=["User", "Messages", "Role"]
print(len(labels))

totalLenOfLabels = sum(len(i) for i in labels)

# Table Header
print("┌" + ("─"*(totalLenOfLabels*int(1.3))*len(labels)) + "┐")

# Labels
for i in labels:

    print("│", i, " "*(12-len(labels[0])), "│")

# Divider
print("├" + "─"*(totalLenOfLabels*2) + "┤")

# Main items
for items in rows:
    print("│", items[0], " "*(12-len(str(items[0]))), "│",
    items[1], " "*(12-len(str(items[0]))), "|",
    items[2], " "*(12-len(str(items[0]))), "|"
    )

tableChars = "│ ─ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘"

# Footer
print("└" + "─"*(totalLenOfLabels*2) + "┘")

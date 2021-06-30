from typing import Any, List, Optional

# Main function
def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    
    # Convert to string
    rows = [[str(x) for x in a] for a in rows]

    if labels != None:
        # Convert to string
        labels = list(map(str, labels))
        # Get lengths
        maxLengthLabel = len(max(labels, key=len))
        maxLengthRow = max(len(str(i)) for sublist in rows for i in sublist)
        maxLength = max(maxLengthLabel, maxLengthRow)
    elif labels == None :
        maxLength = max(len(str(i)) for sublist in rows for i in sublist)
        print("┌" + "─"*maxLength + "┐")

    def print_row(rows):
        return "│" + "│".join(f' {x} '+ " "*(maxLength - len(x)) for x in rows)  + "│"

    def print_board(arr):
        return '\n'.join(print_row(rows) for rows in arr) + "\n"

    def print_footer(labels: Optional = None):
        if labels != None:
            if len(labels) == 1:
                return "└" + "─"*(maxLength) + "┘"
            elif len(labels) >= 2:
                return "└" + ("─"*(maxLength+2) + "┴")*(len(labels)-1) + "─"*(maxLength+2) + "┘"
            else:
                pass
        elif labels == None:
            return "└" + "─"*maxLength + "┘"

    def print_label(labels: Optional = None):
        if labels != None:
            if len(labels) > 1:
                # Top Line
                print("┌" + ("─"*(maxLength+2) + "┬")*(len(labels)-1) + "─"*(maxLength+2) + "┐")
                # Left Wall
                print("│", end="")
                # Labels
                for i in labels:
                    print(" " + i + " "*(maxLength-len(str(i))+1) + "│", end="")
                # Divider
                print("\n├" + ("─"*(maxLength+2) + "┼")*(len(labels)-1) + "─"*(maxLength+2) + "┤")
            elif len(labels) == 1:
                # Top Line
                print("┌" + ("─"*maxLength) + "┐")
                # Labels
                for i in labels:
                    print(i + " "*(maxLength-len(str(i))) + "│", end="")
                # Divider
                print("\n├" + ("─"*maxLength + "┼")*(len(labels)-1) + "─"*maxLength + "┤")
        else:
            print("┌" + ("─"*maxLength) + "┐")

    print_label(labels)
    print(print_board(rows), end='')
    print(print_footer(labels))

# Dummy Data
rows = [
        ["Lemon", "Sugar", "Honey"],
        ["Sebastian", "Dimitri", "Technology"],
        ["conor", "dervla", "jack"]
    ]
labels=["User", "Messages", "Role"]

rows4 = [
        ["Lemon", "Sugar", "Honey", "Jam"],
        ["Sebastian", "Dimitri", "Technology", "Vladimir"],
        ["conor", "dervla", "jack", "Spare room"]
    ]
labels4=["User", "Messages", "Role", "Field"]

rows1 = [
        ["Lemon"],
        ["Sebastian"],
        ["conor"]
    ]
labels1=["User"]


# Run
make_table(rows, labels)
make_table(rows4, labels4)

# Notes to self
# Labels is your headers, so put them first, they are optional
# Rows is essential data
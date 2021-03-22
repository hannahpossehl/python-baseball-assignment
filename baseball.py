import re
import sys, os
ba_regex = re.compile(r"([A-Z][A-Za-z]+ [A-Z][A-Za-z]+) \bbatted\b (\d) \btimes\b \bwith\b (\d)")
average = {}
at_bats_dict = {}
hits_dict = {}
def calculate_average():
    for name in average:
        average[name]= hits_dict[name]/at_bats_dict[name]
    return
def read_file(filename):
    with open(filename) as f:
        for line in f:
            match = ba_regex.match(line)
            if match is not None:
                name = match.group(1)
                at_bats = int(match.group(2))
                hits = int(match.group(3))
                if name in average:
                    hold = at_bats_dict[name]
                    hold_hits = hits_dict[name]
                    at_bats_dict[name]=hold + at_bats
                    hits_dict[name] = hold_hits + hits       
                else:
                        average[name]= 0
                        at_bats_dict[name]= at_bats
                        hits_dict[name] = hits
    calculate_average()
    return

def print_values():
    #help with sorting a dictionary by value https://careerkarma.com/blog/python-sort-a-dictionary-by-value/#:~:text=To%20sort%20a%20dictionary%20by%20value%20in%20Python,They%20use%20a%20mapping%20structure%20to%20store%20data.
    sorted_average = sorted(average.items(), key=lambda x: x[1], reverse=True)
    for i in sorted_average:
        print(i[0], ":", '{:.3f}'.format(round(i[1], 3)))  
    return

if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} filename")
filename = sys.argv[1]
if not os.path.exists(filename):
        sys.exit(f"Error: File '{sys.argv[1]}' not found")

read_file(filename)
print_values()
        



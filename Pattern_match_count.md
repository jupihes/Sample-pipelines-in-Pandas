Code to find 
- count **Pattern match** and **not-match** in a file
- provide first n records of **not-match** items

```python
import re

pattern = r"(?m)^98\d{10},[A-Z-1-9]{3,},A,([1-3]|[1-2][0-9]|[3][0-1]),[0-2],0,[0-1](((?:,)(?:\d{8,10})+)?)+$"
def Pattern_match(file_name, pattern, n=10):
    matched_records = 0
    non_matched_records = 0
    non_matched_list = []
    
    # Open the input file
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
    
            # Check if the line matches the pattern
            if re.search(pattern, line):
                matched_records += 1
            else:
                non_matched_records += 1
                non_matched_list.append(line)
    
    # Print the results
    print("Count of matched records:", matched_records)
    print("Count of non-matched records:", non_matched_records)
    print("Ten first non-matched records:")
    # for record in non_matched_list[:10]:
    #     print(record)
    
    return matched_records, non_matched_records, non_matched_list[:n]

Pattern_match("sample_input.csv", pattern)
Pattern_match("Wlist_Myirancell_four_hours_free.csv", pattern)

Pattern_match("sample_input.txt", pattern)
```

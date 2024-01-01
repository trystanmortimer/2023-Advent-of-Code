import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

word_lookup = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

word_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def digits(line) -> dict:
    
    matches = re.finditer("\d", line)
    match_list = []
    result = {}
    
    for match in matches: 
        match_list.append(match)
    
    result[match_list[0].start()] = match_list[0].group()
    result[match_list[-1].start()] = match_list[-1].group()
    
    return result

def words(line, word_list) -> dict:
    
    result = {}

    for word in word_list:
        matches = re.finditer(word, line)
        match_list = []

        for match in matches:
            match_list.append(match)

        if len(match_list) > 0:
            result[match_list[0].start()] = word_lookup[match_list[0].group()]
            result[match_list[-1].start()] = word_lookup[match_list[-1].group()]

    return result

values = []

with open("data.txt", "r") as file:
    for line in file:
    
        merged = {**digits(line=line), **words(line=line, word_list=word_list)}
        
        values.append(
            int(merged[min(merged.keys())] + merged[max(merged.keys())])
        )

print(f"The new total for day one part two is: {sum(values)}")



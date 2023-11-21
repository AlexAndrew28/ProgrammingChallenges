"""
--PROBLEM DETAILS--

An I for an Eye

Ken has been having trouble lately staying under the word limit in Twitter, so he's decided to write a 
little front-end program which will take in text and shorten it using a fixed set of abbreviations for 
commonly used letter sequences. 

Input:
Input starts with a single integer indicating the number of lines of text to process. 
Following this are lines of text. Each line will contain only alphanumeric characters and spaces, 
and each line will have at least one non-space character. Each line has at most 200 characters.

Output:
Display each line with the appropriate substitutions made. Substitutions should also be made inside 
words, e.g., the word that should be changed to th@. If two letter sequences overlap (like at and to 
in the word baton) just replace the first one (in this case resulting in b@on). If two letter sequences 
start at the same location (like be and bee in been) replace the longer one (in this case resulting in bn). 
If the letter sequence starts with an upper-case letter, then the abbreviation should also be in upper-case 
(if appropriate). Finally, no substituted letter should later be part of another substitution. For example, 
if the input is oweh, you would first replace the owe with an o to get oh. At this point you do NOT replace 
the oh with an o since the oh contains a substituted letter.


Sample Input:
3
Oh say can you see
I do not understand why you are so cranky just because Karel won
Formation

Sample Output:
O say can u c
I do not underst& y u r so cranky just bcause Krl 1
4m@ion

Difficulty: 4.7

--SUBMISSION DETAILS--

Status: Accepted
Langauge: Python
Runtime: 0.06 seconds


Values correct as of: 20/11/2023

"""

number_lines = int(input())

mapping = {
    "four": "4",
    "Four": "4",
    "and" : "&" ,
    "And" : "&" ,
    "one" : "1" ,
    "One" : "1" ,
    "won" : "1" ,
    "Won" : "1" ,
    "too" : "2" ,
    "Too" : "2" ,
    "two" : "2" ,
    "Two" : "2" ,
    "for" : "4" ,
    "For" : "4" ,
    "bea" : "b" ,
    "Bea" : "B" ,
    "bee" : "b" ,
    "Bee" : "B" ,
    "sea" : "c" ,
    "Sea" : "C" ,
    "see" : "c" ,
    "See" : "C" ,
    "eye" : "i" ,
    "Eye" : "I" ,
    "owe" : "o" ,
    "Owe" : "O" ,
    "are" : "r" ,
    "Are" : "R" ,
    "you" : "u" ,
    "You" : "U" ,
    "why" : "y" ,
    "Why" : "Y" ,
    "at" : "@" ,
    "At" : "@" ,
    "to" : "2" ,
    "To" : "2" ,
    "be" : "b" ,
    "Be" : "B" ,
    "oh" : "o" ,
    "Oh" : "O" ,
}

for _ in range(number_lines):
    current_line = input()
    # create a dictionary for each index in the current string
    best = {i: [0, ""] for i in range(len(current_line))}
    counter = 0
    word = 0
    # run through the rules
    for rule_word in mapping.keys():
        counter = 0
        # run through each index in current string
        for i in range(len(current_line)):
            # try to find the current rule
            found = current_line.find(rule_word, i)
            if found == -1:
                break
            else:
                # store the best rule to use at this current point based on the length of the rule word
                if len(rule_word) > best[found][0]:
                    best[found] = [len(rule_word), rule_word]
            counter += 1
        word += 1

    end = False
    pos = 0
    final_output = ""
    # build the final output based on the best rule replacement 
    while not end:
        if pos == len(current_line):
            end = True
        else:
            if best[pos][0] == 0:
                final_output += current_line[pos]
                pos += 1
            else:
                final_output += mapping[best[pos][1]]
                pos += len(best[pos][1])
    print(final_output)
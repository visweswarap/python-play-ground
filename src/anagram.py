# An anagram of a string is another string that contains same characters,
# only the order of characters can be different.
# For example, “abcd” and “dabc” are anagram of each other.

string1 = 'LISTEN'
string2 = 'SILETT'


def is_anagram(str1,str2):
    if len(str1) != len(str2):
        print("Not an Anagram.")
        return 0

    for a in str1:
        if a not in str2:
            print("Not an Anagram.")
            return 0

    print("Yes Anagram.")


is_anagram(string1, string2)
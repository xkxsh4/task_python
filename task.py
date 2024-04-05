def vc_count(string):
    v_count = 0
    vowels ="aeiouAEIOU"
    
    for i in string:
        if i in vowels:
            v_count = v_count +1   
    
    consonets = len(string) - v_count
    dict={
        'vowel' : v_count,
        'consonent': consonets
    }
    print(dict)
    

string = input("Enter the word: ")
string = string.replace(" ", "")

vc_count(string)       
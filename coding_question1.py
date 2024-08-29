
def num_unique_consonants(string):
    #the consonants are the letters that are not vowels,
     
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    # create empty list to store all the letters in the input that are consonants    
    unique = []
    comp = []

    for char in string:
        # check if each character is unique
        if string.count(char)==1:
            unique.append(char)

    for char in unique:      
        # check if each character is a consonant
        if char in consonants: 
            # add the consonants to the list
            comp.append(char)

    # return the number of unique consonants
    print(unique)
    print(comp)
    return len(comp)

string = 'chocolate'

num_unique_consonants(string)
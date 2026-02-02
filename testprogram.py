#without dictionary - by getting input from user
#count number of vowels and consonants in a letter

def countvc (text):
    vowels = 0
    consonants = 0
    vowel = "aeiou"
    vow = ""
    con = ""
    text = text.lower()
    for i in text:
        if i.isalpha():
            if i in vowel:
                vowels += 1
                vow = vow + i
            else:
                consonants += 1
                con = con + i
    return vowels, consonants, vow, con
word = input("Enter the text to count the vowels and consonants: ")
vowels, consonants, vow, con = countvc(word)
print(f"Vowels List = {vow}\nVowels Count = {vowels}")
print(f"Consonants List = {con}\nConsonants Count = {consonants}")

import string

def most_wanted_letter(text):
    text = text.lower()

    letter_counts = {}
    for char in text:
        if char in string.ascii_letters:  
            letter_counts[char] = letter_counts.get(char, 0) + 1

    if not letter_counts:
        return "There are no letters in the string"

    most_common_letter = None
    max_count = 0

    for letter, count in letter_counts.items():
        if count > max_count or (count == max_count and letter < most_common_letter):
            most_common_letter = letter
            max_count = count

    return f"The most popular letter is '{most_common_letter}'"

print(most_wanted_letter("aAaahhh////"))
print(most_wanted_letter("....12345%4(%7535/////..."))
print(most_wanted_letter(""))

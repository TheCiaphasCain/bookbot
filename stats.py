def word_count(book_content):
    # Split the text into words and count them
    words = book_content.split()
    return (len(words))

def character_count(book_content):
    # Set text to all lowercase
    book_content = book_content.lower()
    # Create a temporary dictionary to count occurrences
    temp_count = {}
    for char in book_content:
        if char in temp_count:
            temp_count[char] += 1
        else:
            temp_count[char] = 1
    # Convert to list of dictionaries with named keys
    char_count = []
    for char, count in temp_count.items():
        if char.isalpha():
            char_count.append({"char": char, "count": count})
    return char_count

def pre_sort(char_count):
    return char_count["count"]

def sorted_dictionaries(char_count):
    #sort dictionary of characters in list of dictionaries from greatest to least,
    #omitting any non-aplhabeticals
    char_count.sort(reverse=True, key=pre_sort)

    return char_count

    
    

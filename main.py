from stats import word_count, character_count, sorted_dictionaries
import sys

def main():
    #print("starting main function")
    #print(f"sys.argv = {sys.argv}")

    # Inside main, call get_book_text with the path to a book
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    #print("passed argument check")
    path = sys.argv[1] 
    #print(f"using path: {path}")
    book_content = get_book_text(path)
    #print(f"book content length: {len(book_content)} characters")
    
    # Get word count
    word_cnt = word_count(book_content)
    
    # Get character counts and sort them
    characters = character_count(book_content)
    sorted_chars = sorted_dictionaries(characters)
    
    # Call create_report with the data
    create_report(path, word_cnt, sorted_chars)

def get_book_text(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.read()

def create_report(path, word_count, char_count):
    # print the header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    # print word count
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    # print character count
    print("--------- Character Count -------")

    # print each character and its count on a separate line
    for char_data in char_count:
        if char_data["char"].isalpha():  # Only include alphabetical characters
            char = char_data["char"]
            count = char_data["count"]
            print(f"{char}: {count}")
    
    # print footer
    print("============= END ===============")

main()
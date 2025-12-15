from stats import *
import sys

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    arg1 = sys.argv[1]
    
    list_of_chars = []
    whole_book = get_book_text(arg1)
    
    amount_letters = count_chars(whole_book)
    
    
    num_of_words = count_total_words(whole_book)
    
    for ch in amount_letters:
        list_of_chars.append({"char": ch, "num": amount_letters[ch]})
    
    printer(arg1, num_of_words, list_of_chars)
    
    
main()
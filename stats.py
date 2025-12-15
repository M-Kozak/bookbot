def get_book_text(path):
    with open(path) as f:
        actual_words = f.read()
    return actual_words

def count_total_words(actual_words):
    words = actual_words.split()
    return len(words)

def count_chars(words):
    letters = {}
    all_words = words.lower()
    for char in all_words:
        if char not in letters:
            letters[char] = 0
        letters[char] += 1
    return letters

def sort_on(items):
    return items["num"]

def printer(path, total_amount, list_of_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing books found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_amount} total words")
    print("--------- Character Count -------")
    list_of_chars.sort(reverse=True, key=sort_on)
    
    for items in list_of_chars:
        char = items["char"]
        if not char.isalpha():
            continue
        print(f"{char}: {items['num']}")
    print("============= END ===============")
        
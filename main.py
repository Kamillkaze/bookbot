def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    print(f"{num_words} words found in the document\n")
    print(f"map of characters count: {num_characters}")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    result = {}
    text = text.lower()
    for c in text:
        if not c.isalpha():
            continue
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result

main()
def main():
    print("Type in a file path below and press enter:")
    book_path = input().strip()
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    list_num_characters = convert_dict_to_sorted_list(num_characters)
    print_report(book_path, num_words, list_num_characters)

def print_report(book_path, num_words, num_chars):
    print(f"\n--- Begin report of {book_path} ---\n")
    print(f"{num_words} words found in the document\n")
    for entry in num_chars:
        print(f"The \'{entry["char"]}\' character was found {entry["count"]} times")
    print("\n--- End report ---\n")

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

def convert_dict_to_sorted_list(dict):
    list = []
    for entry in dict:
        data = {}
        data["char"] = entry
        data["count"] = dict[entry]
        list.append(data)

    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(dict):
    return dict["count"]

main()
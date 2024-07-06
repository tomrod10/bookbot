def main():
    file_path = "books/frankenstein.txt"
    text = get_book(file_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    sorted_char_count = list_and_sort_char_count(char_count)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    for c in sorted_char_count:
        print(f"The '{c['char']}' was found {c['num']} times")

    print("--- End Report ---")


def get_book(path):
    with open(path) as f:
        text = f.read()
        return text


def get_word_count(text: str):
    return len(text.split())


def get_char_count(text: str):
    char_count = {}
    for c in text:
        if c.isalpha():
            c = c.lower()
            if c not in char_count:
                char_count[c] = 1
            else:
                char_count[c] += 1
    return char_count


def sort_on(d: dict):
    return d["num"]


def list_and_sort_char_count(char_count: dict):
    count_list = []
    for k in char_count:
        count_list.append({"char": k, "num": char_count[k]})
    count_list.sort(reverse=True, key=sort_on)
    return count_list


if __name__ == "__main__":
    main()

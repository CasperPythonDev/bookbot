def main():

    import string

    alphabet = list(string.ascii_lowercase)
    book_path: str = "books/frankenstein.txt"

    def word_count(book: str) -> int:
        list = book.split()
        return len(list)

    with open(book_path) as f:
        file_contents = f.read()

    words = word_count(file_contents)
    # print(words)

    def count_symbols(book: str) -> dict:
        product = {}
        count = 0
        symbol_list = sorted(list(set(book.lower())))
        for s in symbol_list:

            count = book.lower().count(s)

            product[s] = count

        return product

    def print_report(dict: dict[str, int]) -> None:
        print(f"--- Begin report of {book_path} ---")
        print(f"{words} words found in the document")
        report_list = {}
        for key, value in dict.items():
            if key.isalpha():
                report_list[key] = value

        # sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
        # sorted_dict = dict(sorted(dict.items(), key=lambda x: x[1])))
        my_dict = report_list
        my_sort = sorted(my_dict.items(), key=lambda x: x[1])
        for v in my_sort:
            print(f"'{v[0]}' occurs {v[1]} times")

    final = count_symbols(file_contents)
    print_report(final)


if __name__ == "__main__":
    main()

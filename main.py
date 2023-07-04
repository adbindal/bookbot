def create_report(letter_counts):
    inputs = filter(
        lambda item: item[0].isalpha(), letter_counts.items())
    for inp in sorted(inputs, key=lambda i: i[1], reverse=True):
        print(f"The '{inp[0]}' character was found {inp[1]} times")


def count_by_letter(text):
    counts = {}
    for letter in text:
        ch = letter.lower()
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts


def count_words(text):
    return len(text.split())


with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    create_report(count_by_letter(file_contents))

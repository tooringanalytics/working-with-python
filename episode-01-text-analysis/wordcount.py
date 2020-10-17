import re
import sys

WORD_REGEX = re.compile(r"\w+")
TEXTFILE = "/home/tooring/Documents/Programs/a-tale-of-two-cities-charles-dickens.txt"
TOP = 5
WORD_LEN = 1
BAR_LEN = 30

def all_words(filepath=TEXTFILE, word_len=WORD_LEN):
    with open(TEXTFILE, "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            line_words = WORD_REGEX.findall(line)
            for word in line_words:
                if len(word) >= word_len:
                    yield word

def unique_words(words):
    return set(words)

def histogram(words):
    hist = {}
    for word in words:
        hist[word] = hist[word] + 1 if word in hist else 1
    return hist

def most_frequent(hist):
    return sorted(hist.items(), key=lambda item: item[1], reverse=True)


def wordcount(filepath=TEXTFILE, word_len=WORD_LEN, top=TOP, bar_len=BAR_LEN):
    words = list(all_words(filepath, word_len))

    uniques = unique_words(words)
    hist = histogram(words)
    freq = most_frequent(hist)
    num_words = len(words)
    num_uniques = len(uniques)

    print(f"{num_words} total words. {num_uniques} unique words.")
    print(f"Top {top} words")
    print("-" * 79)
    print(f"No.\tWord\t\tCount")
    print("-" * 79)
    most = freq[0][1]
    for i, wc in enumerate(freq[:top]):
        word = wc[0]
        count = wc[1]
        bar = "#" * int((count / most) * bar_len)
        print(f"{i + 1}\t{word}\t\t{bar} ({count})")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = TEXTFILE
    wordcount(filepath=filepath, top=5, bar_len=40)
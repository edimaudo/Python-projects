import matplotlib.pyplot as plt
import sys
import operator
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "word",
        help="the word to be searched for in the text file."
    )
    parser.add_argument(
        "filename",
        help="the path to the text file to be searched through"
    )

    args = parser.parse_args()

    try:
        open(args.filename)
    except FileNotFoundError:

        # Custom error print
        sys.stderr.write("Error: " + args.filename + " does not exist!")
        sys.exit(1)

    word_freq(args.word, args.filename)


def word_freq(word, filename):
    doc = {}

    for line in open(filename):

        # Assume each word is separated by a space
        split = line.split(' ')
        for entry in split:
            if (doc.__contains__(entry)):
                doc[entry] = int(doc.get(entry)) + 1
            else:
                doc[entry] = 1

    if (word not in doc):
        sys.stderr.write("Error: " + word + " does not appear in " + filename)
        sys.exit(1)

    sorted_doc = (sorted(doc.items(), key=operator.itemgetter(1)))[::-1]
    just_the_occur = []
    just_the_rank = []
    word_rank = 0
    word_frequency = 0

    entry_num = 1
    for entry in sorted_doc:

        if (entry[0] == word):
            word_rank = entry_num
            word_frequency = entry[1]

        just_the_rank.append(entry_num)
        entry_num += 1
        just_the_occur.append(entry[1])

    plt.title("Word Frequencies in " + filename)
    plt.ylabel("Total Number of Occurrences")
    plt.xlabel("Rank of word(\"" + word + "\" is rank " + str(word_rank) + ")")
    plt.loglog(just_the_rank, just_the_occur, basex=10)
    plt.scatter(
        [word_rank],
        [word_frequency],
        color="orange",
        marker="*",
        s=100,
        label=word
    )
    plt.show()

if __name__ == "__main__":
    main()
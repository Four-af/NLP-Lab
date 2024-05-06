word_freq = {}
char_freq = {}


def add_eow_and_spaces(corpus):
    modified_corpus = []
    modified_corpus_word = []
    for word in corpus.split():
        word = word + "$ "
        modified_word = word
        modified_corpus.append(modified_word)
    print(" ".join(modified_corpus))
    return " ".join(modified_corpus)


def get_frequencies(corpus):
    word_freq = {}
    char_freq = {}
    for word in corpus.split():
        for char in word:
            char_freq[char] = char_freq.get(char, 0) + 1
        word_freq[word] = word_freq.get(word, 0) + 1
    print("Word Frequency: ", word_freq)
    print("Char Frequency: ", char_freq)
    # return (word_freq, char_freq)


def merge_pair(pair, corpus):
    merged_corpus = []
    for word in corpus.split():
        merged_word = word.replace(pair, "".join(pair))
        merged_corpus.append(merged_word)
    return " ".join(merged_corpus)


def byte_pair_encoding(corpus, iterations):
    corpus = add_eow_and_spaces(corpus)
    # word_freq, char_freq = get_frequencies(corpus)
    get_frequencies(corpus)
    rules = []

    for i in range(iterations):
        most_freq_pair = max(char_freq, key=char_freq.get)
        rules.append(most_freq_pair)
        corpus = merge_pair(most_freq_pair, corpus)
        get_frequencies(corpus)

    return rules


# Example Usage:
corpus = "I am Adam"
iterations = 5
rules = byte_pair_encoding(corpus, iterations)
print("Byte Pair Encoding Rules:")
for i, rule in enumerate(rules, start=1):
    print(f"Rule {i}: Merge {rule[0]} and {rule[1]}")

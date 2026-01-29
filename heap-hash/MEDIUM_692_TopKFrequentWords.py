"""
    Given an array of strings words and an integer k, return the k most frequent strings.

    Return the answer sorted by the frequency from highest to lowest.
    Sort the words with the same frequency by their lexicographical order.
"""


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        _words = {}

        for word in words:
            if word in _words:
                _words[word] += 1
            else:
                _words[word] = 1

        words_count = {}
        for word, count in _words.items():
            if count in words_count:
                words_count[count].append(word)
            else:
                words_count[count] = [word]

        sorted_words = [
            sorted(words)
            for count, words in sorted(words_count.items(), key=lambda x: x[0], reverse=True)
        ]

        words_count_sorted = []
        for words in sorted_words:
            words_count_sorted += words

        return words_count_sorted[:k]


if __name__ == "__main__":
    assert Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == [
        "i",
        "love",
    ]
    assert Solution().topKFrequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4
    ) == ["the", "is", "sunny", "day"]

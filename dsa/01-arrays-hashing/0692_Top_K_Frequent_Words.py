class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        ordered = sorted(d, key=lambda w: (-d[w], w))
        # sorts by negative count first, then the word by tie
        # -d[w] to reverse the ascending order
        return ordered[:k]

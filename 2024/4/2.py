import numpy as np

word_search = []
with open('2024/4/data') as f:
    text = f.readlines()
    for t in text:
        word_search.append(list(t.rstrip()))

word_search = np.array(word_search)
text_search = ['MAS', 'SAM']

rows, columns = word_search.shape[0], word_search.shape[1]

word_count = 0
for r in range(0, rows - 2):
    for c in range(0, columns - 2):
        ws_subset = word_search[r:r+3, c:c+3]
        diag1 = ''.join(np.diagonal(ws_subset).tolist())
        diag2 = ''.join(np.diagonal(ws_subset[::-1]).tolist())

        if diag1 in text_search and diag2 in text_search:
            word_count += 1

print(word_count)
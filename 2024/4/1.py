import numpy as np

# search_text = ['XMAS', 'SAMX']

word_search = []
with open('2024/4/data') as f:
    text = f.readlines()
    for t in text:
        word_search.append(list(t.rstrip()))

word_search = np.array(word_search)
search_count = 0

for r_ix in range(word_search.shape[0]):
    search_count += ''.join(word_search[r_ix, :].tolist()).count('XMAS')
    search_count += ''.join(word_search[r_ix, :].tolist()).count('SAMX')

for c_ix in range(word_search.shape[1]):
    search_count += ''.join(word_search[:, c_ix].tolist()).count('XMAS')
    search_count += ''.join(word_search[:, c_ix].tolist()).count('SAMX')

print(f'straight: {search_count}')

rows, columns = word_search.shape

for search_matrix in [word_search, word_search[:, ::-1]]:

    for offset in range(-rows+1, columns-1):
        diagonal_text = ''.join(np.diagonal(search_matrix, offset=offset).tolist())
        if len(diagonal_text) >= 4:
            search_count += diagonal_text.count('XMAS')
            search_count += diagonal_text.count('SAMX')

print(search_count)

from algorithms.levenshtein_distance_similarity.levenshtein import levenshtein, normalize

kelime_1 = 'Selamlar'
kelime_2 = 'Selamaa'

max_len = max(len(kelime_1), len(kelime_2))
kelime_1 = normalize(kelime_1, max_len)
kelime_2 = normalize(kelime_2, max_len)
distance = levenshtein(kelime_1, kelime_2)
print(distance)

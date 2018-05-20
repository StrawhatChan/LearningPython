# -*- coding: utf-8 -*-
# Joel Grus, 2016: Data Science from Scratch. O'Reilly Media.
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons, start=3)))
xs = [i + 0.1 for i, _ in enumerate(seasons)]
print(xs)
ys = [season + '+' for _, season in enumerate(seasons)]
print(ys)
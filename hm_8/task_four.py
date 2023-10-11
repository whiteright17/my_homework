result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
symbols = {}
for sym in result_link:
    symbols[sym] = symbols.get(sym, 0) + 1
print(symbols)
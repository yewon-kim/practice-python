dict_a = {
    'kr': '한국',
    'au': '호주',
    'jp': '일본',
    'us': '미국'
}
tuple_list = sorted(dict_a.items(), key = lambda item: item[1])
keys = []
values = []
for key, value in tuple_list:
    keys.append(key)
    values.append(value)
# 3都府県のいくつかの駅名とある日の最高気温のデータを辞書として持っています
weather_information = [
    {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
    {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
    {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},

    {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
    {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
    {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},

    {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
    {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
]

# Q1. 全国の平均気温は？

# temp1 = weather_information[0]['temperature']
# temp2 = weather_information[1]['temperature']
# temp3 = weather_information[2]['temperature']
# temp4 = weather_information[3]['temperature']
# temp5 = weather_information[4]['temperature']
# temp6 = weather_information[5]['temperature']
# temp7 = weather_information[6]['temperature']
# temp8 = weather_information[7]['temperature']

# print(f'{temp1},{temp2},{temp3},{temp4},{temp5},{temp6},{temp7},{temp8}')

# total = temp1 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8

total = 0

for info in weather_information:
    total += info['temperature']

ave = total / len(weather_information)

print(ave)

# Q2. 大阪府のすべての駅名を出力してね。
for sta in weather_information:
    if weather_information['station'] == '福岡':
        print(sta)
    else:
        break

# sta4 = weather_information[3]['station']
# sta5 = weather_information[4]['station']
# sta6 = weather_information[5]['station']
#
# print(f'{sta4},{sta5},{sta6}')

# Q3. 福岡県の平均気温は？

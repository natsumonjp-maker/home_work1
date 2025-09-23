def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください
    total_temp = sum(item['temperature'] for item in weather_information)
    average_temp = total_temp / len(weather_information)
    print(f"全国の平均気温: {average_temp:.1f}℃")  # → 9.5℃

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください
    osaka_stations = [item['station'] for item in weather_information if item['prefecture'] == '大阪府']
    print("大阪府の駅名:", ",".join(osaka_stations))  # → 梅田,大阪,堺

    # Q3. 福岡県の平均気温を計算してください
    fukuoka_temps = [item['temperature'] for item in weather_information if item['prefecture'] == '福岡県']
    fukuoka_avg = sum(fukuoka_temps) / len(fukuoka_temps)
    print(f"福岡県の平均気温: {fukuoka_avg:.1f}℃")  # → 14.0℃


if __name__ == '__main__':
    main()

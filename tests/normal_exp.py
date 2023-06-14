import re
# numbers = "@7.0 @-8.0 @9.0 "
# number_strings = re.findall(r"[-+]?\d*\.?\d+", numbers)
# # number_strings = re.findall(r"\d+", numbers)
# print(number_strings)
# print(type(number_strings))

# text = "Here are some URLs: <https://example1.com>, <https://example2.com>, <https://example3.com>"
# # 正規表現を使用してURLを抽出
# urls = re.findall(r'<(.*?)>', text)
# # 抽出されたURLを表示
# print(urls[2])
# for url in urls:
#     print(url)


text = "*Grafana:*\nあとの<https*> を取得したいです。"
pattern = r"<https[^>]*>"

result = re.findall(pattern, text)
print(result)
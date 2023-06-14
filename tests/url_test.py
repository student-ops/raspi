# import json

# response_data = "[{'bot_id': 'B057HEFQDUN', 'type': 'message', 'text': '*App:* \n<http://91bb-61-114-97-102.ngrok-free.app>\n*Grafana:* \n<http://e921-61-114-97-102.ngrok-free.app>', 'user': 'U057PUFT7H9', 'ts': '1685084498.015519', 'app_id': 'A058DP8GU6L', 'blocks': [{'type': 'rich_text', 'block_id': '8eHa', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'App:', 'style': {'bold': True}}, {'type': 'text', 'text': ' \n'}, {'type': 'link', 'url': 'http://91bb-61-114-97-102.ngrok-free.app'}, {'type': 'text', 'text': '\n'}, {'type': 'text', 'text': 'Grafana:', 'style': {'bold': True}}, {'type': 'text', 'text': ' \n'}, {'type': 'link', 'url': 'http://e921-61-114-97-102.ngrok-free.app'}]}]}], 'team': 'T057PQRQ727', 'bot_profile': {'id': 'B057HEFQDUN', 'deleted': False, 'name': 'api-test', 'updated': 1684111829, 'app_id': 'A058DP8GU6L', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'team_id': 'T057PQRQ727'}}]"

# # シングルクォートをダブルクォートに置換して正しいJSON形式にする
# response_data = response_data.replace("'", "\"")

# # JSON文字列を辞書にパースする
# response_dict = json.loads(response_data)

# # URLを取得する
# blocks = response_dict[0]["blocks"]
# url_list = []
# for block in blocks:
#     elements = block["elements"]
#     for element in elements:
#         if "url" in element:
#             url = element["url"]
#             url_list.append(url)

# print("URL List:", url_list)
import json
import pprint

response_data = "[{'bot_id': 'B057HEFQDUN', 'type': 'message', 'text': '*Grafana:* \n<https://91bb-61-114-97-102.ngrok-free.app>\n*InfluxDB:* \n<http://e921-61-114-97-102.ngrok-free.app>', 'user': 'U057PUFT7H9', 'ts': '1685083979.346289', 'app_id': 'A058DP8GU6L', 'blocks': [{'type': 'rich_text', 'block_id': '/u9', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Grafana:', 'style': {'bold': True}}, {'type': 'text', 'text': ' \n'}, {'type': 'link', 'url': 'https://91bb-61-114-97-102.ngrok-free.app'}, {'type': 'text', 'text': '\n'}, {'type': 'text', 'text': 'InfluxDB:', 'style': {'bold': True}}, {'type': 'text', 'text': ' \n'}, {'type': 'link', 'url': 'http://e921-61-114-97-102.ngrok-free.app'}]}]}], 'team': 'T057PQRQ727', 'bot_profile': {'id': 'B057HEFQDUN', 'deleted': False, 'name': 'api-test', 'updated': 1684111829, 'app_id': 'A058DP8GU6L', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'team_id': 'T057PQRQ727'}}]"

# シングルクォートをダブルクォートに置換して正しいJSON形式にする
response_data = response_data.replace("'", "\"")

# JSON文字列を辞書にパースする
response_dict = json.loads(response_data)

# 構造を上からプロット
pprint.pprint(response_dict)

import json
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


# ===== Line API =====
line_bot_api = LineBotApi('Rts4hEVoK40EjIpVP0qRhWDe7SVLQuASXIbLcbnXWPr6zDhDXaEQt7s6RtiV8otmkBr1k8QYCCN63ano9kYKjMrH9gtN1qY8HVncVvZNJofnsg/EN4qwko489t85FvTcgbD7exc8tEVSmQin+KFF9gdB04t89/1O/w1cDnyilFU=') #Chanel acces token
handler = WebhookHandler('acd437941eb097612b3e2584e979d4d5') # Chenal Secert
group = 'Cceff87945027f6958d8155dd9002b841' #Group ID
# =====================


app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        
        data = json.dumps(request.json)
        print(data)
        
        csp = json.loads(request.json)
        
        text_message = TextSendMessage(text='BloxOne Notification\nID: csp['id']\nType: csp['type']')
        print(text_message)
        line_bot_api.push_message(group, text_message) # push message buy via Line

        # print(request.data)
        return 'success', 200
    else:
        abort(400)

@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    print(body)
    return 'OK'

if __name__ == '__main__':
    app.run()
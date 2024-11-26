from flask import Flask, request
app = Flask(__name__)

# サーバールートへアクセスがあった時 --- (*1)
@app.route('/')
def index():
    # フォームを表示する --- (*2)
    return """
        <html><body>
        <form action="/hello" method="GET">
          名前: <input type="text" name="name">
<BR>
          ひとこと: <input type="text" name="hitokoto">
          <input type="submit" value="送信">
        </form>
        </body></html>
    """

# /hello へアクセスがあった時 --- (*3)
@app.route('/hello')
def hello():
    # nameとhitokotoのパラメータを得る --- (*4)
    name = request.args.get('name')
    # hitokotoのパラメータを得る --- (*4)
    hitokoto = request.args.get('hitokoto')
    if name is None: name = '名無し'
    if hitokoto is None: hitokoto = 'ひとことなし'
    # 自己紹介を自動作成
    return """
    <h1>{0}さん、こんにちは！{1}</h1>
    """.format(name,hitokoto)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


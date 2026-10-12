from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'admin' and password == '123456':
        return jsonify({
            'message': '登录成功',
            'token': 'abc123'
        }), 200

    return jsonify({
        'message': '用户名或密码错误'
    }), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8787)
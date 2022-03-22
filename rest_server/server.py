from flask import Flask, request, jsonify
import jwt
import time

app = Flask(__name__)

def get_jwt_token(username, deviceid):
    headers = {
        "alg": "HS256",
        "typ": "JWT"
    }
    # 设置headers，即加密算法的配置
    salt = "tqhql!@#$"
    # 随机的salt密钥，只有token生成者（同时也是校验者）自己能有，用于校验生成的token是否合法
    exp = int(time.time() + 3600 * 2)
    # 设置超时时间：当前时间的100s以后超时
    payload = {
        "name": username,
        "exp": exp,
        "deviceid": deviceid
    }
    token = jwt.encode(payload=payload, key=salt, algorithm='HS256', headers=headers)
    return token

@app.route('/api/rest/v2.0/login', methods=['PUT'])
def login():
    payload = request.json
    rep_val = {}
    if payload is not None:
        username = payload['username']
        print(username)
        #devicesn = payload['deviceSn']
        #print(deviceid)
        if username == "xiaoye1":
            uid = 30004
            deviceId = 40004
        else:
            uid = 30003
            deviceId = 40003

        jwt_token = get_jwt_token(username, deviceId)
        # {"userId":18,"token":"225322833","username":"1010","displayName":"1010","org":null,"email":"1010@hexmeet.cn","cellphone":"1010","telephone":"1010","role":null,"deviceId":139,"callServiceToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiMTAxMCIsImV4cCI6MTUxNTcyOTMyNSwiZGV2aWNlaWQiOjEzOX0.rNCKZembWjuotsxzPX3ZCQFoj9WCI8n2alzv6vgXaG0","callServiceUrl":"ws://172.24.0.63:9002/websocket/message?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiMTAxMCIsImV4cCI6MTUxNTcyOTMyNSwiZGV2aWNlaWQiOjEzOX0.rNCKZembWjuotsxzPX3ZCQFoj9WCI8n2alzv6vgXaG0","everChangedPasswd":true,"agentId":1}

        rep_val['userId'] = uid
        rep_val['username'] = username
        rep_val['deviceId'] = deviceId
        rep_val['callServiceUrl'] = 'ws://127.0.0.1:9002/websocket/message?token=' + jwt_token
    return jsonify(rep_val)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8340, debug=True)

import json
import jwt
import time
import uuid


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


def update_msg_info(msg, uid, deviceid, to, callid):
    obj = json.loads(msg)
    obj["contact"]["uid"] = uid
    obj["contact"]["deviceid"] = deviceid
    obj["to"] = "sip:" + to + "@hexmeet.com"
    obj["from"] = "sip:" + deviceid + "@simulatorEp.com"
    obj["callid"] = callid
    obj["branch_id"] = str(uuid.uuid4())
    # obj["callid"] = str(uuid.uuid4())

    return json.dumps(obj)


def gen_register_req(uid, deviceid):
    register_msg = '''{
            "method":"REGISTER",
            "from":"sip:31400@simulatorEp.com",
            "to":"sip:31400@dolphin.com",
            "callid":"mTjbsGlh",
            "user-agent":"Simulator Sling ep",
            "contact":{
                "uid":"60414",
                "deviceid":"696002"
            },
            "cseq":{
                "method":"REGISTER",
                "sequence":"1"
            },
            "content-type":"",
            "content":"",
            "event":"",
            "source_ip":"127.0.0.1",
            "region":{
                "city_code":0,
                "country":"0",
                "province":"0",
                "city":"内网IP"
            }
        }'''

    # register_obj = json.loads(register_msg)
    return update_msg_info(register_msg, uid, deviceid, '',str(uuid.uuid4()))


async def send_msg_and_await_rsp(req_msg, websocket):
    await websocket.send(req_msg)
    response_str = await websocket.recv()
    print('=>' + response_str)
    if "200 OK" in response_str:
        return True
    elif "ACK" in response_str:
        return True
    return False


async def await_bye(websocket):
    bye_str = await websocket.recv()
    print('=>' + bye_str)

    if "BYE" in bye_str:
        obj = json.loads(bye_str)
        obj['method'] = '200 OK'
        r200OK = json.dumps(obj)
        print('<=' + r200OK)
        await websocket.send(r200OK)

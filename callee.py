# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import time
import random
import asyncio
import websockets
import json
import uuid
import common


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.




def gen_invite( uid, deviceid, to):
    invite_msg = '''{
        "method":"INVITE",
        "from":"sip:31388@simulatorEp.com",
        "to":"sip:13900000001@dolphin.com",
        "callid":"AKrT1Pz8",
        "user-agent":"Simulator Sling ep",
        "contact":{
            "uid":"60402",
            "deviceid":"695990"
        },
        "cseq":{
            "method":"INVITE",
            "sequence":"2"
        },
        "content-type":"sdp",
        "event":"",
        "source_ip":"172.26.0.153",
        "call_mode":2,
        "region":{
            "city_code":0,
            "country":"0",
            "province":"0",
            "city":"内网IP"
        }
    }'''
    return common.update_msg_info(invite_msg, uid, deviceid,to, str(uuid.uuid4()))


def gen_bye(uid, deviceid, to, callid):
    bye_msg = '''{
        "method": "BYE",
        "from": "sip:60005",
        "to": "sip:260082@172.25.0.155",
        "callid": "8d1ea517-cf36-4b98-8334-c9a4ea4b7035",
        "contact": {
            "uid": "20006",
            "deviceid": "60005"
        },
        "content": "",
        "cseq": {
            "method": "BYE",
            "sequence": "1"
        },
        "user-agent": "HexMeet EasyVideo Win SVC 1.6.0.355",
        "content-type": "",
        "event": "",
        "conf_password": "",
        "display_name": "",
        "universal_id": "",
        "branch_id": "",
        "reason": "EP_NORMAL",
        "call_mode":2
    }'''
    return common.update_msg_info(bye_msg, uid, deviceid, to, callid)

async def main_logic():
    deviceid = 40003
    #random.randint(40000, 45000)
    username = "simu1237"
    #simu" + str(random.randint(60000, 65000))
    uid = 30003
    to = "40004"
    #random.randint(30000, 35000)
    token = common.get_jwt_token(username, deviceid)
    async with websockets.connect('ws://127.0.0.1:9002/websocket/messsage?token=' + token) as websocket:
        print("connected")
        register_msg = common.gen_register_req(str(uid), str(deviceid))
        print(register_msg)
        await common.send_msg_and_await_rsp(register_msg,websocket)
        time.sleep(2)
        invite_msg = gen_invite(str(uid),str(deviceid), to)
        print(invite_msg)
        await common.send_msg_and_await_rsp(invite_msg, websocket)
        time.sleep(2)
        obj = json.loads(invite_msg)
        callid = obj['callid']
        #send ack
        obj["method"] = "ACK"
        ack = json.dumps(obj)
        print(ack)
        await websocket.send(ack)
        bye_msg = gen_bye(str(uid), str(deviceid),  to, callid)
        print(bye_msg)
        await common.send_msg_and_await_rsp(bye_msg, websocket)
        time.sleep(2)


if __name__ == '__main__':
    # print(get_jwt_token(username,deviceid))
    asyncio.get_event_loop().run_until_complete(main_logic())
    # print(gen_register_req(username, str(uid), str(deviceid)))
    # deviceid = random.randint(40000, 45000)
    # username = "simu" + str(random.randint(60000, 65000))
    # uid = random.randint(30000, 35000)
    # gen_invite(username,str(uid), str(deviceid))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import json
import common
import time
import asyncio
import websockets



def update_answer_msg_info(msg, uid, deviceid, fromUrl, to, callid):
    obj = json.loads(msg)
    obj["contact"]["uid"] = uid
    obj["contact"]["deviceid"] = deviceid
    obj["to"] = to
    obj["from"] = fromUrl
    obj["callid"] = callid
    # obj["callid"] = str(uuid.uuid4())

    return json.dumps(obj)


def gen_inv_200OK(uid, deviceid, fromurl, to,callid):
    inv_200ok = '''{
                    "method":"200 OK",
                    "from":"sip:70021@172.25.0.165",
                    "to":"sip:13123618606@10.252.0.44",
                    "callid":"11a00d36-dcfb-4f87-bb8a-a7adb46a6f4c",
                    "display_name":"VE660_77",
                    "user-agent":"HexMeet MRU 2.8.5.13582",
                    "branch_id":"7e3140ae-670c-43ec-9a2f-0350fc3fce36",
                    "contact":{
                        "uid":"280019",
                        "deviceid":"70021"
                    },
                    "cseq":{
                        "method":"INVITE",
                        "sequence":"1"
                    },
                    "content-type":"sdp",                    
                    "call_type":"0",
                    "call_mode":2
                }'''
    return update_answer_msg_info(inv_200ok,uid, deviceid, fromurl,to,callid)

async def await_incoming_call(websocket,uid, deviceid):
    inv_str = await websocket.recv()
    print(inv_str)
    obj = json.loads(inv_str)
    ##send 200 Ok
    ##get from


    # peer_uid = obj["contact"]["uid"]
    # peer_deviceid = obj["contact"]["deviceid"]
    to = obj["to"]
    fromurl = obj["from"]
    callid = obj["callid"]

    r200Ok_msg = gen_inv_200OK(uid, deviceid, fromurl, to, callid)
    ##set from, to, callid
    print(r200Ok_msg)
    await common.send_msg_and_await_rsp(r200Ok_msg, websocket)
    # await websocket.send(r200Ok_msg)
    # response_str = await websocket.recv()
    # time.sleep(2)


    # time.sleep(2)

    ## awaite ack

async def main_logic():
    deviceid = 40004
    # random.randint(40000, 45000)
    username = "simu1237"
    # simu" + str(random.randint(60000, 65000))
    uid = 30004
    #to = "40003"
    # random.randint(30000, 35000)
    token = common.get_jwt_token(username, deviceid)
    async with websockets.connect('ws://127.0.0.1:9002/websocket/messsage?token=' + token) as websocket:
        print("connected")
        register_msg = common.gen_register_req(str(uid), str(deviceid))
        print(register_msg)
        await common.send_msg_and_await_rsp(register_msg, websocket)
        time.sleep(2)
        await await_incoming_call(websocket,str(uid), str(deviceid))
        # invite_msg = gen_invite(username,str(uid),str(deviceid), to)
        # print(invite_msg)
        # await send_msg_and_await_rsp(invite_msg, websocket, username, uid, deviceid)
        time.sleep(2)
        # obj = json.loads(invite_msg)
        # callid = obj['callid']
        await common.await_bye(websocket)
        # bye_msg = gen_bye(username, str(uid), str(deviceid),  to, callid)
        # await send_msg_and_await_rsp(bye_msg, websocket, username, uid, deviceid)
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

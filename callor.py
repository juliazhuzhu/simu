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
                    "content":"v=0\\r\\no=MCU 1164457869 0 IN IP4 172.25.0.165\\r\\ns=NGMCU\\r\\nc=IN IP4 172.25.0.165\\r\\nb=AS:4096\\r\\nt=0 0\\r\\na=hxm-conference-control:0\\r\\na=whiteboard:1\\r\\nm=audio 30002 RTP/SAVP 126 111\\r\\na=sendrecv\\r\\na=rtpmap:126 ARLY/48000\\r\\na=fmtp:126 bitrate=64000\\r\\na=rid:1 recv pt=126 ssrc=67120331\\r\\na=rid:2 send pt=126 ssrc=67110516\\r\\na=rtpmap:111 telephone-event/8000\\r\\na=fmtp:111 0-15\\r\\na=openfec:* no_padding\\r\\na=rtcp:30002\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:O8Vi2lKh4i8g5Nsx3WxgE3swppmlanjhacKF9BEX|2^31\\r\\nm=video 30002 RTP/SAVP 99 109 100 110 101 111 102 112 103 113\\r\\nb=TIAS:4096000\\r\\na=sendrecv\\r\\na=content:main\\r\\na=label:1\\r\\na=rtpmap:99 H265/90000\\r\\na=fmtp:99 profile-space=0; profile-id=1; level-id=150; max-lsr=267386880; max-lps=8912896; max-fps=3000\\r\\na=rtcp-fb:99 hxm-cc\\r\\na=rtpmap:109 rtx/90000\\r\\na=fmtp:109 apt=99\\r\\na=rtp-rtx:99 max-temp-layer=3\\r\\na=rtcp-fb:99 nack pli\\r\\na=rtpmap:100 H265/90000\\r\\na=fmtp:100 profile-space=0; profile-id=1; level-id=120; max-lsr=66846720; max-lps=2228224; max-fps=3000\\r\\na=rtcp-fb:100 hxm-cc\\r\\na=rtpmap:110 rtx/90000\\r\\na=fmtp:110 apt=100\\r\\na=rtp-rtx:100 max-temp-layer=3\\r\\na=rtcp-fb:100 nack pli\\r\\na=rtpmap:101 H265/90000\\r\\na=fmtp:101 profile-space=0; profile-id=1; level-id=93; max-lsr=33177600; max-lps=983040; max-fps=3000\\r\\na=rtcp-fb:101 hxm-cc\\r\\na=rtpmap:111 rtx/90000\\r\\na=fmtp:111 apt=101\\r\\na=rtp-rtx:101 max-temp-layer=3\\r\\na=rtcp-fb:101 nack pli\\r\\na=rtpmap:102 H265/90000\\r\\na=fmtp:102 profile-space=0; profile-id=1; level-id=63; max-lsr=7372800; max-lps=245760; max-fps=3000\\r\\na=rtcp-fb:102 hxm-cc\\r\\na=rtpmap:112 rtx/90000\\r\\na=fmtp:112 apt=102\\r\\na=rtp-rtx:102 max-temp-layer=3\\r\\na=rtcp-fb:102 nack pli\\r\\na=rtpmap:103 H265/90000\\r\\na=fmtp:103 profile-space=0; profile-id=1; level-id=60; max-lsr=3686400; max-lps=122880; max-fps=3000\\r\\na=rtcp-fb:103 hxm-cc\\r\\na=rtpmap:113 rtx/90000\\r\\na=fmtp:113 apt=103\\r\\na=rtp-rtx:103 max-temp-layer=3\\r\\na=rtcp-fb:103 nack pli\\r\\na=rid:1 recv pt=99 ssrc=67120332;max-temp-layers=3;layer-br-ratio=1:1:2\\r\\na=rid:2 send pt=99 ssrc=67110517\\r\\na=rid:3 recv pt=100 ssrc=67120333;max-temp-layers=3;layer-br-ratio=1:1:2\\r\\na=rid:5 recv pt=101 ssrc=67120334;max-temp-layers=3;layer-br-ratio=1:1:2\\r\\na=rid:7 recv pt=102 ssrc=67120335;max-temp-layers=3;layer-br-ratio=1:1:2\\r\\na=rid:9 recv pt=103 ssrc=67120336;max-temp-layers=3;layer-br-ratio=1:1:2\\r\\na=imageattr:99 recv [x=3840,y=2160] send [x=3840,y=2160]\\r\\na=imageattr:100 recv [x=1920,y=1080] send [x=1920,y=1080]\\r\\na=imageattr:101 recv [x=1280,y=720] send [x=1280,y=720]\\r\\na=imageattr:102 recv [x=640,y=360] send [x=640,y=360]\\r\\na=imageattr:103 recv [x=320,y=180] send [x=320,y=180]\\r\\na=simulcast:recv 1;3;5;7;9 send 2 \\r\\na=rtcp:30002\\r\\na=rtcp-fb:* ccm fir tmmbr\\r\\na=rtcp-fb:* ccm fir\\r\\na=openfec:* no_padding g60\\r\\na=res-neg\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:AB1t9x9wPPew3KrQxZKr7yxmxEdDXYpTDYN8n+Vi|2^31\\r\\nm=application 30002 UDP/BFCP *\\r\\na=floorctrl:s-only\\r\\na=confid:1\\r\\na=userid:58786\\r\\na=floorid:1 m-stream:2\\r\\na=setup:passive\\r\\na=connection:new\\r\\nm=video 30002 RTP/SAVP 99 101\\r\\nb=TIAS:2048000\\r\\na=sendrecv\\r\\na=content:slides\\r\\na=label:2\\r\\na=rtpmap:99 H265/90000\\r\\na=fmtp:99 profile-space=0; profile-id=1; level-id=150; max-lsr=267386880; max-lps=8912896; max-fps=3000\\r\\na=rtpmap:101 rtx/90000\\r\\na=fmtp:101 apt=99\\r\\na=rtp-rtx:99 max-temp-layer=1\\r\\na=rtcp-fb:99 nack pli\\r\\na=rid:1 recv pt=99 ssrc=67120338;max-temp-layers=3;layer-br-ratio=2:1:1\\r\\na=rid:2 send pt=99 ssrc=67110518\\r\\na=imageattr:99 recv [x=3840,y=2160] send [x=3840,y=2160]\\r\\na=simulcast:recv 1 send 2 \\r\\na=rtcp:30002\\r\\na=rtcp-fb:* ccm fir tmmbr\\r\\na=rtcp-fb:* ccm fir\\r\\na=openfec:* no_padding g60\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:tve7vC2LFIh/kPLY/bz45e7JZvk4W8Rt8PQfxlfH|2^31\\r\\nm=application 30002 RTP/SAVP 100\\r\\na=sendrecv\\r\\na=rtpmap:100 H224/4800\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:m+2K0y112/GST3f1RcauEATLYrI3rj0+VkTniqSU|2^31\\r\\na=remb\\r\\na=rtcp:30002\\r\\na=rid:1 recv pt=100 ssrc=67120339\\r\\na=rid:2 send pt=100 ssrc=67110519\\r\\n",                    
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
                        "content":"v=0\\r\\n",
                        "content":"v=0",
                        "call_type":"0",
                        "call_mode":2
                    }'''

    json.loads(inv_200ok)
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

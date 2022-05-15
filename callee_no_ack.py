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
        "content":"v=0\\r\\no=hexmeet-mre 1368 2933 IN IP4 172.20.0.31\\r\\ns=Talk\\r\\nc=IN IP4 172.20.0.31\\r\\nb=AS:2048\\r\\nt=0 0\\r\\na=rtcp-xr:rcvr-rtt=all:10000 stat-summary=loss,dup,jitt,TTL voip-metrics\\r\\na=hxm-conference-control:0\\r\\nm=audio 50000 RTP/SAVP 126 111\\r\\na=rtpmap:126 ARLY/48000\\r\\na=fmtp:126 bitrate=64000\\r\\na=rtpmap:111 telephone-event/8000\\r\\na=fmtp:111 0-15\\r\\na=crypto:1 AES_CM_256_HMAC_SHA1_80 inline:mlf6wck4+jI50KM2tXYGYyp8ylALOg+dd1KfIXbjXjYc54aHjHRSMgY19HgHrQ==\\r\\na=crypto:2 AES_CM_256_HMAC_SHA1_32 inline:D0gFM7NcFvHUmEzGl/Pa9GRmolUttF+gc+rCdsDBEcYzo74yOAdYk7h/H572+Q==\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:PE6Oi+VaHWQT7QrEgTd8sdcyoQFAEJhlSPMsU7No\\r\\na=crypto:4 AES_CM_128_HMAC_SHA1_32 inline:+bg0TIYwLFq7EZWoiF7F12S8RX1Y0b/Ie3/LSs9H\\r\\na=rtcp:50000\\r\\na=openfec:* no_padding g60\\r\\nm=video 50000 RTP/SAVP 99 104 100 105 101 106 102 107 103 108\\r\\na=rtpmap:99 H264/90000\\r\\na=fmtp:99 profile-level-id=640028; sar=13; packetization-mode=1\\r\\na=rtpmap:104 rtx/90000\\r\\na=fmtp:104 apt=99\\r\\na=rtpmap:100 H264/90000\\r\\na=fmtp:100 profile-level-id=64001f; max-br=20010; sar=13; packetization-mode=1\\r\\na=rtpmap:105 rtx/90000\\r\\na=fmtp:105 apt=100\\r\\na=rtpmap:101 H264/90000\\r\\na=fmtp:101 profile-level-id=640015; max-mbps=27000; max-fs=1024; max-br=20010; sar=13; packetization-mode=1\\r\\na=rtpmap:106 rtx/90000\\r\\na=fmtp:106 apt=101\\r\\na=rtpmap:102 H264/90000\\r\\na=fmtp:102 profile-level-id=64000a; max-mbps=3500; max-fs=256; max-br=20010; sar=13; packetization-mode=1\\r\\na=rtpmap:107 rtx/90000\\r\\na=fmtp:107 apt=102\\r\\na=rtpmap:103 H264/90000\\r\\na=fmtp:103 profile-level-id=64000a; max-br=20010; sar=13; packetization-mode=1\\r\\na=rtpmap:108 rtx/90000\\r\\na=fmtp:108 apt=103\\r\\na=content:main\\r\\na=label:1\\r\\na=crypto:1 AES_CM_256_HMAC_SHA1_80 inline:6irgw7EsQlmx9IhlZUjzqJlWl0Lf9coqKjVxMGEwqTqiuhIrgkgnGjhYu4zsuw==\\r\\na=crypto:2 AES_CM_256_HMAC_SHA1_32 inline:4Pc+lQkDVXjMvrdFQT/wWlH5BeOwcMkR2p5OwKlQAtFWvTKFfak2OCKj4p3RrQ==\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:pR69XZ1fk5vpzOwrSEPqURotRJ960r1lUHU9S9Lt\\r\\na=crypto:4 AES_CM_128_HMAC_SHA1_32 inline:7F8KSce2u9W1IivC6iRPrBPI1ITAZr5Jw/V2MJcD\\r\\na=rtcp:50000\\r\\na=rtcp-fb:99 nack pli\\r\\na=rtcp-fb:99 ccm fir\\r\\na=rtcp-fb:99 hxm-cc\\r\\na=rtcp-fb:100 nack pli\\r\\na=rtcp-fb:100 ccm fir\\r\\na=rtcp-fb:100 hxm-cc\\r\\na=rtcp-fb:101 nack pli\\r\\na=rtcp-fb:101 ccm fir\\r\\na=rtcp-fb:101 hxm-cc\\r\\na=rtcp-fb:102 nack pli\\r\\na=rtcp-fb:102 ccm fir\\r\\na=rtcp-fb:102 hxm-cc\\r\\na=rtcp-fb:103 nack pli\\r\\na=rtcp-fb:103 ccm fir\\r\\na=rtcp-fb:103 hxm-cc\\r\\na=max-recv-streams:9; c4k=1; c1080=2; c720=3; c360=4; c180=5; c90=6\\r\\na=auto-speaker-layout:101,202,301,404,503\\r\\na=auto-gallery-layout:101,201,401,602,604,901\\r\\na=imageattr:99 send [x=1920,y=1080] recv [x=1920,y=1080]\\r\\na=rid:1 send pt=99 max-br=1137; max-temp-layers=2; layer-br-ratio=1:1\\r\\na=rid:2 recv pt=99\\r\\na=imageattr:100 send [x=1280,y=720] recv [x=1280,y=720]\\r\\na=rid:3 send pt=100 max-br=568; max-temp-layers=2; layer-br-ratio=1:1\\r\\na=rid:4 recv pt=100\\r\\na=imageattr:101 send [x=640,y=360] recv [x=640,y=360]\\r\\na=rid:5 send pt=101 max-br=227; max-temp-layers=2; layer-br-ratio=1:1\\r\\na=rid:6 recv pt=101\\r\\na=imageattr:102 send [x=320,y=180] recv [x=320,y=180]\\r\\na=rid:7 send pt=102 max-br=85; max-temp-layers=2; layer-br-ratio=1:1\\r\\na=rid:8 recv pt=102\\r\\na=imageattr:103 send [x=160,y=90] recv [x=160,y=90]\\r\\na=rid:9 send pt=103 max-br=28; max-temp-layers=2; layer-br-ratio=1:1\\r\\na=rid:10 recv pt=103\\r\\na=simulcast:\\r\\na=res-neg\\r\\na=rtp-rtx:99 max-temp-layer=1\\r\\na=rtp-rtx:100 max-temp-layer=1\\r\\na=rtp-rtx:101 max-temp-layer=1\\r\\na=rtp-rtx:102 max-temp-layer=1\\r\\na=rtp-rtx:103 max-temp-layer=1\\r\\na=openfec:* no_padding g60\\r\\na=rtcp-ltrf:99\\r\\na=rtcp-ltrf:100\\r\\na=rtcp-ltrf:101\\r\\na=rtcp-ltrf:102\\r\\na=rtcp-ltrf:103\\r\\nm=application 50000 UDP/BFCP *\\r\\na=floorctrl:c-s\\r\\na=setup:actpass\\r\\na=connection:new\\r\\na=confid:1\\r\\na=userid:2\\r\\na=floorid:1 mstrm:3\\r\\nm=video 50000 RTP/SAVP 99 100\\r\\na=rtpmap:99 H264/90000\\r\\na=fmtp:99 profile-level-id=640016; max-mbps=122000; max-fs=8192; sar=13; packetization-mode=1\\r\\na=rtpmap:100 rtx/90000\\r\\na=fmtp:100 apt=99\\r\\na=content:slides\\r\\na=label:3\\r\\na=crypto:1 AES_CM_256_HMAC_SHA1_80 inline:mW8QHpP6uuy0FAe4/9QnbA1DpIPnJjX0xKvLtUIR1JK3nKGW5FCjfPEq0VNYQA==\\r\\na=crypto:2 AES_CM_256_HMAC_SHA1_32 inline:qYfT6EW5U63aTSAGfbS/hrvBEEGlllOxsLn+tZE47ufAG/rOt2/RGg8+gZXY1w==\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:3xHMSGF25+W4eI3fStQOCEFKHKacJuwpT2EfkgT2\\r\\na=crypto:4 AES_CM_128_HMAC_SHA1_32 inline:cTVSjOmk/Aonc/udqzbhnt0vxFuB3CSyJq9TpUdO\\r\\na=rtcp:50000\\r\\na=rtcp-fb:99 nack pli\\r\\na=rtcp-fb:99 ccm fir\\r\\na=max-recv-streams:1\\r\\na=imageattr:99 send [x=1920,y=1080] recv [x=1920,y=1080]\\r\\na=rid:1 send pt=99 max-br=1433; max-temp-layers=2; layer-br-ratio=2:1\\r\\na=rid:2 recv pt=99\\r\\na=simulcast:send 0 recv 0\\r\\na=res-neg\\r\\na=rtp-rtx:99 max-temp-layer=1\\r\\na=openfec:* no_padding g60\\r\\na=rtcp-ltrf:99\\r\\nm=application 50000 RTP/SAVP 100\\r\\na=rtpmap:100 H224/4800\\r\\na=fmtp:100\\r\\na=crypto:1 AES_CM_256_HMAC_SHA1_80 inline:YE40zb9l+j5om7ilzcE528+mcEdzlbRTHPd0QMPuEKVQIZIIbr5Y+p0k3J058A==\\r\\na=crypto:2 AES_CM_256_HMAC_SHA1_32 inline:Brsob0cBarTo7dEd/8BDfu8Y02LzWu6tvIAMtmS/1CdyiMXcj2N6HyQ7bSbE8A==\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:mys185TIF7XpGPSy909wepQr9EyKJWwEVw53gNiw\\r\\na=crypto:4 AES_CM_128_HMAC_SHA1_32 inline:szMfRwW5B/ZFHU0wuvSr7y0DZMKzzFKGB8ZaXnhy\\r\\na=rtcp:50000\\r\\na=remb\\r\\n",
        "event":"",
        "source_ip":"172.26.0.153",
        "call_mode":2,
        "to_type":2,
        "region":{
            "city_code":0,
            "country":"0",
            "province":"0",
            "city":"内网IP"
        }
    }'''
    ##"content": "v=0\\r\\no=MCU 1164457869 0 IN IP4 172.25.0.165\\r\\ns=NGMCU\\r\\nc=IN IP4 172.25.0.165\\r\\nb=AS:4096\\r\\nt=0 0\\r\\na=hxm-conference-control:0\\r\\na=whiteboard:1\\r\\nm=audio 30002 RTP/SAVP 126 111\\r\\na=sendrecv\\r\\na=rtpmap:126 ARLY/48000\\r\\na=fmtp:126 bitrate=64000\\r\\na=rid:1 recv pt=126 ssrc=67120331\\r\\na=rid:2 send pt=126 ssrc=67110516\\r\\na=rtpmap:111 telephone-event/8000\\r\\na=fmtp:111 0-15\\r\\na=openfec:* no_padding\\r\\na=rtcp:30002\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:O8Vi2lKh4i8g5Nsx3WxgE3swppmlanjhacKF9BEX|2^31\\r\\nm=video 30002 RTP/SAVP 99 109 100 110 101 111 102 112 103 113\\r\\nb=TIAS:4096000\\r\\na=sendrecv\\r\\na=content:main\\r\\na=label:1\\r\\na=rtpmap:99 H265/90000\\r\\na=fmtp:99 profile-space=0; profile-id=1; level-id=150; max-lsr=267386880; max-lps=8912896; max-fps=3000\\r\\na=rtcp-fb:99 hxm-cc\\r\\na=rtpmap:109 rtx/90000\\r\\na=fmtp:109 apt=99\\r\\na=rtp-rtx:99 max-temp-layer=3\\r\\na=rtcp-fb:99 nack pli\\r\\na=rtpmap:100 H265/90000\\r\\na=fmtp:100 profile-space=0; profile-id=1; level-id=120; max-lsr=66846720; max-lps=2228224; max-fps=3000\\r\\na=rtcp-fb:100 hxm-cc\\r\\na=rtpmap:110 rtx/90000\\r\\na=fmtp:110 apt=100\\r\\na=rtp-rtx:100 max-temp-layer=3\\r\\na=rtcp-fb:100 nack pli\\r\\na=rtpmap:101 H265/90000\\r\\na=fmtp:101 profile-space=0; profile-id=1; level-id=93; max-lsr=33177600; max-lps=983040; max-fps=3000\\r\\na=rtcp-fb:101 hxm-cc\\r\\na=rtpmap:111 rtx/90000\\r\\na=fmtp:111 apt=101\\r\\na=rtp-rtx:101 max-temp-layer=3\\r\\na=rtcp-fb:101 nack pli\\r\\na=rtpmap:102 H265/90000\\r\\na=fmtp:102 profile-space=0; profile-id=1; level-id=63; max-lsr=7372800; max-lps=245760; max-fps=3000\\r\\na=rtcp-fb:102 hxm-cc\\r\\na=rtpmap:112 rtx/90000\\r\\na=fmtp:112 apt=102\\r\\na=rtp-rtx:102 max-temp-layer=3\\r\\na=rtcp-fb:102 nack pli\\r\\na=rtpmap:103 H265/90000\\r\\na=fmtp:103 profile-space=0; profile-id=1; level-id=60; max-lsr=3686400; max-lps=122880; max-fps=3000\\r\\na=rtcp-fb:103 hxm-cc\\r\\na=rtpmap:113 rtx/90000\\r\\na=fmtp:113 apt=103\\r\\na=rtp-rtx:103 max-temp-layer=3\\r\\na=rtcp-fb:103 nack pli\\r\\na=rid:1 recv pt=99 ssrc=67120332;max-temp-layers=3;layer-br-ratio=1:1:2\\r\\na=rid:2 send pt=99 ssrc=67110517\\r\\na=rid:3 recv pt=100 ssrc=67120333;max-temp-layers=3;layer-br-ratio=1:1:2\\r\\na=rid:5 recv pt=101 ssrc=67120334;max-temp-layers=3;layer-br-ratio=1:1:2\\r\\na=rid:7 recv pt=102 ssrc=67120335;max-temp-layers=3;layer-br-ratio=1:1:2\\r\\na=rid:9 recv pt=103 ssrc=67120336;max-temp-layers=3;layer-br-ratio=1:1:2\\r\\na=imageattr:99 recv [x=3840,y=2160] send [x=3840,y=2160]\\r\\na=imageattr:100 recv [x=1920,y=1080] send [x=1920,y=1080]\\r\\na=imageattr:101 recv [x=1280,y=720] send [x=1280,y=720]\\r\\na=imageattr:102 recv [x=640,y=360] send [x=640,y=360]\\r\\na=imageattr:103 recv [x=320,y=180] send [x=320,y=180]\\r\\na=simulcast:recv 1;3;5;7;9 send 2 \\r\\na=rtcp:30002\\r\\na=rtcp-fb:* ccm fir tmmbr\\r\\na=rtcp-fb:* ccm fir\\r\\na=openfec:* no_padding g60\\r\\na=res-neg\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:AB1t9x9wPPew3KrQxZKr7yxmxEdDXYpTDYN8n+Vi|2^31\\r\\nm=application 30002 UDP/BFCP *\\r\\na=floorctrl:s-only\\r\\na=confid:1\\r\\na=userid:58786\\r\\na=floorid:1 m-stream:2\\r\\na=setup:passive\\r\\na=connection:new\\r\\nm=video 30002 RTP/SAVP 99 101\\r\\nb=TIAS:2048000\\r\\na=sendrecv\\r\\na=content:slides\\r\\na=label:2\\r\\na=rtpmap:99 H265/90000\\r\\na=fmtp:99 profile-space=0; profile-id=1; level-id=150; max-lsr=267386880; max-lps=8912896; max-fps=3000\\r\\na=rtpmap:101 rtx/90000\\r\\na=fmtp:101 apt=99\\r\\na=rtp-rtx:99 max-temp-layer=1\\r\\na=rtcp-fb:99 nack pli\\r\\na=rid:1 recv pt=99 ssrc=67120338;max-temp-layers=3;layer-br-ratio=2:1:1\\r\\na=rid:2 send pt=99 ssrc=67110518\\r\\na=imageattr:99 recv [x=3840,y=2160] send [x=3840,y=2160]\\r\\na=simulcast:recv 1 send 2 \\r\\na=rtcp:30002\\r\\na=rtcp-fb:* ccm fir tmmbr\\r\\na=rtcp-fb:* ccm fir\\r\\na=openfec:* no_padding g60\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:tve7vC2LFIh/kPLY/bz45e7JZvk4W8Rt8PQfxlfH|2^31\\r\\nm=application 30002 RTP/SAVP 100\\r\\na=sendrecv\\r\\na=rtpmap:100 H224/4800\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:m+2K0y112/GST3f1RcauEATLYrI3rj0+VkTniqSU|2^31\\r\\na=remb\\r\\na=rtcp:30002\\r\\na=rid:1 recv pt=100 ssrc=67120339\\r\\na=rid:2 send pt=100 ssrc=67110519\\r\\n",
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
        "call_mode":2,
        "to_type":1
    }'''
    return common.update_msg_info(bye_msg, uid, deviceid, to, callid)

async def main_logic():
    deviceid = 40003
    #random.randint(40000, 45000)
    username = "simu1237"
    #simu" + str(random.randint(60000, 65000))
    uid = 30003
    to = "40004"
    dst_uid = "30004"
    #random.randint(30000, 35000)
    token = common.get_jwt_token(username, deviceid)
    async with websockets.connect('ws://127.0.0.1:9002/websocket/messsage?token=' + token) as websocket:
        print("connected")
        register_msg = common.gen_register_req(str(uid), str(deviceid))
        print(register_msg)
        await common.send_msg_and_await_rsp(register_msg,websocket)
        time.sleep(2)
        invite_msg = gen_invite(str(uid),str(deviceid), dst_uid)
        print('<=' + invite_msg)
        await common.send_msg_and_await_rsp(invite_msg, websocket)
        #time.sleep(2)
        obj = json.loads(invite_msg)
        callid = obj['callid']
        print("await another retransmit msg")
        #send ack
        # obj["method"] = "ACK"
        # obj["to_type"] = 2
        # ack = json.dumps(obj)
        # print('<=' + ack)
        # await websocket.send(ack)
        response_str = await websocket.recv()
        print('=>' + response_str)
        time.sleep(5)
        bye_msg = gen_bye(str(uid), str(deviceid),  to, callid)
        print('<=' + bye_msg)
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

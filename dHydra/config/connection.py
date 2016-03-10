# -*- coding: utf8 -*-
"""
Connection Settings
Created on 02/26/2016
@description:	Used for 
@author: 		Wen Gu
@contact: 		emptyset110@gmail.com
"""

"""
新浪财经
FROM ssologin.js(v1.4.18)
"""
import time
import random

CLIENT = "ssologin.js(v1.4.18)"
CROSSDOMAIN_HOST = [
	"passport.weibo.com"
,	"crosdom.weicaifu.com"
,	"passport.weibo.cn"
]

HEADERS_LOGIN = {
	"Accept" : '*/*'
,	"Accept-Encoding" : 'gzip, deflate, sdch'
,	"Accept-Language" : 'en-US,en;q=0.8'
,	"Connection" : 'keep-alive'
,	"Host" : 'login.sina.com.cn'
,	"Referer" : 'http://finance.sina.com.cn/'
,	"User-Agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
}
PARAM_L2HIST = lambda symbol,page: {
	"symbol"			:	symbol
,	"callback"			:	"jQuery17209838373235483986_" + str( int(time.time()*1000) )
,	"pageNum"			:	10000
,	"page"				:	page
,	"stime"				:	'09:25:00'
,	"etime"				:	'15:05:00'
,	"sign"				:	''
,	"num"				:	'20'
,	"_"					:	int(time.time()*1000)
}
HEADERS_L2 = lambda symbol	: {
	'Host'				:	'stock.finance.sina.com.cn'
,	'Connection'		:	'keep-alive'
,	'Accept'			:	'*/*'
,	'User-Agent'		:	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
,	'Referer'			:	'http://vip.stock.finance.sina.com.cn/quotes_service/view/l2_tradedetail.php?symbol=%s' % symbol
,	'Accept-Encoding'	:	'gzip, deflate, sdch'
,	'Accept-Language'	:	'en-US,en;q=0.8'
}
HEADERS_WSKT_TOKEN = lambda 	:	{
	'Accept'					:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
,	'Accept-Encoding'			:	'gzip, deflate, sdch'
,	'Accept-Language'			:	'en-US,en;q=0.8'
,	'Connection'				:	'keep-alive'
,	'Host'						:	'current.sina.com.cn'
,	'User-Agent'				:	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
,	'Referer'					:	'http://finance.sina.com.cn/realstock/company/sz300204/l2.shtml'
# ,	"Cookie"					:	"UOR=,finance.sina.com.cn,; SINAGLOBAL=117.85.56.181_1456667771.258251; vjuids=-4299b1d0a.153282a4536.0.63624093; SGUID=1456667772264_5d5aafd5; U_TRS1=000000b5.5238d9b.56d2fc7c.5af26a8b; lxlrtst=1457139560_c; ArtiFSize=14; Apache=221.227.4.159_1457548762.812349; U_TRS2=0000009f.8b4c60c3.56e06ddb.b1cf7a44; ULV=1457548764592:16:14:11:221.227.4.159_1457548762.812349:1457548763017; usrmdpool=usrmdinst_4; SessionID=274ubc2f1vpfgn0p1m5g7p4j81; vjlast=1457552280; lxlrttp=1457516257; ULOGIN_IMG=gz-8eb0f9dc72a2210895619c82f8973929664c; SUS=SID-3341633314-1457552529-GZ-jkpet-e6947bd2432c7bc5cb423c8599ce6c52; SUE=es%3Dcab851dfba86aaaa40e82a45c0ae9d48%26ev%3Dv1%26es2%3D4f0b9b69c8415751fac8b7855702612b%26rs0%3DyVeIY5YqTKcveiDkaCwn2YByliyE2Ig5ChkAd4deQhlGCrKFEZJM1oJXmnAwpJDyiCV4vgpIUWHgV6Hv09fMYVznGFvblRr5Dr6Inknwl6lNaXMXXUjTLXSNUMNYLQW1VmqAZfVH9t%252BbJhWYCvJ%252FPNPARJRjjj4SjLMXX9ENlOE%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1457552529%26et%3D1457638929%26d%3D40c3%26i%3D6c52%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D6%26st%3D0%26lt%3D1%26uid%3D3341633314%26user%3D13373635073%26ag%3D1%26name%3D13373635073%26nick%3DOriginal_Emptyset%26sex%3D%26ps%3D0%26email%3D%26dob%3D%26ln%3D13373635073%26os%3D%26fmp%3D%26lcp%3D2016-03-10%252003%253A18%253A04; SUB=_2A2575AzBDeRxGeVN71MX8y3PyjiIHXVYkHkJrDV_PUNbuNBeLXfekW9LHetA9a_fGyYITeJjrjjraMGDKLCq5w..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh0iz-ugMVN5EgRvkEg4y1X; ALF=1489088529; sso_info=v02m6alo5qztY-cpqWnmpa5oZuFvYWbl4G0npeNpZ2CmbWalpC9jLOMtIyTmLOMs4yxjYDAwA==; rotatecount=27"
}
HEADERS_CROSSDOMAIN = lambda host	:	{
	'Host'							:	host
,	'User-Agent'					:	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
,	'Accept'						: 	'*/*'
,	'Accept-Language'				:	'en-US,en;q=0.5'
,	'Accept-Encoding'				:	'gzip, deflate'
,	'Referer'						:	'http://finance.sina.com.cn/realstock/company/sz300204/l2.shtml'
,	'Connection'					:	'keep-alive'
}
PARAM_LOGIN = lambda : {
	"client" 		:	CLIENT
,	"_"				:	int(time.time()*1000)
}
PARAM_PRELOGIN = lambda su : {
	"entry"			:	"finance"
,	"callback"		:	"sinaSSOController.preloginCallBack"
,	"su"			:	su
,	"rsakt"			:	'mod'
,	"client"		:	CLIENT
,	"_"				:	int(time.time()*1000)
}
PARAM_WSKT_TOKEN = lambda ip, qlist: {
	"query"	:	"hq_pjb"
,	"ip"	:	ip
,	"_"		:	random.uniform(0.1,0.2)
,	"kick"	:	1
,	"list"	:	qlist
}
DATA_LOGIN = lambda su,servertime,nonce,rsakv,sp: {
	"entry"			:	"finance"
,	"gateway"		:	1
,	"from"			:	""
,	"savestate" 	:	30
,	"useticket" 	:	0
,	"pagerefer" 	:	""
,	"vsnf"			:	"1"
,	"su"			:	su
,	"service"		:	"sso"
,	"servertime"	:	servertime
,	"nonce"			:	nonce
,	"pwencode"		:	"rsa2"
,	"rsakv"			:	rsakv
,	"sp"			:	sp
,	"sr" 			:	"1920*1080"
,	"encoding"		:	"UTF-8"
,	"cdult"			:	3
,	"domain"		:	"sina.com.cn"
,	"prelt"			:	72
,	"returntype"	:	"TEXT"
}

URL_CROSSDOMAIN = "http://login.sina.com.cn/sso/crossdomain.php"
URL_SSOLOGIN = "http://login.sina.com.cn/sso/login.php"
URL_SSOLOGOUT = "http://login.sina.com.cn/sso/logout.php"
URL_UPDATECOOKIE = "http://login.sina.com.cn/sso/updatetgt.php"
URL_PRELOGIN = "http://login.sina.com.cn/sso/prelogin.php"
URL_PINCODE = "http://login.sina.com.cn/cgi/pin.php"
URL_VFVALID = "http://weibo.com/sguide/vdun.php"

URL_L2HIST = 'http://stock.finance.sina.com.cn/stock/api/openapi.php/StockLevel2Service.getTransactionList'
URL_WSKT_TOKEN = 'https://current.sina.com.cn/auth/api/jsonp.php/var%20KKE_auth_OSfOoonMj=/AuthSign_Service.getSignCode'
SOCKET_BASE = 'ws://ff.sinajs.cn/wskt'

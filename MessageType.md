# Message Type


| 消息类型代码   | 描述                           |
|----------------|--------------------------------|
| 0              | 朋友圈消息                     |
| 1              | 文字                           |
| 3              | 图片                           |
| 34             | 语音                           |
| 37             | 好友确认                       |
| 40             | POSSIBLEFRIEND_MSG            |
| 42             | 名片                           |
| 43             | 视频                           |
| 47             | 石头剪刀布 或 表情图片          |
| 48             | 位置                           |
| 49             | 共享实时位置、文件、转账、链接 |
| 50             | VOIPMSG                        |
| 51             | 微信初始化                     |
| 52             | VOIPNOTIFY                     |
| 53             | VOIPINVITE                     |
| 62             | 小视频                         |
| 66             | 微信红包                       |
| 9999           | SYSNOTICE                      |
| 10000          | 红包、系统消息                 |
| 10002          | 撤回消息                       |
| 1048625        | 搜狗表情                       |
| 16777265       | 链接                           |
| 436207665      | 微信红包                       |
| 536936497      | 红包封面                       |
| 754974769      | 视频号视频                     |
| 771751985      | 视频号名片                     |
| 822083633      | 引用消息                       |
| 922746929      | 拍一拍                         |
| 973078577      | 视频号直播                     |
| 974127153      | 商品链接                       |
| 975175729      | 视频号直播                     |
| 1040187441     | 音乐链接                       |
| 1090519089     | 文件                           |


**文本 1**
```xml
- header
wxid_jrpmphrrct5n21[wxid_jrpmphrrct5n21]|1513032632607765485|2025-03-28 00:04:34|1|0b27c3cd230f1058b34fd4dafe8e3b65
- source
<msgsource>
  <pua>1</pua>
  <eggIncluded>1</eggIncluded>
  <signature>N0_V1_RsPUUhnx|v1_Bx1IoL+L</signature>
  <tmp_node>
    <publisher-id />
  </tmp_node>
  <sec_msg_node>
    <alnode>
      <fr>1</fr>
    </alnode>
  </sec_msg_node>
</msgsource>
- content
123
```

**图片 3**
```xml
wxid_jrpmphrrct5n21[wxid_jrpmphrrct5n21]|6602511768485105124|2025-03-28 00:42:10|3|eafc12c171b3cc045107768d2765ffca
<msgsource>    <sec_msg_node>        <uuid>354cf962bac94e820fb6a45ae399cc8e_</uuid>        <risk-file-flag />        <risk-file-md5-list />        <alnode>            <fr>1</fr>        </alnode>    </sec_msg_node>    <imgmsg_pd cdnmidimgurl_size="107114" cdnmidimgurl_pd_pri="30" cdnmidimgurl_pd="0" />    <signature>N0_V1_plFrcG9t|v1_ENg7Bc5V</signature>    <tmp_node>        <publisher-id />    </tmp_node></msgsource>

- content
<?xml version="1.0"?>
<msg>
        <img aeskey="eff5b5743867193d5082ef24437120c9" encryver="1" cdnthumbaeskey="eff5b5743867193d5082ef24437120c9" cdnthumburl="3057020100044b30490201000204d48e135e02032f5aa90204a5996971020467e51869042437393062653961642d383462612d343139372d383236642d633137626636633330346465020405150a020201000405004c55cd00" cdnthumblength="6231" cdnthumbheight="576" cdnthumbwidth="300" cdnmidheight="0" cdnmidwidth="0" cdnhdheight="0" cdnhdwidth="0" cdnmidimgurl="3057020100044b30490201000204d48e135e02032f5aa90204a5996971020467e51869042437393062653961642d383462612d343139372d383236642d633137626636633330346465020405150a020201000405004c55cd00" length="737482" md5="b0199f922d038be12efccf8f41a7afc9" hevc_mid_size="107114" originsourcemd5="7f5f1d08f201c12ca1b4f10888363651">
                <secHashInfoBase64>eyJwaGFzaCI6IjEwMTA1MDEwYjA1MDkwMDAiLCJwZHFIYXNoIjoiNTU5YWQ1MGU4ZDI1ODY3Y2Q3
NWFjMzA5OGY4Nzk3MTYzYjRiY2Q0OTk3NDZhZjViNmExMTg1ODRhYmM2OGQ1MyJ9
</secHashInfoBase64>
                <live>
                        <duration>0</duration>
                        <size>0</size>
                        <md5 />
                        <fileid />
                        <hdsize>0</hdsize>
                        <hdmd5 />
                        <hdfileid />
                        <stillimagetimems>0</stillimagetimems>
                </live>
        </img>
        <platform_signature />
        <imgdatahash />
        <ImgSourceInfo>
                <ImgSourceUrl />
                <BizType>0</BizType>
        </ImgSourceInfo>
</msg>

- thumb&extra
缩略图路径
原图路径
C:/Users/CSY/Documents/WeChat Files/wxid_pvebx6dozp3r19/FileStorage/MsgAttach/baf923f18e7cf3462bd6fe820f0b9fab/Thumb/2025-03/b1755b467e19a9ee0402cb9407e2d72d_t.dat
C:/Users/CSY/Documents/WeChat Files/wxid_pvebx6dozp3r19/FileStorage/MsgAttach/baf923f18e7cf3462bd6fe820f0b9fab/Image/2025-03/48c122d8bf597d27bc982d344eb37317.dat
```

**语音 34**
疑问，文件路径不清楚是extra还是thumb
```xml
wxid_jrpmphrrct5n21[wxid_jrpmphrrct5n21]|8048852312300487515|2025-03-28 00:48:33|34|41303636383833393538643530666500290048032825baf923f308f103

<msgsource>    <signature>N0_V1_86kh1i5R|v1_p32e/LtP</signature>    <tmp_node>        <publisher-id />    </tmp_node>    <sec_msg_node>        <alnode>            <fr>1</fr>        </alnode>    </sec_msg_node></msgsource>
- content
<msg><voicemsg endflag="1" cancelflag="0" forwardflag="0" voiceformat="4" voicelength="3236" length="4516" bufid="0" aeskey="68d42b7621601eb33fe3e2b99df5a2d7" voiceurl="3052020100044b304902010002046ce844e702032f5aa9020427996971020467e58161042435363865666264342d383264312d346130382d396431632d37343734613165663036373702040518000f0201000400" voicemd5="" clientmsgid="41303636383833393538643530666500290048032825baf923f308f103" fromusername="wxid_jrpmphrrct5n21" /></msg>

C:/Users/CSY/Documents/WeChat Files/3236

```



**表情包 47**



**链接 49**
wxid_jrpmphrrct5n21[wxid_jrpmphrrct5n21]|573441918258362773|2025-03-28 00:54:23|49|c646cdc5288d0e2f131c7b3cf5856e27
<msgsource>    <sec_msg_node>        <uuid>c64982f5a34673afc641cda658a6ede5_</uuid>        <risk-file-flag />        <risk-file-md5-list />        <alnode>            <fr>1</fr>        </alnode>    </sec_msg_node>    <signature>N0_V1_xps9z80z|v1_jxTp3bZ0</signature>    <tmp_node>        <publisher-id />    </tmp_node></msgsource>
<?xml version="1.0"?>
<msg>
	<appmsg appid="" sdkver="0">
		<title>特朗普开始抱怨俄罗斯</title>
		<des></des>
		<username />
		<action>view</action>
		<type>5</type>
		<showtype>0</showtype>
		<content />
		<url>http://mp.weixin.qq.com/s?__biz=MjM5MzA0MTg2MA==&amp;mid=2654544522&amp;idx=2&amp;sn=9eb839a6cb6d2d8878b051707292af8d&amp;chksm=bc2b0846ec64158cc6403ac6e263e51d0ad6ca4437b807c9f5baad99b2d3089043422d45a0a6&amp;mpshare=1&amp;scene=1&amp;srcid=0328Jd3woiRXImPWXWnbzlYm&amp;sharer_shareinfo=d734c0b7e03fc6e46cf25366eb024ae3&amp;sharer_shareinfo_first=d734c0b7e03fc6e46cf25366eb024ae3#rd</url>
		<lowurl />
		<forwardflag>0</forwardflag>
		<dataurl />
		<lowdataurl />
		<contentattr>0</contentattr>
		<streamvideo>
			<streamvideourl />
			<streamvideototaltime>0</streamvideototaltime>
			<streamvideotitle />
			<streamvideowording />
			<streamvideoweburl />
			<streamvideothumburl />
			<streamvideoaduxinfo />
			<streamvideopublishid />
		</streamvideo>
		<canvasPageItem>
			<canvasPageXml><![CDATA[]]></canvasPageXml>
		</canvasPageItem>
		<appattach>
			<attachid />
			<cdnthumburl>3057020100044b304902010002044e8e116a02032f5aa902049f996971020467e53b83042438356631326563382d663762612d346263312d383430342d3136303530366330353630310204051408030201000405004c50b900</cdnthumburl>
			<cdnthumbmd5>0737041c62b4e7cef51bf40b59477017</cdnthumbmd5>
			<cdnthumblength>23491</cdnthumblength>
			<cdnthumbheight>120</cdnthumbheight>
			<cdnthumbwidth>120</cdnthumbwidth>
			<cdnthumbaeskey>c07b3cc74645e6ed08b66bdc16847870</cdnthumbaeskey>
			<aeskey>c07b3cc74645e6ed08b66bdc16847870</aeskey>
			<encryver>1</encryver>
			<fileext />
			<islargefilemsg>0</islargefilemsg>
		</appattach>
		<extinfo />
		<androidsource>2</androidsource>
		<sourceusername>gh_2837b93c1976</sourceusername>
		<sourcedisplayname>参考消息</sourcedisplayname>
		<commenturl />
		<thumburl />
		<mediatagname />
		<messageaction><![CDATA[]]></messageaction>
		<messageext><![CDATA[]]></messageext>
		<emoticongift>
			<packageflag>0</packageflag>
			<packageid />
		</emoticongift>
		<emoticonshared>
			<packageflag>0</packageflag>
			<packageid />
		</emoticonshared>
		<designershared>
			<designeruin>0</designeruin>
			<designername>null</designername>
			<designerrediretcturl><![CDATA[null]]></designerrediretcturl>
		</designershared>
		<emotionpageshared>
			<tid>0</tid>
			<title>null</title>
			<desc>null</desc>
			<iconUrl><![CDATA[null]]></iconUrl>
			<secondUrl>null</secondUrl>
			<pageType>0</pageType>
			<setKey>null</setKey>
		</emotionpageshared>
		<webviewshared>
			<shareUrlOriginal>http://mp.weixin.qq.com/s?__biz=MjM5MzA0MTg2MA==&amp;mid=2654544522&amp;idx=2&amp;sn=9eb839a6cb6d2d8878b051707292af8d&amp;chksm=bce4366fb898b83e07bae7540deadc01b4067b327b78e20a08582306e437cf2fd83c4640e395&amp;xtrack=1&amp;scene=90&amp;subscene=93&amp;sessionid=1743094456&amp;flutter_pos=0&amp;clicktime=1743094458&amp;enterid=1743094458&amp;finder_biz_enter_id=4&amp;ranksessionid=1743092899&amp;ascene=56&amp;fasttmpl_type=0&amp;fasttmpl_fullversion=7662766-zh_CN-zip&amp;fasttmpl_flag=0&amp;realreporttime=1743094458400#rd</shareUrlOriginal>
			<shareUrlOpen>https://mp.weixin.qq.com/s?__biz=MjM5MzA0MTg2MA==&amp;mid=2654544522&amp;idx=2&amp;sn=9eb839a6cb6d2d8878b051707292af8d&amp;chksm=bce4366fb898b83e07bae7540deadc01b4067b327b78e20a08582306e437cf2fd83c4640e395&amp;xtrack=1&amp;scene=90&amp;subscene=93&amp;sessionid=1743094456&amp;flutter_pos=0&amp;clicktime=1743094458&amp;enterid=1743094458&amp;finder_biz_enter_id=4&amp;ranksessionid=1743092899&amp;ascene=56&amp;fasttmpl_type=0&amp;fasttmpl_fullversion=7662766-zh_CN-zip&amp;fasttmpl_flag=0&amp;realreporttime=1743094458400&amp;devicetype=android-35&amp;version=2800385e&amp;nettype=WIFI&amp;lang=zh_CN&amp;session_us=gh_2837b93c1976&amp;countrycode=CN&amp;exportkey=n_ChQIAhIQdqGdVDfiEpRFDBXucyKMOhLxAQIE97dBBAEAAAAAAE6cGgjsWGcAAAAOpnltbLcz9gKNyK89dVj08ilxX%2FrSKZ6PZ%2FIGbs2KjuFMtgG8An%2BbX13s%2BBb%2FXkT1JJ5YdKbXhOm9evJ0HBYHiLB5z74lQhcJavVZwEQSACrjpe4hkpECQlTMfcJuuTjUlPIrIT85KPbXjsHFJWihkWjPxPxMWdFbwmWX8fBWyLP5mw4y9OvkgW%2BrRO0Wr0na94dmFBvUQJ10PTXQ3yL0jZVglc9DfdhXL1wsntGD%2BjQUjvJtX5A378%2Fn2kt%2Byo4%2BkT6mW7utXsqbfuRSyerLyQo%2F%2FQQ1KwUkbus%3D&amp;pass_ticket=aRd22hglaiOnOifEJ9YjjeLHnrSQsStNdz3Ns9cxfbXspW4uT1fvPHWob13lctXv&amp;wx_header=3</shareUrlOpen>
			<jsAppId />
			<publisherId>msg_10058727</publisherId>
			<publisherReqId>1485218850</publisherReqId>
		</webviewshared>
		<template_id />
		<md5>0737041c62b4e7cef51bf40b59477017</md5>
		<websearch>
			<rec_category>0</rec_category>
			<channelId>0</channelId>
		</websearch>
		<weappinfo>
			<username />
			<appid />
			<appservicetype>0</appservicetype>
			<secflagforsinglepagemode>0</secflagforsinglepagemode>
			<videopageinfo>
				<thumbwidth>120</thumbwidth>
				<thumbheight>120</thumbheight>
				<fromopensdk>0</fromopensdk>
			</videopageinfo>
		</weappinfo>
		<statextstr />
		<mmreadershare>
			<itemshowtype>0</itemshowtype>
			<ispaysubscribe>0</ispaysubscribe>
		</mmreadershare>
		<musicShareItem>
			<musicDuration>0</musicDuration>
		</musicShareItem>
		<finderLiveProductShare>
			<finderLiveID><![CDATA[]]></finderLiveID>
			<finderUsername><![CDATA[]]></finderUsername>
			<finderObjectID><![CDATA[]]></finderObjectID>
			<finderNonceID><![CDATA[]]></finderNonceID>
			<liveStatus><![CDATA[]]></liveStatus>
			<appId><![CDATA[]]></appId>
			<pagePath><![CDATA[]]></pagePath>
			<productId><![CDATA[]]></productId>
			<coverUrl><![CDATA[]]></coverUrl>
			<productTitle><![CDATA[]]></productTitle>
			<marketPrice><![CDATA[0]]></marketPrice>
			<sellingPrice><![CDATA[0]]></sellingPrice>
			<platformHeadImg><![CDATA[]]></platformHeadImg>
			<platformName><![CDATA[]]></platformName>
			<shopWindowId><![CDATA[]]></shopWindowId>
			<flashSalePrice><![CDATA[0]]></flashSalePrice>
			<flashSaleEndTime><![CDATA[0]]></flashSaleEndTime>
			<ecSource><![CDATA[]]></ecSource>
			<sellingPriceWording><![CDATA[]]></sellingPriceWording>
			<platformIconURL><![CDATA[]]></platformIconURL>
			<firstProductTagURL><![CDATA[]]></firstProductTagURL>
			<firstProductTagAspectRatioString><![CDATA[0.0]]></firstProductTagAspectRatioString>
			<secondProductTagURL><![CDATA[]]></secondProductTagURL>
			<secondProductTagAspectRatioString><![CDATA[0.0]]></secondProductTagAspectRatioString>
			<firstGuaranteeWording><![CDATA[]]></firstGuaranteeWording>
			<secondGuaranteeWording><![CDATA[]]></secondGuaranteeWording>
			<thirdGuaranteeWording><![CDATA[]]></thirdGuaranteeWording>
			<isPriceBeginShow>false</isPriceBeginShow>
			<lastGMsgID><![CDATA[]]></lastGMsgID>
			<promoterKey><![CDATA[]]></promoterKey>
			<discountWording><![CDATA[]]></discountWording>
			<priceSuffixDescription><![CDATA[]]></priceSuffixDescription>
			<productCardKey><![CDATA[]]></productCardKey>
			<isWxShop><![CDATA[]]></isWxShop>
			<brandIconUrl><![CDATA[]]></brandIconUrl>
			<showBoxItemStringList />
		</finderLiveProductShare>
		<finderOrder>
			<appID><![CDATA[]]></appID>
			<orderID><![CDATA[]]></orderID>
			<path><![CDATA[]]></path>
			<priceWording><![CDATA[]]></priceWording>
			<stateWording><![CDATA[]]></stateWording>
			<productImageURL><![CDATA[]]></productImageURL>
			<products><![CDATA[]]></products>
			<productsCount><![CDATA[0]]></productsCount>
			<orderType><![CDATA[0]]></orderType>
			<newPriceWording><![CDATA[]]></newPriceWording>
			<newStateWording><![CDATA[]]></newStateWording>
			<useNewWording><![CDATA[0]]></useNewWording>
		</finderOrder>
		<finderShopWindowShare>
			<finderUsername><![CDATA[]]></finderUsername>
			<avatar><![CDATA[]]></avatar>
			<nickname><![CDATA[]]></nickname>
			<commodityInStockCount><![CDATA[]]></commodityInStockCount>
			<appId><![CDATA[]]></appId>
			<path><![CDATA[]]></path>
			<appUsername><![CDATA[]]></appUsername>
			<query><![CDATA[]]></query>
			<liteAppId><![CDATA[]]></liteAppId>
			<liteAppPath><![CDATA[]]></liteAppPath>
			<liteAppQuery><![CDATA[]]></liteAppQuery>
			<platformTagURL><![CDATA[]]></platformTagURL>
			<saleWording><![CDATA[]]></saleWording>
			<lastGMsgID><![CDATA[]]></lastGMsgID>
			<profileTypeWording><![CDATA[]]></profileTypeWording>
			<saleWordingExtra><![CDATA[]]></saleWordingExtra>
			<isWxShop><![CDATA[]]></isWxShop>
			<platformIconUrl><![CDATA[]]></platformIconUrl>
			<brandIconUrl><![CDATA[]]></brandIconUrl>
			<description><![CDATA[]]></description>
			<backgroundUrl><![CDATA[]]></backgroundUrl>
			<darkModePlatformIconUrl><![CDATA[]]></darkModePlatformIconUrl>
			<reputationInfo>
				<hasReputationInfo>0</hasReputationInfo>
				<reputationScore>0</reputationScore>
				<reputationWording />
				<reputationTextColor />
				<reputationLevelWording />
				<reputationBackgroundColor />
			</reputationInfo>
			<productImageURLList />
		</finderShopWindowShare>
		<findernamecard>
			<username />
			<avatar><![CDATA[]]></avatar>
			<nickname />
			<auth_job />
			<auth_icon>0</auth_icon>
			<auth_icon_url />
			<ecSource><![CDATA[]]></ecSource>
			<lastGMsgID><![CDATA[]]></lastGMsgID>
		</findernamecard>
		<finderGuarantee>
			<scene><![CDATA[0]]></scene>
		</finderGuarantee>
		<directshare>0</directshare>
		<gamecenter>
			<namecard>
				<iconUrl />
				<name />
				<desc />
				<tail />
				<jumpUrl />
			</namecard>
		</gamecenter>
		<patMsg>
			<chatUser />
			<records>
				<recordNum>0</recordNum>
			</records>
		</patMsg>
		<secretmsg>
			<issecretmsg>0</issecretmsg>
		</secretmsg>
		<referfromscene>0</referfromscene>
		<gameshare>
			<liteappext>
				<liteappbizdata />
				<priority>0</priority>
			</liteappext>
			<appbrandext>
				<litegameinfo />
				<priority>-1</priority>
			</appbrandext>
			<gameshareid />
			<sharedata />
			<isvideo>0</isvideo>
			<duration>-1</duration>
			<isexposed>0</isexposed>
			<readtext />
		</gameshare>
		<mpsharetrace>
			<hasfinderelement>0</hasfinderelement>
			<lastgmsgid />
		</mpsharetrace>
		<wxgamecard>
			<framesetname />
			<mbcarddata />
			<minpkgversion />
			<clientextinfo />
			<mbcardheight>0</mbcardheight>
			<isoldversion>0</isoldversion>
		</wxgamecard>
		<liteapp>
			<id>null</id>
			<path />
			<query />
			<istransparent>0</istransparent>
			<hideicon>0</hideicon>
		</liteapp>
		<finderCollection>
			<feedCount>0</feedCount>
			<collectionTopicType>0</collectionTopicType>
			<paidCollectionType>0</paidCollectionType>
			<price>0</price>
			<title />
			<collectionId>0</collectionId>
			<thumbUrl />
			<collectionDesc />
			<authorUsername />
			<nickname />
			<avatarURL />
			<authIconURL />
			<authIconType>0</authIconType>
		</finderCollection>
	</appmsg>
	<fromusername>wxid_jrpmphrrct5n21</fromusername>
	<scene>0</scene>
	<appinfo>
		<version>1</version>
		<appname></appname>
	</appinfo>
	<commenturl></commenturl>
</msg>

C:/Users/CSY/Documents/WeChat Files/wxid_pvebx6dozp3r19/FileStorage/Cache/2025-03/722c1d9b86546a9a9076ed8ca393b742_t.jpg
C:/Users/CSY/Documents/WeChat Files/wxid_pvebx6dozp3r19/FileStorage/Cache/2025-03/722c1d9b86546a9a9076ed8ca393b742.jpg

** 引用 49**
```xml
wxid_jrpmphrrct5n21[wxid_jrpmphrrct5n21]|2155189721313623950|2025-03-28 00:58:26|49|5bebc7076624d1ada72d1c8820af1788
<msgsource>    <alnode>        <fr>4</fr>    </alnode>    <eggIncluded>1</eggIncluded>    <sec_msg_node>        <uuid>480fb2f01706cedbc37c5ca7c64be8a6_</uuid>        <risk-file-flag />        <risk-file-md5-list />        <alnode>            <fr>1</fr>        </alnode>    </sec_msg_node>    <signature>N0_V1_HrKpKgfN|v1_9PbCZzxV</signature>    <tmp_node>        <publisher-id />    </tmp_node></msgsource>
<?xml version="1.0"?>
<msg>
	<appmsg appid="" sdkver="0">
		<title>你在说什么</title>
		<des />
		<username />
		<action>view</action>
		<type>57</type>
		<showtype>0</showtype>
		<content />
		<url />
		<lowurl />
		<forwardflag>0</forwardflag>
		<dataurl />
		<lowdataurl />
		<contentattr>0</contentattr>
		<streamvideo>
			<streamvideourl />
			<streamvideototaltime>0</streamvideototaltime>
			<streamvideotitle />
			<streamvideowording />
			<streamvideoweburl />
			<streamvideothumburl />
			<streamvideoaduxinfo />
			<streamvideopublishid />
		</streamvideo>
		<canvasPageItem>
			<canvasPageXml><![CDATA[]]></canvasPageXml>
		</canvasPageItem>
		<refermsg>
			<type>1</type>
			<svrid>2632787944628480497</svrid>
			<fromusr>wxid_pvebx6dozp3r19</fromusr>
			<chatusr>wxid_pvebx6dozp3r19</chatusr>
			<displayname>再会，谢谢所有的鱼</displayname>
			<msgsource>&lt;msgsource&gt;
	&lt;sec_msg_node&gt;
		&lt;alnode&gt;
			&lt;fr&gt;1&lt;/fr&gt;
		&lt;/alnode&gt;
	&lt;/sec_msg_node&gt;
	&lt;pua&gt;1&lt;/pua&gt;
	&lt;signature&gt;N0_V1_gv0N5G+P|v1_FbY6S0Hn&lt;/signature&gt;
	&lt;tmp_node&gt;
		&lt;publisher-id&gt;&lt;/publisher-id&gt;
	&lt;/tmp_node&gt;
&lt;/msgsource&gt;
</msgsource>
			<content>访问你提供的链接时出问题啦，可能是链接拼写有误。你可以确认下链接是否正确，或者跟我说说你想通过这个链接了解什么内容，我来帮你查询。 
conversation_id: 7486533878581100595</content>
			<strid />
			<createtime>1743094510</createtime>
		</refermsg>
		<appattach>
			<totallen>0</totallen>
			<attachid />
			<cdnattachurl />
			<emoticonmd5 />
			<aeskey />
			<fileext />
			<islargefilemsg>0</islargefilemsg>
		</appattach>
		<extinfo />
		<androidsource>0</androidsource>
		<thumburl />
		<mediatagname />
		<messageaction><![CDATA[]]></messageaction>
		<messageext><![CDATA[]]></messageext>
		<emoticongift>
			<packageflag>0</packageflag>
			<packageid />
		</emoticongift>
		<emoticonshared>
			<packageflag>0</packageflag>
			<packageid />
		</emoticonshared>
		<designershared>
			<designeruin>0</designeruin>
			<designername>null</designername>
			<designerrediretcturl><![CDATA[null]]></designerrediretcturl>
		</designershared>
		<emotionpageshared>
			<tid>0</tid>
			<title>null</title>
			<desc>null</desc>
			<iconUrl><![CDATA[null]]></iconUrl>
			<secondUrl>null</secondUrl>
			<pageType>0</pageType>
			<setKey>null</setKey>
		</emotionpageshared>
		<webviewshared>
			<shareUrlOriginal />
			<shareUrlOpen />
			<jsAppId />
			<publisherId />
			<publisherReqId />
		</webviewshared>
		<template_id />
		<md5 />
		<websearch>
			<rec_category>0</rec_category>
			<channelId>0</channelId>
		</websearch>
		<weappinfo>
			<username />
			<appid />
			<appservicetype>0</appservicetype>
			<secflagforsinglepagemode>0</secflagforsinglepagemode>
			<videopageinfo>
				<thumbwidth>0</thumbwidth>
				<thumbheight>0</thumbheight>
				<fromopensdk>0</fromopensdk>
			</videopageinfo>
		</weappinfo>
		<statextstr />
		<musicShareItem>
			<musicDuration>0</musicDuration>
		</musicShareItem>
		<finderLiveProductShare>
			<finderLiveID><![CDATA[]]></finderLiveID>
			<finderUsername><![CDATA[]]></finderUsername>
			<finderObjectID><![CDATA[]]></finderObjectID>
			<finderNonceID><![CDATA[]]></finderNonceID>
			<liveStatus><![CDATA[]]></liveStatus>
			<appId><![CDATA[]]></appId>
			<pagePath><![CDATA[]]></pagePath>
			<productId><![CDATA[]]></productId>
			<coverUrl><![CDATA[]]></coverUrl>
			<productTitle><![CDATA[]]></productTitle>
			<marketPrice><![CDATA[0]]></marketPrice>
			<sellingPrice><![CDATA[0]]></sellingPrice>
			<platformHeadImg><![CDATA[]]></platformHeadImg>
			<platformName><![CDATA[]]></platformName>
			<shopWindowId><![CDATA[]]></shopWindowId>
			<flashSalePrice><![CDATA[0]]></flashSalePrice>
			<flashSaleEndTime><![CDATA[0]]></flashSaleEndTime>
			<ecSource><![CDATA[]]></ecSource>
			<sellingPriceWording><![CDATA[]]></sellingPriceWording>
			<platformIconURL><![CDATA[]]></platformIconURL>
			<firstProductTagURL><![CDATA[]]></firstProductTagURL>
			<firstProductTagAspectRatioString><![CDATA[0.0]]></firstProductTagAspectRatioString>
			<secondProductTagURL><![CDATA[]]></secondProductTagURL>
			<secondProductTagAspectRatioString><![CDATA[0.0]]></secondProductTagAspectRatioString>
			<firstGuaranteeWording><![CDATA[]]></firstGuaranteeWording>
			<secondGuaranteeWording><![CDATA[]]></secondGuaranteeWording>
			<thirdGuaranteeWording><![CDATA[]]></thirdGuaranteeWording>
			<isPriceBeginShow>false</isPriceBeginShow>
			<lastGMsgID><![CDATA[]]></lastGMsgID>
			<promoterKey><![CDATA[]]></promoterKey>
			<discountWording><![CDATA[]]></discountWording>
			<priceSuffixDescription><![CDATA[]]></priceSuffixDescription>
			<productCardKey><![CDATA[]]></productCardKey>
			<isWxShop><![CDATA[]]></isWxShop>
			<brandIconUrl><![CDATA[]]></brandIconUrl>
			<showBoxItemStringList />
		</finderLiveProductShare>
		<finderOrder>
			<appID><![CDATA[]]></appID>
			<orderID><![CDATA[]]></orderID>
			<path><![CDATA[]]></path>
			<priceWording><![CDATA[]]></priceWording>
			<stateWording><![CDATA[]]></stateWording>
			<productImageURL><![CDATA[]]></productImageURL>
			<products><![CDATA[]]></products>
			<productsCount><![CDATA[0]]></productsCount>
			<orderType><![CDATA[0]]></orderType>
			<newPriceWording><![CDATA[]]></newPriceWording>
			<newStateWording><![CDATA[]]></newStateWording>
			<useNewWording><![CDATA[0]]></useNewWording>
		</finderOrder>
		<finderShopWindowShare>
			<finderUsername><![CDATA[]]></finderUsername>
			<avatar><![CDATA[]]></avatar>
			<nickname><![CDATA[]]></nickname>
			<commodityInStockCount><![CDATA[]]></commodityInStockCount>
			<appId><![CDATA[]]></appId>
			<path><![CDATA[]]></path>
			<appUsername><![CDATA[]]></appUsername>
			<query><![CDATA[]]></query>
			<liteAppId><![CDATA[]]></liteAppId>
			<liteAppPath><![CDATA[]]></liteAppPath>
			<liteAppQuery><![CDATA[]]></liteAppQuery>
			<platformTagURL><![CDATA[]]></platformTagURL>
			<saleWording><![CDATA[]]></saleWording>
			<lastGMsgID><![CDATA[]]></lastGMsgID>
			<profileTypeWording><![CDATA[]]></profileTypeWording>
			<saleWordingExtra><![CDATA[]]></saleWordingExtra>
			<isWxShop><![CDATA[]]></isWxShop>
			<platformIconUrl><![CDATA[]]></platformIconUrl>
			<brandIconUrl><![CDATA[]]></brandIconUrl>
			<description><![CDATA[]]></description>
			<backgroundUrl><![CDATA[]]></backgroundUrl>
			<darkModePlatformIconUrl><![CDATA[]]></darkModePlatformIconUrl>
			<reputationInfo>
				<hasReputationInfo>0</hasReputationInfo>
				<reputationScore>0</reputationScore>
				<reputationWording />
				<reputationTextColor />
				<reputationLevelWording />
				<reputationBackgroundColor />
			</reputationInfo>
			<productImageURLList />
		</finderShopWindowShare>
		<findernamecard>
			<username />
			<avatar><![CDATA[]]></avatar>
			<nickname />
			<auth_job />
			<auth_icon>0</auth_icon>
			<auth_icon_url />
			<ecSource><![CDATA[]]></ecSource>
			<lastGMsgID><![CDATA[]]></lastGMsgID>
		</findernamecard>
		<finderGuarantee>
			<scene><![CDATA[0]]></scene>
		</finderGuarantee>
		<directshare>0</directshare>
		<gamecenter>
			<namecard>
				<iconUrl />
				<name />
				<desc />
				<tail />
				<jumpUrl />
			</namecard>
		</gamecenter>
		<patMsg>
			<chatUser />
			<records>
				<recordNum>0</recordNum>
			</records>
		</patMsg>
		<secretmsg>
			<issecretmsg>0</issecretmsg>
		</secretmsg>
		<referfromscene>0</referfromscene>
		<gameshare>
			<liteappext>
				<liteappbizdata />
				<priority>0</priority>
			</liteappext>
			<appbrandext>
				<litegameinfo />
				<priority>-1</priority>
			</appbrandext>
			<gameshareid />
			<sharedata />
			<isvideo>0</isvideo>
			<duration>-1</duration>
			<isexposed>0</isexposed>
			<readtext />
		</gameshare>
		<mpsharetrace>
			<hasfinderelement>0</hasfinderelement>
			<lastgmsgid />
		</mpsharetrace>
		<wxgamecard>
			<framesetname />
			<mbcarddata />
			<minpkgversion />
			<clientextinfo />
			<mbcardheight>0</mbcardheight>
			<isoldversion>0</isoldversion>
		</wxgamecard>
		<liteapp>
			<id>null</id>
			<path />
			<query />
			<istransparent>0</istransparent>
			<hideicon>0</hideicon>
		</liteapp>
		<finderCollection>
			<feedCount>0</feedCount>
			<collectionTopicType>0</collectionTopicType>
			<paidCollectionType>0</paidCollectionType>
			<price>0</price>
			<title />
			<collectionId>0</collectionId>
			<thumbUrl />
			<collectionDesc />
			<authorUsername />
			<nickname />
			<avatarURL />
			<authIconURL />
			<authIconType>0</authIconType>
		</finderCollection>
	</appmsg>
	<fromusername>wxid_jrpmphrrct5n21</fromusername>
	<scene>0</scene>
	<appinfo>
		<version>1</version>
		<appname></appname>
	</appinfo>
	<commenturl></commenturl>
</msg>

C:/Users/CSY/Documents/WeChat Files/wxid_pvebx6dozp3r19/FileStorage/Cache/2025-03/27d6e53ec00ac4b7376f68658dd5981f
```
引用图片
```xml
wxid_jrpmphrrct5n21[wxid_jrpmphrrct5n21]|1396441906898940262|2025-03-28 01:01:09|49|9ef6b86e95d3ab16751b2037c20bcec6
<msgsource>    <alnode>        <fr>4</fr>    </alnode>    <eggIncluded>1</eggIncluded>    <sec_msg_node>        <uuid>354cf962bac94e820fb6a45ae399cc8e_</uuid>        <risk-file-flag />        <risk-file-md5-list />        <alnode>            <fr>1</fr>        </alnode>    </sec_msg_node>    <signature>N0_V1_O1ENlqKC|v1_9zHA+3Qx</signature>    <tmp_node>        <publisher-id />    </tmp_node></msgsource>
<?xml version="1.0"?>
<msg>
	<appmsg appid="" sdkver="0">
		<title>还看还看</title>
		<des />
		<username />
		<action>view</action>
		<type>57</type>
		<showtype>0</showtype>
		<content />
		<url />
		<lowurl />
		<forwardflag>0</forwardflag>
		<dataurl />
		<lowdataurl />
		<contentattr>0</contentattr>
		<streamvideo>
			<streamvideourl />
			<streamvideototaltime>0</streamvideototaltime>
			<streamvideotitle />
			<streamvideowording />
			<streamvideoweburl />
			<streamvideothumburl />
			<streamvideoaduxinfo />
			<streamvideopublishid />
		</streamvideo>
		<canvasPageItem>
			<canvasPageXml><![CDATA[]]></canvasPageXml>
		</canvasPageItem>
		<refermsg>
			<type>3</type>
			<svrid>6602511768485105124</svrid>
			<fromusr>wxid_pvebx6dozp3r19</fromusr>
			<chatusr>wxid_jrpmphrrct5n21</chatusr>
			<displayname>Deku</displayname>
			<msgsource>&lt;msgsource&gt;&lt;sec_msg_node&gt;&lt;uuid&gt;354cf962bac94e820fb6a45ae399cc8e_&lt;/uuid&gt;&lt;/sec_msg_node&gt;&lt;/msgsource&gt;</msgsource>
			<content>&lt;msg&gt;&lt;img aeskey="eff5b5743867193d5082ef24437120c9" encryver="1" cdnthumbaeskey="eff5b5743867193d5082ef24437120c9" cdnthumburl="3057020100044b30490201000204d48e135e02032f5aa90204a5996971020467e51869042437393062653961642d383462612d343139372d383236642d633137626636633330346465020405150a020201000405004c55cd00" cdnthumblength="6231" cdnthumbheight="576" cdnthumbwidth="300" cdnmidimgurl="3057020100044b30490201000204d48e135e02032f5aa90204a5996971020467e51869042437393062653961642d383462612d343139372d383236642d633137626636633330346465020405150a020201000405004c55cd00" length="737482" md5="b0199f922d038be12efccf8f41a7afc9" hevc_mid_size="107114" originsourcemd5="7f5f1d08f201c12ca1b4f10888363651"&gt;&lt;secHashInfoBase64&gt;eyJwaGFzaCI6IjEwMTA1MDEwYjA1MDkwMDAiLCJwZHFIYXNoIjoiNTU5YWQ1MGU4ZDI1ODY3Y2Q3&amp;#x0A;NWFjMzA5OGY4Nzk3MTYzYjRiY2Q0OTk3NDZhZjViNmExMTg1ODRhYmM2OGQ1MyJ9&amp;#x0A;&lt;/secHashInfoBase64&gt;&lt;/img&gt;&lt;/msg&gt;</content>
			<strid />
			<createtime>1743093729</createtime>
		</refermsg>
		<appattach>
			<totallen>0</totallen>
			<attachid />
			<cdnattachurl />
			<emoticonmd5 />
			<aeskey />
			<fileext />
			<islargefilemsg>0</islargefilemsg>
		</appattach>
		<extinfo />
		<androidsource>0</androidsource>
		<thumburl />
		<mediatagname />
		<messageaction><![CDATA[]]></messageaction>
		<messageext><![CDATA[]]></messageext>
		<emoticongift>
			<packageflag>0</packageflag>
			<packageid />
		</emoticongift>
		<emoticonshared>
			<packageflag>0</packageflag>
			<packageid />
		</emoticonshared>
		<designershared>
			<designeruin>0</designeruin>
			<designername>null</designername>
			<designerrediretcturl><![CDATA[null]]></designerrediretcturl>
		</designershared>
		<emotionpageshared>
			<tid>0</tid>
			<title>null</title>
			<desc>null</desc>
			<iconUrl><![CDATA[null]]></iconUrl>
			<secondUrl>null</secondUrl>
			<pageType>0</pageType>
			<setKey>null</setKey>
		</emotionpageshared>
		<webviewshared>
			<shareUrlOriginal />
			<shareUrlOpen />
			<jsAppId />
			<publisherId />
			<publisherReqId />
		</webviewshared>
		<template_id />
		<md5 />
		<websearch>
			<rec_category>0</rec_category>
			<channelId>0</channelId>
		</websearch>
		<weappinfo>
			<username />
			<appid />
			<appservicetype>0</appservicetype>
			<secflagforsinglepagemode>0</secflagforsinglepagemode>
			<videopageinfo>
				<thumbwidth>0</thumbwidth>
				<thumbheight>0</thumbheight>
				<fromopensdk>0</fromopensdk>
			</videopageinfo>
		</weappinfo>
		<statextstr />
		<musicShareItem>
			<musicDuration>0</musicDuration>
		</musicShareItem>
		<finderLiveProductShare>
			<finderLiveID><![CDATA[]]></finderLiveID>
			<finderUsername><![CDATA[]]></finderUsername>
			<finderObjectID><![CDATA[]]></finderObjectID>
			<finderNonceID><![CDATA[]]></finderNonceID>
			<liveStatus><![CDATA[]]></liveStatus>
			<appId><![CDATA[]]></appId>
			<pagePath><![CDATA[]]></pagePath>
			<productId><![CDATA[]]></productId>
			<coverUrl><![CDATA[]]></coverUrl>
			<productTitle><![CDATA[]]></productTitle>
			<marketPrice><![CDATA[0]]></marketPrice>
			<sellingPrice><![CDATA[0]]></sellingPrice>
			<platformHeadImg><![CDATA[]]></platformHeadImg>
			<platformName><![CDATA[]]></platformName>
			<shopWindowId><![CDATA[]]></shopWindowId>
			<flashSalePrice><![CDATA[0]]></flashSalePrice>
			<flashSaleEndTime><![CDATA[0]]></flashSaleEndTime>
			<ecSource><![CDATA[]]></ecSource>
			<sellingPriceWording><![CDATA[]]></sellingPriceWording>
			<platformIconURL><![CDATA[]]></platformIconURL>
			<firstProductTagURL><![CDATA[]]></firstProductTagURL>
			<firstProductTagAspectRatioString><![CDATA[0.0]]></firstProductTagAspectRatioString>
			<secondProductTagURL><![CDATA[]]></secondProductTagURL>
			<secondProductTagAspectRatioString><![CDATA[0.0]]></secondProductTagAspectRatioString>
			<firstGuaranteeWording><![CDATA[]]></firstGuaranteeWording>
			<secondGuaranteeWording><![CDATA[]]></secondGuaranteeWording>
			<thirdGuaranteeWording><![CDATA[]]></thirdGuaranteeWording>
			<isPriceBeginShow>false</isPriceBeginShow>
			<lastGMsgID><![CDATA[]]></lastGMsgID>
			<promoterKey><![CDATA[]]></promoterKey>
			<discountWording><![CDATA[]]></discountWording>
			<priceSuffixDescription><![CDATA[]]></priceSuffixDescription>
			<productCardKey><![CDATA[]]></productCardKey>
			<isWxShop><![CDATA[]]></isWxShop>
			<brandIconUrl><![CDATA[]]></brandIconUrl>
			<showBoxItemStringList />
		</finderLiveProductShare>
		<finderOrder>
			<appID><![CDATA[]]></appID>
			<orderID><![CDATA[]]></orderID>
			<path><![CDATA[]]></path>
			<priceWording><![CDATA[]]></priceWording>
			<stateWording><![CDATA[]]></stateWording>
			<productImageURL><![CDATA[]]></productImageURL>
			<products><![CDATA[]]></products>
			<productsCount><![CDATA[0]]></productsCount>
			<orderType><![CDATA[0]]></orderType>
			<newPriceWording><![CDATA[]]></newPriceWording>
			<newStateWording><![CDATA[]]></newStateWording>
			<useNewWording><![CDATA[0]]></useNewWording>
		</finderOrder>
		<finderShopWindowShare>
			<finderUsername><![CDATA[]]></finderUsername>
			<avatar><![CDATA[]]></avatar>
			<nickname><![CDATA[]]></nickname>
			<commodityInStockCount><![CDATA[]]></commodityInStockCount>
			<appId><![CDATA[]]></appId>
			<path><![CDATA[]]></path>
			<appUsername><![CDATA[]]></appUsername>
			<query><![CDATA[]]></query>
			<liteAppId><![CDATA[]]></liteAppId>
			<liteAppPath><![CDATA[]]></liteAppPath>
			<liteAppQuery><![CDATA[]]></liteAppQuery>
			<platformTagURL><![CDATA[]]></platformTagURL>
			<saleWording><![CDATA[]]></saleWording>
			<lastGMsgID><![CDATA[]]></lastGMsgID>
			<profileTypeWording><![CDATA[]]></profileTypeWording>
			<saleWordingExtra><![CDATA[]]></saleWordingExtra>
			<isWxShop><![CDATA[]]></isWxShop>
			<platformIconUrl><![CDATA[]]></platformIconUrl>
			<brandIconUrl><![CDATA[]]></brandIconUrl>
			<description><![CDATA[]]></description>
			<backgroundUrl><![CDATA[]]></backgroundUrl>
			<darkModePlatformIconUrl><![CDATA[]]></darkModePlatformIconUrl>
			<reputationInfo>
				<hasReputationInfo>0</hasReputationInfo>
				<reputationScore>0</reputationScore>
				<reputationWording />
				<reputationTextColor />
				<reputationLevelWording />
				<reputationBackgroundColor />
			</reputationInfo>
			<productImageURLList />
		</finderShopWindowShare>
		<findernamecard>
			<username />
			<avatar><![CDATA[]]></avatar>
			<nickname />
			<auth_job />
			<auth_icon>0</auth_icon>
			<auth_icon_url />
			<ecSource><![CDATA[]]></ecSource>
			<lastGMsgID><![CDATA[]]></lastGMsgID>
		</findernamecard>
		<finderGuarantee>
			<scene><![CDATA[0]]></scene>
		</finderGuarantee>
		<directshare>0</directshare>
		<gamecenter>
			<namecard>
				<iconUrl />
				<name />
				<desc />
				<tail />
				<jumpUrl />
			</namecard>
		</gamecenter>
		<patMsg>
			<chatUser />
			<records>
				<recordNum>0</recordNum>
			</records>
		</patMsg>
		<secretmsg>
			<issecretmsg>0</issecretmsg>
		</secretmsg>
		<referfromscene>0</referfromscene>
		<gameshare>
			<liteappext>
				<liteappbizdata />
				<priority>0</priority>
			</liteappext>
			<appbrandext>
				<litegameinfo />
				<priority>-1</priority>
			</appbrandext>
			<gameshareid />
			<sharedata />
			<isvideo>0</isvideo>
			<duration>-1</duration>
			<isexposed>0</isexposed>
			<readtext />
		</gameshare>
		<mpsharetrace>
			<hasfinderelement>0</hasfinderelement>
			<lastgmsgid />
		</mpsharetrace>
		<wxgamecard>
			<framesetname />
			<mbcarddata />
			<minpkgversion />
			<clientextinfo />
			<mbcardheight>0</mbcardheight>
			<isoldversion>0</isoldversion>
		</wxgamecard>
		<liteapp>
			<id>null</id>
			<path />
			<query />
			<istransparent>0</istransparent>
			<hideicon>0</hideicon>
		</liteapp>
		<finderCollection>
			<feedCount>0</feedCount>
			<collectionTopicType>0</collectionTopicType>
			<paidCollectionType>0</paidCollectionType>
			<price>0</price>
			<title />
			<collectionId>0</collectionId>
			<thumbUrl />
			<collectionDesc />
			<authorUsername />
			<nickname />
			<avatarURL />
			<authIconURL />
			<authIconType>0</authIconType>
		</finderCollection>
	</appmsg>
	<fromusername>wxid_jrpmphrrct5n21</fromusername>
	<scene>0</scene>
	<appinfo>
		<version>1</version>
		<appname></appname>
	</appinfo>
	<commenturl></commenturl>
</msg>

C:/Users/CSY/Documents/WeChat Files/wxid_pvebx6dozp3r19/FileStorage/Cache/2025-03/959f9958deed0b6ff1137d5198cffac9
```
**文件 49**
wxid_jrpmphrrct5n21[wxid_jrpmphrrct5n21]|4437991385565688661|2025-03-28 01:10:16|49|0e855ac764bfacee7d09027bed4f485e
<msgsource>    <signature>N0_V1_4pBdG0YD|v1_kU0iWzf8</signature>    <tmp_node>        <publisher-id />    </tmp_node>    <sec_msg_node>        <alnode>            <fr>1</fr>        </alnode>    </sec_msg_node></msgsource>
<msg>
    <fromusername>wxid_jrpmphrrct5n21</fromusername>
    <scene>0</scene>
    <commenturl></commenturl>
    <appmsg appid="" sdkver="0">
        <title>SANS_2024_SOC_Survey_Facing_Top_Challenges_Security_Operations_v3.pdf</title>
        <des></des>
        <action>view</action>
        <type>6</type>
        <showtype>0</showtype>
        <content></content>
        <url></url>
        <dataurl></dataurl>
        <lowurl></lowurl>
        <lowdataurl></lowdataurl>
        <recorditem></recorditem>
        <thumburl></thumburl>
        <messageaction></messageaction>
        <laninfo>http://192.168.71.42:9114/lan_wxid_pvebx6dozp3r19_1827161319_10059058_1743095416159;06c8f1c454920a5862fbec68e9b88823</laninfo>
        <md5>b47680500189000ab0082e05725c64a1</md5>
        <extinfo></extinfo>
        <sourceusername></sourceusername>
        <sourcedisplayname></sourcedisplayname>
        <commenturl></commenturl>
        <appattach>
            <totallen>3925265</totallen>
            <attachid></attachid>
            <emoticonmd5></emoticonmd5>
            <fileext>pdf</fileext>
            <fileuploadtoken>v1_Tmt7tVyz297sRlfzU38hJCjWNBKhD/sj4txmPByTJgAXuJoWdXpeTwgUPn8xmvyQLZcVpXxX/WBN+Wadfuiks6lvhRNiebJIOt2G40AJ/CCdJIyhPz2UIci4hqNbRM86Pe291tJj1+A/Zoc46NVNiEIl20/O+NXp5FTl15wIk3dmLz2LbcunHvcWCcZAZo3MoRCZJ5nAJcYRcG2M9c6JLYME27o/HJpNZiRB/NxOD2xAjUhLszTe9Bw+cZPTRpAY0PlS6ylw/H7vWfW3</fileuploadtoken>
            <aeskey></aeskey>
        </appattach>
        <webviewshared>
            <publisherId></publisherId>
            <publisherReqId>0</publisherReqId>
        </webviewshared>
        <weappinfo>
            <pagepath></pagepath>
            <username></username>
            <appid></appid>
            <appservicetype>0</appservicetype>
        </weappinfo>
        <websearch />
    </appmsg>
    <appinfo>
        <version>1</version>
        <appname>Window wechat</appname>
    </appinfo>
</msg>

C:/Users/CSY/Documents/WeChat Files/wxid_pvebx6dozp3r19/FileStorage/File/2025-03/SANS_2024_SOC_Survey_Facing_Top_Challenges_Security_Operations_v3.pdf
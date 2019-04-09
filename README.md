# NaxcaServer

Just a travel provider simulator. Just for fun.
![Image of simulator](https://lh5.googleusercontent.com/-OiR2Zahgryc/TWtD_hbzbWI/AAAAAAAABeY/S4F8ZLelA2w/s1600/diy_flight_simulator.jpg)
 
## HotelsDate: 2030-01-29

Provider|Returns|When request is|Url|File
|---|---|---|---|---|
|RTS|1DayStay 1Room 1Adt|Date:2030-01-01|http://matabares.com:8000/rtssimulation/WebServiceProjects/NetWebService/WsHotelProducts.asmx
|RTS|HotelInfoEn|HotelCode:BKK0001 Language:EN|
|RTS|HotelInfoPt|HotelCode:BKK0001 Language:BR|
|RTS|HotelInfoHotelCodeIsMissing|HotelCode:null Language:AR|
|RTS|HotelInfoError|HotelCode:NOHOTELCODE Language:AR|
|RTS|Remark Hotel Information|HotelCode:BKK0001  RoomTypeCode:TH&#124;001:AVAU:19491:M50496:219274:215398&#124;PREMIER ROOM&#124;SB*1#&#124;BKK&#124;&#124;ZDG.CQ&#124;USD&#124;JHPRZGK&#124;~None|http://matabares.com:8000/rtssimulation/WebServiceProjects/NetWebService/WsHotelProducts.asmx
|RTS|Cancel policies on penalty (non refundable)|HotelCode:BKK0001 RoomTypeCode:TH&#124;001:AVAU:19491:M50496:219274:215398&#124;PREMIER ROOM&#124;SB*1#&#124;BKK&#124;&#124;ZDG.CQ&#124;USD&#124;JHPRZGK&#124;~None|
|RTS|Cancel policies on penalty (non refundable)|HotelCode:BKK0001 RoomTypeCode:TH&#124;001:AVAU:19491:M50496:219274:215398&#124;PREMIER ROOM&#124;SB*1#&#124;BKK&#124;&#124;ZDG.CQ&#124;USD&#124;JHPRZGK&#124;~None|
|RTS|HotelInfo without amenities DT02|HotelCode:BKK0003 Language:{AR&#124;EN&#124;BR}||
|OLYMPIA-ABREU|Retorna hoteles con diferentes casos de MinPrice y Total amount. **Hotel 1453:** Amount="107.58" MinPrice="117.25" **Hotel 1454:** Amount="107.58" Commission="0.00" MinPrice="0" **Hotel 1455:** Amount="507.58"|Date: 2030-01-29 1Room 1Adult|-|providersimulation/olympia/search_1r1a_minprice.xml|
|OLYMPIA|Retorna static data de hotel en inglés|HotelCode="1" LangRequested="EN"||providersimulation/olympia/hotelinfo_en_ok.xml|
|TOURICO|5 hotels 1 month future|<Destination xmlns="http://schemas.tourico.com/webservices/hotelv3">MIA</Destination>|---|providersimulation/tourico/flow1r1a_searchresponse.xml|
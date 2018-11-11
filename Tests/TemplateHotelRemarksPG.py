from bs4 import BeautifulSoup


body = '<?xml version="1.0"?> <soap:Envelope xmlns:rts="http://www.rts.co.kr/" xmlns:soap="http://www.w3.org/2003/05/soap-envelope"> <soap:Header> <BaseInfo> <SiteCode>htest-00</SiteCode> <Password>0000</Password> <RequestType>NetPartner</RequestType> </BaseInfo> </soap:Header> <soap:Body> <GetRemarkHotelInformationForCustomerCount> <HotelSearchListNetGuestCount> <LanguageCode>EN</LanguageCode> <TravelerNationality>AE</TravelerNationality> <CityCode>HKG</CityCode> <CheckInDate>2016-06-05</CheckInDate> <CheckOutDate>2016-06-06</CheckOutDate> <StarRating>0</StarRating> <LocationCode/> <SupplierCompCode/> <AvailableHotelOnly>true</AvailableHotelOnly> <RecommendHotelOnly>false</RecommendHotelOnly> <ClientCurrencyCode>USD</ClientCurrencyCode> <ItemName/> <SellerMarkup>*1</SellerMarkup> <CompareYn>false</CompareYn> <SortType/> <ItemCodeList> <ItemCodeInfo> <ItemCode>HKG0001</ItemCode> <ItemNo>5</ItemNo> </ItemCodeInfo> </ItemCodeList> <GuestList> <GuestsInfo> <AdultCount>1</AdultCount> <ChildCount>1</ChildCount> <RoomCount>1</RoomCount> <ChildAge1>1</ChildAge1> <ChildAge2>0</ChildAge2> </GuestsInfo> </GuestList> </HotelSearchListNetGuestCount> <RoomTypeCode>24lHpDD94AafaeiucpXv3A7W|BAR|318^NOR|HKG|RO|ST|1*1*3QYlRbnQ+vgQxDDMUYhPDQ ==*RO-CN1*DBT-CN1|DOUBLE OR TWIN STANDARD|NA.NTQ</RoomTypeCode> </GetRemarkHotelInformationForCustomerCount> </soap:Body> </soap:Envelope>'
file = open("../providersimulation/rts/RemarkHotelInformationRemarks.xml","r", encoding='utf8')
data = file.read()
file.close()
parsedXml = BeautifulSoup(body, 'xml')
#print(parsedXml.find("Body").find("GetRemarkHotelInformationForCustomerCount").find("HotelSearchListNetGuestCount. ItemCodeList.ItemCodeInfo.ItemCode ItemNo"))
itemCode = parsedXml.Body.GetRemarkHotelInformationForCustomerCount.HotelSearchListNetGuestCount.ItemCodeList.ItemCodeInfo.ItemCode.get_text()
itemNo = parsedXml.Body.GetRemarkHotelInformationForCustomerCount.HotelSearchListNetGuestCount.ItemCodeList.ItemCodeInfo.ItemNo.get_text()
roomTypeCode = parsedXml.Body.GetRemarkHotelInformationForCustomerCount.RoomTypeCode.get_text()
print(itemNo)
body = str.replace(body,"{ZZZZ}",itemCode)
class RtsSimulation:

    def RtsResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")
        if "GetHotelSearchListForCustomerCount" in body:

            if "<CheckInDate>2020-01-01</CheckInDate>" in body:
                file = open("providersimulation/rts/1DayStay1Room1Adt.xml", #busqueda 1 adulto 1 dia destino bangkok
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            elif "<CheckInDate>2020-01-02</CheckInDate>" in body:
                file = open("providersimulation/rts/HotelSearch_3DayStay1Room1Adt.xml", #busqueda 1 adulto 3 dias bangkok
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            elif "<CheckInDate>2020-01-03</CheckInDate>" in body:
                file = open("providersimulation/rts/HotelSearch_3DayStay1Room1Adt_2Room2Adt1Chd.xml", #busqueda 1 adulto un cuarto, 2 adultos un niño en segundo cuarto destino bangkok
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            elif "<CheckInDate>2020-01-04</CheckInDate>" in body:
                file = open("providersimulation/rts/HotelSearch_3DayStay1Room2Adt_2Room2Adt.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            elif "<CheckInDate>2020-01-05</CheckInDate>" in body:
                file = open("providersimulation/rts/HotelSearch_3DayStay1Room2Adt1Chd.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            elif "<CheckInDate>2020-01-06</CheckInDate>" in body:
                file = open("providersimulation/rts/HotelSearch_3DayStay1Room2Adt1Inf.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            elif "<CheckInDate>2020-01-07</CheckInDate>" in body:  #busqueda 1 adulto destino Bogota
                file = open("providersimulation/rts/HotelSearch_BO1_3DayStay1Room1Adt.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            elif "<CheckInDate>2020-01-07</CheckInDate>" in body:
                file = open("providersimulation/rts/singleHotelSearch1adtBKK0001.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            elif "<CheckInDate>2020-01-18</CheckInDate>" in body:
                file = open("providersimulation/rts/singleHotelSearch1adtBKK0001.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "GetCancelDeadlineForCustormerCountResponse":
            if "<CheckInDate>2020-01-02</CheckInDate>" in body:
                file = open("providersimulation/rts/1DayStay1Room1Adt.xml",  # busqueda 1 adulto 3 dia destino bangkok
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            elif "<CheckInDate>2020-01-02</CheckInDate>" in body:
                file = open("providersimulation/rts/1DayStay1Room1Adt.xml",  # busqueda 1 adulto 3 dia destino bangkok
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "GetHotelInformation" in body:
            if "<ItemCode>BKK0001</ItemCode>" in body and "<LanguageCode>AR</LanguageCode>" in body:
                file = open("providersimulation/rts/HotelInfoEs.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<ItemCode>BKK0001</ItemCode>" in body and "<LanguageCode>BR</LanguageCode>" in body:
                file = open("providersimulation/rts/HotelInfoBr.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<ItemCode>BKK0001</ItemCode>" in body and "<LanguageCode>EN</LanguageCode>" in body:
                file = open("providersimulation/rts/HotelInfoEn.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<ItemCode>BKK0002</ItemCode>" in body :
                if "<LanguageCode>EN</LanguageCode>" in body:
                    file = open("providersimulation/rts/HotelInfoBkk0002EN.xml",
                            "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

                elif "<LanguageCode>AR</LanguageCode>" in body:
                    file = open("providersimulation/rts/HotelInfoBkk0002AR.xml",
                            "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

                elif "<LanguageCode>BR</LanguageCode>" in body:
                    file = open("providersimulation/rts/HotelInfoBkk0002BR.xml",
                                "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

            if "<ItemCode>NOHOTELCODE</ItemCode>" in body :
                file = open("providersimulation/rts/HotelInfoError.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<ItemCode />" in body :
                file = open("providersimulation/rts/HotelInfoHotelCodeIsMissing.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
        if "GetCancelDeadlineForCustomerCount" in body:
            if "<ItemCode>BKK0001</ItemCode>" in body and "<RoomTypeCode>TH|001:AVAU:19491:M50496:219274:215398|PREMIER ROOM|SB*1#|BKK||ZDG.CQ|USD|JHPRZGK|~None</RoomTypeCode>" in body:
                file = open("providersimulation/rts/CancelDeadlineNonRefundable.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "GetRemarkHotelInformationForCustomerCount" in body:
            file = open("providersimulation/rts/RemarkHotelInformationRemarks.xml","r", encoding='utf8')
            data = file.read()
            file.close()
            data = self.ReplaceValuesInGetRemarkHotelInformationForCustomerCountResponse(body,data)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

    def ReplaceValuesInGetRemarkHotelInformationForCustomerCountResponse(self, body, responseData):
        try:
            from bs4 import BeautifulSoup
            parsedBody = BeautifulSoup(body, 'xml')
            itemCode = parsedBody.Body.GetRemarkHotelInformationForCustomerCount.HotelSearchListNetGuestCount.ItemCodeList.ItemCodeInfo.ItemCode.get_text()
            itemNo = parsedBody.Body.GetRemarkHotelInformationForCustomerCount.HotelSearchListNetGuestCount.ItemCodeList.ItemCodeInfo.ItemNo.get_text()
            roomTypeCode = parsedBody.Body.GetRemarkHotelInformationForCustomerCount.RoomTypeCode.get_text()
            responseData = str.replace(responseData, "{ITEM_CODE}", itemCode)
            responseData = str.replace(responseData, "{ITEM_NO}", itemNo)
            responseData = str.replace(responseData, "{ROOM_TYPE_CODE}", roomTypeCode)
            return responseData
        except Exception as e:
            return "<error>{}</error>".format(str(e))






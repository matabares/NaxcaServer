class RtsSimulation:

    def RtsResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")
        if "GetHotelSearchListForCustomerCount" in body:
            if "<CheckInDate>2030-01-01</CheckInDate>" in body:
                file = open("providersimulation/rts/1DayStay1Room1Adt.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            elif "<CheckInDate>2019-01-01</CheckInDate>" in body:
                file = open("providersimulation/rts/HotelSearch_3DayStay1Room1Adt.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            elif "<CheckInDate>2020-01-01</CheckInDate>" in body:
                file = open("providersimulation/rts/HotelSearch_3DayStay1Room1Adt_2Room2Adt1Chd.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            elif "<CheckInDate>2030-01-01</CheckInDate>" in body:
                file = open("providersimulation/rts/HotelSearch_3DayStay1Room2Adt_2Room2Adt.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            elif "<CheckInDate>2040-01-01</CheckInDate>" in body:
                file = open("providersimulation/rts/HotelSearch_3DayStay1Room2Adt1Chd.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            elif "<CheckInDate>2050-01-01</CheckInDate>" in body:
                file = open("providersimulation/rts/HotelSearch_3DayStay1Room2Adt1Inf.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            elif "<CheckInDate>2060-01-01</CheckInDate>" in body:
                file = open("providersimulation/rts/singleHotelSearch1adtBKK0001.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            elif "<CheckInDate>1492-10-12</CheckInDate>" in body:
                file = open("providersimulation/rts/singleHotelSearch1adtBKK0001.xml",
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
            if "<ItemCode>BKK</ItemCode>" in body and "<LanguageCode>AR</LanguageCode>" in body:
                file = open("providersimulation/rts/HotelInfoError.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<ItemCode></ItemCode>" in body :
                file = open("providersimulation/rts/HotelInfoHotelCodeIsMissing.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

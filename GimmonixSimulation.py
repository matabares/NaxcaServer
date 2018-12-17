class GimmonixSimulation:

    def GimmonixResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")

        if "HotelsServiceSearchRequest" in body:
            if "<CheckIn>2020-01-01T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_3DayStay1Room1Adt.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckIn>2020-01-02T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_3DayStay1Room2Adt1Chd.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckIn>2020-01-03T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_3DayStay1Room2Adt1Inf.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckIn>2020-01-04T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_3DayStay1Room2Adt_2Room2Adt.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckIn>2020-01-05T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_3DayStay1Room1Adt_2Room2Adt1Chd.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "GetPackagesRequest" in body:
            if "4116714" in body:
                file = open("providersimulation/gimmonix/getPackages_4116714.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "4116845"  in body:
                file = open("providersimulation/gimmonix/getPackages_4116845.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "4116742" in body:
                file = open("providersimulation/gimmonix/getPackages_4116742.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "HotelCancellationPolicyResponse" in body:
            if "<CheckIn>2020-01-01</CheckIn>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room1Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckIn>2020-01-02</CheckIn>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room2Adt1Chd.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckIn>2020-01-03</CheckIn>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room2Adt1Inf.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckIn>2020-01-04</CheckIn>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room2Adt_2Room2Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckIn>2020-01-05</CheckIn>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room1Adt_2Room2Adt1Chd.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "HotelBookInfoRequest" in body:
            if "<CheckIn>2020-01-01</CheckIn>" in body:
                file = open("providersimulation/gimmonix/successBooking_3DayStay1Room1Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckIn>2020-01-02</CheckIn>" in body:
                file = open("providersimulation/gimmonix/successBooking_3DayStay1Room2Adt1Chd.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckIn>2020-01-03</CheckIn>" in body:
                file = open("providersimulation/gimmonix/successBooking_3DayStay1Room2Adt1Inf.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckIn>2020-01-04</CheckIn>" in body:
                file = open("providersimulation/gimmonix/successBooking_3DayStay1Room2Adt_2Room2Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckIn>2020-01-05</CheckIn>" in body:
                file = open("providersimulation/gimmonix/successBooking_3DayStay1Room1Adt_2Room2Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
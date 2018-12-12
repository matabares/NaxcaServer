class GimmonixSimulation:

    def GimmonixResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")

        if "HotelsServiceSearchRequest" in body:
            if "<DetailLevel>LOW</DetailLevel>" in body:
                if "<CheckInDate>2020-01-01</CheckInDate>" in body:
                    file = open("providersimulation/gimmonix/hotelSearch_3DayStay1Room1Adt.xml","r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "<CheckInDate>2020-01-02</CheckInDate>" in body:
                    file = open("providersimulation/gimmonix/hotelSearch_3DayStay1Room2Adt1Chd.xml","r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "<CheckInDate>2020-01-03</CheckInDate>" in body:
                    file = open("providersimulation/gimmonix/hotelSearch_3DayStay1Room2Adt1Inf.xml","r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "<CheckInDate>2020-01-04</CheckInDate>" in body:
                    file = open("providersimulation/gimmonix/hotelSearch_3DayStay1Room2Adt_2Room2Adt.xml","r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "<CheckInDate>2020-01-05</CheckInDate>" in body:
                    file = open("providersimulation/gimmonix/hotelSearch_3DayStay1Room1Adt_2Room2Adt1Chd.xml","r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

        if "HotelCancellationPolicyResponse" in body:
            if "<CheckInDate>2020-01-01</CheckInDate>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room1Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-01-02</CheckInDate>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room2Adt1Chd.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-01-03</CheckInDate>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room2Adt1Inf.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-01-04</CheckInDate>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room2Adt_2Room2Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-01-05</CheckInDate>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room1Adt_2Room2Adt1Chd.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "HotelBookInfoRequest" in body:
            if "<CheckInDate>2020-01-01</CheckInDate>" in body:
                file = open("providersimulation/gimmonix/successBooking_3DayStay1Room1Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-01-02</CheckInDate>" in body:
                file = open("providersimulation/gimmonix/successBooking_3DayStay1Room2Adt1Chd.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-01-03</CheckInDate>" in body:
                file = open("providersimulation/gimmonix/successBooking_3DayStay1Room2Adt1Inf.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-01-04</CheckInDate>" in body:
                file = open("providersimulation/gimmonix/successBooking_3DayStay1Room2Adt_2Room2Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-01-05</CheckInDate>" in body:
                file = open("providersimulation/gimmonix/successBooking_3DayStay1Room1Adt_2Room2Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
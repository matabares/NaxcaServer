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


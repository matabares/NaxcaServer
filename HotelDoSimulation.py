import re


class HotelDoSimulation:

    def HotelDoResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")

        if 'GetQuoteHotels' in body:
            if "20300101" in body:
                file = open(
                    "providersimulation/hoteldo/1r1a_Search.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
        if 'GetRateRules' in body:
            if "20300101" in body:
                file = open(
                    "providersimulation/hoteldo/1r1a_Verify.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

import re


class HotelDoSimulation:

    def HotelDoResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml;charset=UTF-8')
        info.end_headers()

        if 'GetQuoteHotels' in info.path:
            if "20300101" in info.path:
                file = open(
                    "providersimulation/hoteldo/1r1a_Search.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "20300201" in info.path:
                file = open(
                    "providersimulation/hoteldo/1r1a_Search-2HotelsAvailable.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "20300102" in info.path:
                file = open(
                    "providersimulation/hoteldo/2a1chd_Search.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
        if 'GetRateRules' in info.path:
            if "20300101" in info.path:
                file = open(
                    "providersimulation/hoteldo/1r1a_Verify.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "20300101" in info.path:
                file = open(
                    "providersimulation/hoteldo/2a1chd_Verify.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

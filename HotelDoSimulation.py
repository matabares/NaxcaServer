import re


class HotelDoSimulation:

    def HotelDoResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'application/json; charset=utf-8')
        info.end_headers()

        file = open("providersimulation/hoteldo/hoteldo.xml","r", encoding='utf8')
        data = file.read()
        file.close()
        info.wfile.write(bytes(data, 'UTF-8'))
        return info

            

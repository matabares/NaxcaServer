import re
from datetime import datetime


class dingusProviderSimulation:

    def dingusResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml; charset=utf-8')
        info.end_headers()
        print(info.headers)
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody,"utf-8")

        if "OTA_HotelAvailRQ" in body:
            days = getDates(body)
            if days == 33:
                file = open("providersimulation\dingus\HotelConnector_HotelSearch_ReturnNonRefundableHotel.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            elif days == 20:
                file = open("providersimulation\dingus\HotelConnector_HotelSearch_AvailableCostOk.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "OTA_HotelAvailRQ" in body:
            if days == 40:
                file = open("providersimulation\dingus\HotelConnector_HotelVerify_ReservationOk.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "OTA_CancelRQ" in body:
            if 'HotelCode="1"' in body:
                file = open("providersimulation\dingus\HotelConnector_HotelCancel_CancelOk.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if 'HotelCode="2"' in body:
                file = open("providersimulation\dingus\HotelConnector_HotelCancel_DoubleCancelOk.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "OTA_HotelDescriptiveInfoRQ" in body:
            if 'HotelCode="8"' in body:
                file = open("providersimulation\dingus\HotelConnector_HotelInformation_HotelCategoryOk.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        info.send_error(404,"File not found")
        return info


def getDates(data):
    regex = re.findall(r'[0-9]*-[0-9]*-[0-9]*', data)
    dateFrom = datetime.strptime(regex[0], '%Y-%m-%d')
    dateTo = datetime.strptime(regex[1], '%Y-%m-%d')
    if dateFrom > dateTo:
        dateFrom = datetime.strptime(regex.index(1), '%Y-%m-%d')
    return dateFrom - datetime.now()

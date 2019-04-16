import datetime
from bs4 import BeautifulSoup

class TouricoHotelsSimulation:

    def GetCheckin(self):
        return datetime.date.today() + datetime.timedelta(days=30)

    def GetCheckout(self):
        return datetime.date.today() + datetime.timedelta(days=33)

    def ReplaceDates(self, data):
        data = str.replace(data, "{START_DATE}", self.GetCheckin().strftime("%Y-%m-%d"))
        return data

    def ReplaceDatesCancellationPolicies(self, data):
        data = str.replace(data, "{CANCEL_CHECKIN}", self.GetCheckin().strftime("%m/%d/%Y"))
        data = str.replace(data, "{CANCEL_CHECKOUT}", self.GetCheckout().strftime("%m/%d/%Y"))
        return data

    def ReplaceDatesBooking(self, data):
        data = str.replace(data, "{BOOKING_CHECKIN_DATE}", self.GetCheckin().strftime("%Y-%m-%d"))
        data = str.replace(data, "{BOOKING_CHECKOUT_DATE}", self.GetCheckin().strftime("%Y-%m-%d"))
        return data

    def TouricoResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml; charset=utf-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")
        bodyXml = BeautifulSoup(body, 'xml')

        # 1r1a
        if 'SearchHotels' in body and '<Destination xmlns="http://schemas.tourico.com/webservices/hotelv3">MIA</Destination>' in body:
            file = open("providersimulation/tourico/flow1r1a_searchresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            data = self.ReplaceDates(data)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'CheckAvailabilityAndPrices' in body and '<HotelIdInfo id="943"/>' in body:
            file = open("providersimulation/tourico/flow1r1a_checkavailabilityresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            data = self.ReplaceDates(data)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'GetCancellationPolicies' in body and '<hotelId>943</hotelId>' in body:
            file = open("providersimulation/tourico/flow1r1a_cancellationpoliciesresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            data = self.ReplaceDatesCancellationPolicies(data)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'BookHotelV3' in body and '<HotelId xmlns="http://schemas.tourico.com/webservices/hotelv3">943</HotelId>' in body:
            file = open("providersimulation/tourico/flow1r1a_bookhotelresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            data = self.ReplaceDatesBooking(data)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'CancelReservation' in body and '<nResID>164187981</nResID>' in body:
            file = open("providersimulation/tourico/flow1r1a_cancelreservationresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

from datetime import datetime
from bs4 import BeautifulSoup

class TouricoHotelsSimulation:

    def ReplaceDatesHotelSearch(self, data, requestXml, responseXml):
        data = data.replace(responseXml.Envelope.Body.SearchHotelsResponse.SearchHotelsResult.HotelList.Hotel.RoomTypes.RoomType.attrs['startDate'],
                            requestXml.Envelope.Body.SearchHotels.request.CheckIn.text + "T00:00:00")
        return data

    def ReplaceDatesCheckAvailabilityAndPrices(self, data, requestXml, responseXml):
        data = data.replace(responseXml.Envelope.Body.CheckAvailabilityAndPricesResponse.CheckAvailabilityAndPricesResult.HotelList.Hotel.RoomTypes.RoomType.attrs['startDate'],
                            requestXml.Envelope.Body.CheckAvailabilityAndPrices.request.CheckIn.text + "T00:00:00")
        return data

    def ReplaceDatesCancellationPolicies(self, data, requestXml, responseXml):
        data = data.replace(responseXml.Envelope.Body.GetCancellationPoliciesResponse.HotelPolicy.RoomTypePolicy.attrs['CheckIn'],
                            datetime.strptime(requestXml.Envelope.Body.GetCancellationPolicies.dtCheckIn.text[0:10], "%Y-%m-%d").strftime("%m/%d/%Y"))
        data = data.replace(responseXml.Envelope.Body.GetCancellationPoliciesResponse.HotelPolicy.RoomTypePolicy.attrs['CheckOut'],
                            datetime.strptime(requestXml.Envelope.Body.GetCancellationPolicies.dtCheckOut.text[0:10], "%Y-%m-%d").strftime("%m/%d/%Y"))
        return data

    def ReplaceDatesBooking(self, data, requestXml, responseXml):
        data = data.replace(responseXml.Envelope.Body.BookHotelV3Response.BookHotelV3Result.ResGroup.Reservations.Reservation.attrs['fromDate'],
                            requestXml.Envelope.Body.BookHotelV3.request.CheckIn.text + "T00:00:00")
        data = data.replace(responseXml.Envelope.Body.BookHotelV3Response.BookHotelV3Result.ResGroup.Reservations.Reservation.attrs['toDate'],
                            requestXml.Envelope.Body.BookHotelV3.request.CheckOut.text + "T00:00:00")
        return data

    def TouricoResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml; charset=utf-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")
        requestXml = BeautifulSoup(body, 'xml')

        # 1r1a
        if 'SearchHotels' in body \
                and requestXml.Envelope.Body.SearchHotels.request.Destination.text == 'MIA' \
                and requestXml.Envelope.Body.SearchHotels.request.RoomsInformation.RoomInfo.AdultNum.text == "1":
            file = open("providersimulation/tourico/flow1r1a_searchresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            responseXml = BeautifulSoup(data, 'xml')
            data = self.ReplaceDatesHotelSearch(data, requestXml, responseXml)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'CheckAvailabilityAndPrices' in body \
                and requestXml.Envelope.Body.CheckAvailabilityAndPrices.request.HotelIdsInfo.HotelIdInfo.attrs['id'] == '943':
            file = open("providersimulation/tourico/flow1r1a_checkavailabilityresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            responseXml = BeautifulSoup(data, 'xml')
            data = self.ReplaceDatesCheckAvailabilityAndPrices(data, requestXml, responseXml)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'GetCancellationPolicies' in body \
                and requestXml.Envelope.Body.GetCancellationPolicies.hotelId.text == '943':
            file = open("providersimulation/tourico/flow1r1a_cancellationpoliciesresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            responseXml = BeautifulSoup(data, 'xml')
            data = self.ReplaceDatesCancellationPolicies(data, requestXml, responseXml)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'BookHotelV3' in body \
                and requestXml.Envelope.Body.BookHotelV3.request.HotelId.text == '943':
            file = open("providersimulation/tourico/flow1r1a_bookhotelresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            responseXml = BeautifulSoup(data, 'xml')
            data = self.ReplaceDatesBooking(data, requestXml, responseXml)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'CancelReservation' in body \
                and requestXml.Envelope.Body.CancelReservation.nResID.text == '164187981':
            file = open("providersimulation/tourico/flow1r1a_cancelreservationresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        # 1r2a2c
        if 'SearchHotels' in body \
                and requestXml.Envelope.Body.SearchHotels.request.Destination.text == 'MIA' \
                and requestXml.Envelope.Body.SearchHotels.request.RoomsInformation.RoomInfo.AdultNum.text == "2" \
                and requestXml.Envelope.Body.SearchHotels.request.RoomsInformation.RoomInfo.ChildNum is not None \
                and requestXml.Envelope.Body.SearchHotels.request.RoomsInformation.RoomInfo.ChildNum.text == "2":
            file = open("providersimulation/tourico/flow1r2a2c_searchresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            responseXml = BeautifulSoup(data, 'xml')
            data = self.ReplaceDatesHotelSearch(data, requestXml, responseXml)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'CheckAvailabilityAndPrices' in body \
                and requestXml.Envelope.Body.CheckAvailabilityAndPrices.request.HotelIdsInfo.HotelIdInfo.attrs['id'] == '1492470':
            file = open("providersimulation/tourico/flow1r2a2c_checkavailabilityresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            responseXml = BeautifulSoup(data, 'xml')
            data = self.ReplaceDatesCheckAvailabilityAndPrices(data, requestXml, responseXml)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'GetCancellationPolicies' in body \
                and requestXml.Envelope.Body.GetCancellationPolicies.hotelId.text == '1492470':
            file = open("providersimulation/tourico/flow1r2a2c_cancellationpoliciesresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            responseXml = BeautifulSoup(data, 'xml')
            data = self.ReplaceDatesCancellationPolicies(data, requestXml, responseXml)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'BookHotelV3' in body \
                and requestXml.Envelope.Body.BookHotelV3.request.HotelId.text == '1492470':
            file = open("providersimulation/tourico/flow1r2a2c_bookhotelresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            responseXml = BeautifulSoup(data, 'xml')
            data = self.ReplaceDatesBooking(data, requestXml, responseXml)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'CancelReservation' in body \
                and requestXml.Envelope.Body.CancelReservation.nResID.text == '164195126':
            file = open("providersimulation/tourico/flow1r2a2c_cancelreservationresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        # 1r2a1c
        if 'SearchHotels' in body \
                and requestXml.Envelope.Body.SearchHotels.request.Destination.text == 'MIA' \
                and requestXml.Envelope.Body.SearchHotels.request.RoomsInformation.RoomInfo.AdultNum.text == "2" \
                and requestXml.Envelope.Body.SearchHotels.request.RoomsInformation.RoomInfo.ChildNum is not None \
                and requestXml.Envelope.Body.SearchHotels.request.RoomsInformation.RoomInfo.ChildNum.text == "1":
            file = open("providersimulation/tourico/flow1r2a1c_searchresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            responseXml = BeautifulSoup(data, 'xml')
            data = self.ReplaceDatesHotelSearch(data, requestXml, responseXml)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'CheckAvailabilityAndPrices' in body \
                and requestXml.Envelope.Body.CheckAvailabilityAndPrices.request.HotelIdsInfo.HotelIdInfo.attrs[
            'id'] == '1263768':
            file = open("providersimulation/tourico/flow1r2a1c_checkavailabilityresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            responseXml = BeautifulSoup(data, 'xml')
            data = self.ReplaceDatesCheckAvailabilityAndPrices(data, requestXml, responseXml)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'GetCancellationPolicies' in body \
                and requestXml.Envelope.Body.GetCancellationPolicies.hotelId.text == '1263768':
            file = open("providersimulation/tourico/flow1r2a1c_cancellationpoliciesresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            responseXml = BeautifulSoup(data, 'xml')
            data = self.ReplaceDatesCancellationPolicies(data, requestXml, responseXml)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'BookHotelV3' in body \
                and requestXml.Envelope.Body.BookHotelV3.request.HotelId.text == '1263768':
            file = open("providersimulation/tourico/flow1r2a1c_bookhotelresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            responseXml = BeautifulSoup(data, 'xml')
            data = self.ReplaceDatesBooking(data, requestXml, responseXml)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'CancelReservation' in body \
                and requestXml.Envelope.Body.CancelReservation.nResID.text == '164193008':
            file = open("providersimulation/tourico/flow1r2a1c_cancelreservationresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

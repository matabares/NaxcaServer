import datetime

class OlympiaSimulation:

    def GetCheckin(self):
        return datetime.date.today() + datetime.timedelta(days=5)

    def GetCheckout(self):
        return datetime.date.today() + datetime.timedelta(days=8)

    def ReplaceDates(self, data):
        data = str.replace(data, "{CHECKIN_DATE}", self.GetCheckin().strftime("%Y-%m-%d"))
        data = str.replace(data, "{CHECKOUT_DATE}", self.GetCheckout().strftime("%Y-%m-%d"))
        return data

    def OlympiaResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml; charset=utf-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")

        if "OTA_HotelAvailRQ" in body:
            if "2030-01-01" in body:
                file = open("providersimulation/olympia/search_1r1a_clx0.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-02" in body:
                file = open("providersimulation/olympia/search_1r1a_2r2a1c_clx0.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-03" in body:
                file = open("providersimulation/olympia/search_1r1a_2r2a1c_clx2.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-04" in body:
                file = open("providersimulation/olympia/search_1r1a_2r2a1c_clxnrf.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-05" in body:
                file = open("providersimulation/olympia/search_1r1a_2r2a1c_contracts0.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-06" in body:
                file = open("providersimulation/olympia/search_1r1a_2r2a1c_contracts2.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-07" in body:
                file = open("providersimulation/olympia/search_1r1a_2r2a1c_currEur.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-08" in body:
                file = open("providersimulation/olympia/search_1r1a_2r2a1c_currUsd.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-09" in body:
                file = open("providersimulation/olympia/search_1r1a_2r2a1c_hotels1rooms6.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-10" in body:
                file = open("providersimulation/olympia/search_1r1a_2r2a1c_hotels5.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-11" in body:
                file = open("providersimulation/olympia/search_1r1a_2r2a2c.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-12" in body:
                file = open("providersimulation/olympia/search_1r1a_clx2.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-13" in body:
                file = open("providersimulation/olympia/search_1r1a_clxnrf.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-14" in body:
                file = open("providersimulation/olympia/search_1r1a_contracts0.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-15" in body:
                file = open("providersimulation/olympia/search_1r1a_contracts2.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-16" in body:
                file = open("providersimulation/olympia/search_1r1a_currEur.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-17" in body:
                file = open("providersimulation/olympia/search_1r1a_currUsd.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-18" in body:
                file = open("providersimulation/olympia/search_1r1a_hotels1rooms5.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-19" in body:
                file = open("providersimulation/olympia/search_1r1a_hotels5.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-20" in body:
                file = open("providersimulation/olympia/search_1r1a_room_specialinfo.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-21" in body:
                file = open("providersimulation/olympia/search_1r2a1c.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-22" in body:
                file = open("providersimulation/olympia/search_1r2a1i.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-23" in body:
                file = open("providersimulation/olympia/search_1r2a_2r2a.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-24" in body:
                file = open("providersimulation/olympia/search_1r1a_2r2a1c_hotels1_clx0.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-25" in body:
                file = open("providersimulation/olympia/search_1r1a_2r2a1c_hotels1_clx2.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-26" in body:
                file = open("providersimulation/olympia/search_1r1a_2r2a1c_hotels1_contracts2_roomspecialinfo.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-27" in body:
                file = open("providersimulation/olympia/search_1r1a_2r2a1c_hotels1_clxnrf.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info


            #flujo 1
            if 'CityCode="T01"' in body:
                file = open("providersimulation/olympia/flow1_search_1r1a.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                data = self.ReplaceDates(data)
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if 'HotelCode="0001"' in body:
                file = open("providersimulation/olympia/flow1_search_hotel_0001.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                data = self.ReplaceDates(data)
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "OTA_HotelResRQ" and "Transaction=PreBooking" in body:

            #flujo 1
            if 'BookingCode="test1test1test1test1"' in body:
                file = open("providersimulation/olympia/flow1_prebooking_ok.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "OTA_HotelResRQ" and "Transaction=Booking" in body:

            #flujo 1
            if 'BookingCode="test1test1test1test1"' in body:
                file = open("providersimulation/olympia/flow1_reservation_ok.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "OTA_HotelResRQ" and "Transaction=Cancel" in body:

            #flujo 1
            if 'Type="Locator" ID="100000"' in body:
                file = open("providersimulation/olympia/flow1_cancel_ok.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
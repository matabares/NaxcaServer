import datetime
import json

class ApitudeHotelesSimulation:

    def ReplaceCancelationPoliciesDates(self, data, checkIn):
        jsonBody = json.loads(data)
        for hotel in jsonBody['hotels']['hotels']:
            for room in hotel['rooms']:
                for rate in room['rates']:
                    if 'cancellationPolicies' in rate:
                        offset = 0
                        for clx in rate['cancellationPolicies']:
                            offset = offset + 2
                            clxDate = checkIn - datetime.timedelta(days=offset)
                            clx['from'] = clxDate.strftime('%Y-%m-%d')+"T23:59:00+02:00"
        return json.dumps(jsonBody)



    def ApitudeDeleteResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'application/json;charset=UTF-8')
        info.end_headers()
        #1r1a_hotelcode10
        if "10-4200606" in info.path:
            file = open("providersimulation/apitudehoteles/flow1r1a_cancel_ok.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        # 1r1a_hotelcode20
        if "20-4200606" in info.path:
            file = open("providersimulation/apitudehoteles/flow1r1a_cancel_ok.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        # 1r1a_hotelcode30
        if "30-4200606" in info.path:
            file = open("providersimulation/apitudehoteles/flow1r1a_cancel_ok.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        # 1r1a_hotelcode40
        if "40-4200606" in info.path:
            file = open("providersimulation/apitudehoteles/flow1r1a_cancel_ok.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        # 1r1a_hotelcode90
        if "90-4200606" in info.path:
            file = open("providersimulation/apitudehoteles/cancel_error.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        # 1r1a_hotelcode100
        if "100-4200606" in info.path:
            file = open("providersimulation/apitudehoteles/cancel_error.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        # 1r2a1c
        if "1-4226257" in info.path:
            file = open("providersimulation/apitudehoteles/flow1r2a1c_cancel_ok.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        # 1r2a2c
        if "1-4226258" in info.path:
            file = open("providersimulation/apitudehoteles/flow1r2a2c_cancel_ok.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        # 1r2a_2r2a
        if "1-4226330" in info.path:
            file = open("providersimulation/apitudehoteles/flow1r2a_2r2a_cancel_ok.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        # 1r1a_2r2a1c_hotelcode10
        if "10-4226404" in info.path:
            file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_cancel_ok.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
            # 1r1a_2r2a1c_hotelcode20
        if "20-4226404" in info.path:
            file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_cancel_ok.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        # 1r1a_2r2a1c_hotelcode30
        if "30-4226404" in info.path:
            file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_cancel_ok.json", "r",
                        encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        # 1r1a_2r2a1c_hotelcode40
        if "40-4226404" in info.path:
            file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_cancel_ok.json", "r",
                        encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        # 1r1a_2r2a1c_hotelcode90
        if "90-4226404" in info.path:
            file = open("providersimulation/apitudehoteles/cancel_error.json", "r",
                        encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        # 1r1a_2r2a1c_hotelcode100
        if "100-4226404" in info.path:
            file = open("providersimulation/apitudehoteles/cancel_error.json", "r",
                        encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        # 1r3a_2r4a
        if "1-4226551" in info.path:
            file = open("providersimulation/apitudehoteles/flow1r3a_2r4a_cancel_ok.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info


    def ApitudeGetResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'application/json;charset=UTF-8')
        info.end_headers()

        if 'hotels/1?language=ENG' in info.path:
            file = open("providersimulation/apitudehoteles/hotelinfo_en_ok.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'hotels/0?language=ENG' in info.path:
            file = open("providersimulation/apitudehoteles/hotelinfo_error.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        if 'types/ratecommentdetails' in info.path:
            file = open("providersimulation/apitudehoteles/ratecommentsdetails.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info


    def ApitudePostResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'application/json;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")
        jsonBody = json.loads(body)
        today = datetime.datetime.now()

        if "hotels" in info.path:
            checkIn = datetime.datetime.strptime(jsonBody['stay']['checkIn'], "%Y-%m-%d")
            checkOut = datetime.datetime.strptime(jsonBody['stay']['checkOut'], "%Y-%m-%d")
            occupanciesCount = len(jsonBody['occupancies'])
            latitude = jsonBody['geolocation']['latitude']
            longitude = jsonBody['geolocation']['longitude']
            radius = jsonBody['geolocation']['radius']
            occupanciesCount = len(jsonBody['occupancies'])
            if occupanciesCount == 1:
                adultCount = jsonBody['occupancies'][0]['adults']
                childCount = jsonBody['occupancies'][0].get('children', 0)
                #1r1a
                if adultCount == 1 and childCount == 0:
                    file = open("providersimulation/apitudehoteles/flow1r1a_searchresponse.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    data = self.ReplaceCancelationPoliciesDates(data, checkIn)
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

                #1r2a1c
                if adultCount == 2 and childCount == 1:
                    file = open("providersimulation/apitudehoteles/flow1r2a1c_searchresponse.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    data = self.ReplaceCancelationPoliciesDates(data, checkIn)
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

                # 1r2a2c
                if adultCount == 2 and childCount == 2:
                    file = open("providersimulation/apitudehoteles/flow1r2a2c_searchresponse.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    data = self.ReplaceCancelationPoliciesDates(data, checkIn)
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
            if occupanciesCount == 2:
                adultCountRoom1 = jsonBody['occupancies'][0]['adults']
                childCountRoom1 = jsonBody['occupancies'][0].get('children', 0)
                adultCountRoom2 = jsonBody['occupancies'][1]['adults']
                childCountRoom2 = jsonBody['occupancies'][1].get('children', 0)

                #1r1a_2r2a1c
                if adultCountRoom1 == 1 and childCountRoom1 == 0 and adultCountRoom2 == 2 and childCountRoom2 == 1:
                    file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_searchresponse.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    data = self.ReplaceCancelationPoliciesDates(data, checkIn)
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

                #1r2a_2r2a
                if adultCountRoom1 == 2 and childCountRoom1 == 0 and adultCountRoom2 == 2 and childCountRoom2 == 0:
                    file = open("providersimulation/apitudehoteles/flow1r2a_2r2a_searchresponse.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    data = self.ReplaceCancelationPoliciesDates(data, checkIn)
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

                # 1r3a_2r4a
                if adultCountRoom1 == 3 and childCountRoom1 == 0 and adultCountRoom2 == 4 and childCountRoom2 == 0:
                    file = open("providersimulation/apitudehoteles/flow1r3a_2r4a_searchresponse.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    data = self.ReplaceCancelationPoliciesDates(data, checkIn)
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info


        if 'checkrates' in info.path:
            roomsCount = len(jsonBody['rooms'])
            if roomsCount == 1:
                rateKey = jsonBody['rooms'][0]['rateKey']
                if "1r1a_rk10" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r1a_checkrates_hotelcode10.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk20" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r1a_checkrates_hotelcode20.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk30" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r1a_checkrates_hotelcode30.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk40" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r1a_checkrates_hotelcode40.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk50" in rateKey:
                    file = open("providersimulation/apitudehoteles/checkrates_error.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk60" in rateKey:
                    file = open("providersimulation/apitudehoteles/checkrates_error.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk70" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r1a_checkrates_hotelcode70.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk80" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r1a_checkrates_hotelcode80.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk90" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r1a_checkrates_hotelcode90.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk100" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r1a_checkrates_hotelcode100.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r2a1c_rk10" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r2a1c_checkratesresponse.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r2a2c_rk10" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r2a2c_checkratesresponse.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
            if roomsCount == 2:
                rateKeyRoom1 = jsonBody['rooms'][0]['rateKey']
                rateKeyRoom2 = jsonBody['rooms'][1]['rateKey']
                if "1r2a_2r2a_rk10" in rateKeyRoom1 and "1r2a_2r2a_rk11" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r2a_2r2a_checkratesresponse.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk10" in rateKeyRoom1 and "1r1a_2r2a1c_rk11" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_checkrates_hotelcode10.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk20" in rateKeyRoom1 and "1r1a_2r2a1c_rk21" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_checkrates_hotelcode20.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk30" in rateKeyRoom1 and "1r1a_2r2a1c_rk31" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_checkrates_hotelcode30.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk40" in rateKeyRoom1 and "1r1a_2r2a1c_rk41" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_checkrates_hotelcode40.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk50" in rateKeyRoom1 and "1r1a_2r2a1c_rk51" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/checkrates_error.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk60" in rateKeyRoom1 and "1r1a_2r2a1c_rk61" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/checkrates_error.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk70" in rateKeyRoom1 and "1r1a_2r2a1c_rk71" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_checkrates_hotelcode70.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk80" in rateKeyRoom1 and "1r1a_2r2a1c_rk81" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_checkrates_hotelcode80.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk90" in rateKeyRoom1 and "1r1a_2r2a1c_rk91" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_checkrates_hotelcode90.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk100" in rateKeyRoom1 and "1r1a_2r2a1c_rk101" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_checkrates_hotelcode100.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r3a_2r4a_rk10" in rateKeyRoom1 and "1r3a_2r4a_rk11" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r3a_2r4a_checkratesresponse.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

        if 'booking' in info.path:
            roomsCount = len(jsonBody['rooms'])
            if roomsCount == 1:
                rateKey = jsonBody['rooms'][0]['rateKey']
                if "1r1a_rk10" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r1a_booking_hotelcode10.json.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk20" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r1a_booking_hotelcode20.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk30" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r1a_booking_hotelcode30.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk40" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r1a_booking_hotelcode40.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk70" in rateKey:
                    file = open("providersimulation/apitudehoteles/booking_error.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk80" in rateKey:
                    file = open("providersimulation/apitudehoteles/booking_error.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk90" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r1a_booking_hotelcode90.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_rk100" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r1a_booking_hotelcode100.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r2a1c_rk10" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r2a1c_bookingresponse.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r2a2c_rk10" in rateKey:
                    file = open("providersimulation/apitudehoteles/flow1r2a2c_bookingresponse.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
            if roomsCount == 2:
                rateKeyRoom1 = jsonBody['rooms'][0]['rateKey']
                rateKeyRoom2 = jsonBody['rooms'][1]['rateKey']
                if "1r2a_2r2a_rk10" in rateKeyRoom1 and "1r2a_2r2a_rk11" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r2a_2r2a_bookingresponse.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk10" in rateKeyRoom1 and "1r1a_2r2a1c_rk11" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r2a_2r2a1c_booking_hotelcode10.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk20" in rateKeyRoom1 and "1r1a_2r2a1c_rk21" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r2a_2r2a1c_booking_hotelcode20.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk30" in rateKeyRoom1 and "1r1a_2r2a1c_rk31" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r2a_2r2a1c_booking_hotelcode30.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk40" in rateKeyRoom1 and "1r1a_2r2a1c_rk41" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r2a_2r2a1c_booking_hotelcode40.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk70" in rateKeyRoom1 and "1r1a_2r2a1c_rk71" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/booking_error.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk80" in rateKeyRoom1 and "1r1a_2r2a1c_rk81" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/booking_error.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk90" in rateKeyRoom1 and "1r1a_2r2a1c_rk91" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r2a_2r2a1c_booking_hotelcode90.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r1a_2r2a1c_rk100" in rateKeyRoom1 and "1r1a_2r2a1c_rk101" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r2a_2r2a1c_booking_hotelcode100.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
                if "1r3a_2r4a_rk10" in rateKeyRoom1 and "1r3a_2r4a_rk11" in rateKeyRoom2:
                    file = open("providersimulation/apitudehoteles/flow1r3a_2r4a_bookingresponse.json", "r",
                                encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info
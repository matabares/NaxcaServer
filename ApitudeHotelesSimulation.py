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
                            clx['from'] = f"{(checkIn - datetime.timedelta(days=offset)).strftime('%Y-%m-%d')}T23:59:00+02:00"
        return json.dumps(jsonBody)



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
            checkIn = jsonBody['stay']['checkIn']
            checkOut = jsonBody['stay']['checkOut']
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
                if adultCount == 2 and childCount ==1:
                    file = open("providersimulation/apitudehoteles/flow1r2a1c_searchresponse.json", "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    data = self.ReplaceCancelationPoliciesDates(data, checkIn)
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

        if 'checkrates' in info.path:
            rateKey = jsonBody['rooms'][0]['rateKey']
            if rateKey == "":
                pass




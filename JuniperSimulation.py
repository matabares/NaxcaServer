class juniperProviderSimulation:

    def juniperResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")

        if "OTA_HotelAvail" in body:
                file = open(
                    "providersimulation/junipersimulation/1adtSearchMIA.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "OTA_HotelBookingRule" in body:
            if ("3MOkqa56LFbIGLeI" in body):
                file = open(
                  "providersimulation/junipersimulation/BookingRuleService.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if ("ihq5vLqy" in body):
                file = open(
                    "providersimulation/junipersimulation/BookingRuleServiceBadDown.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if ("5FvH3EFyDZNMxY3I4Q6ztZi2" in body):
                file = open(
                    "providersimulation/junipersimulation/BookingRuleServiceBadUp.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if ("nKaLlvBMaZyl" in body):
                file = open(
                    "providersimulation/junipersimulation/BookingRuleServiceGoodDown.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if ("aRIRzh7dFnJ4an" in body):
                file = open(
                    "providersimulation/junipersimulation/BookingRuleServiceGoodUp.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info


        if "OTA_HotelRes" in body:
            if "500" in body:
                file = open(
                    "providersimulation/junipersimulation/HotelRes.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "501" in body:
                file = open(
                    "providersimulation/junipersimulation/HotelResErrorDown.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "600" in body:
                file = open(
                    "providersimulation/junipersimulation/HotelResErrorUp.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "400" in body:
                file = open(
                    "providersimulation/junipersimulation/HotelResGoodDown.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "499" in body:
                file = open(
                    "providersimulation/junipersimulation/HotelResGoodUp.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
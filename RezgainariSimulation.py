class RezgainariSimulation:
    def RezariResponse(self, response):
        response.send_response(200)
        response.send_header('Content-Type', 'text/xml;charset=UTF-8')
        response.end_headers()
        contentLen = int(response.headers['Content-Length'])
        postBody = response.rfile.read(contentLen)
        body = str(postBody, "utf-8")

        if "HotelARIGetRQ" in body:
            file = open("providersimulation/rezgainari/HotelARIGetRS_No_Inventory.xml",
                        "r", encoding='utf8')
            data = file.read()
            file.close()
            response.wfile.write(bytes(data, 'UTF-8'))
            return response

        if "HotelPropertyListGetRQ" in body:
            if 'ChainCode=""' in body or 'ChainCode="1173"' in body:
                file = open("providersimulation/rezgainari/HotelPropertyListGetRS_ChainProperty.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                response.wfile.write(bytes(data, 'UTF-8'))
                return response
        if "HotelProductListGetRS" in body:
            if 'HotelCode="HMWMH"' in body:
                file = open("providersimulation/rezgainari/HotelProductListGetRS_Success.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                response.wfile.write(bytes(data, 'UTF-8'))
                return response






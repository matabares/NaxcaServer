class HotelBedsSimulation:

    def HotelBedsResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")

        if "HotelValuedAvailRQ" in body:
                file = open("providersimulation/hotelBeds/search.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "ServiceAddRQ" in body:
            file = open("providersimulation/hotelBeds/verify.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
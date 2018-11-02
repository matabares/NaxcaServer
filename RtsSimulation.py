class RtsSimulation:

    def RtsResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")
        print(body)
        print(info.path)


        if "NDC_AirShopping_16.1" in info.path:

            if "<Date>2030-01-01</Date>" in body:
                file = open("providersimulation/avianca/Domestic1AdtOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                print(data)
                return info
            if "<Date>2030-01-02</Date>" in body:
                file = open("providersimulation/avianca/Domestic1AdtRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

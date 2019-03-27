

class ApitudeHotelesSimulation:

    def ApitudeResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'application/json;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")

        if '"latitude": 1' in body:
            file = open("providersimulation/apitudehoteles/flow1r1a_searchresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info




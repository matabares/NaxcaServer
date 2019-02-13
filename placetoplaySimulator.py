class placetoplaySimulation:

    def P2pResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")
        file = open("providersimulation/p2p/placetoplayaprobadoyrechazado.xml", "r", encoding='utf8')
        data = file.read()
        file.close()
        info.wfile.write(bytes(data, 'UTF-8'))
        return info
import re


class RentingSimulation:

    def RentingResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'application/json; charset=utf-8')
        info.end_headers()

        if "get-matrix" in info.path:
            file = open("providersimulation\\rentingcarz\\NEWCOMPANY.json","r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
            

class HotelBedsSimulation:

    def HotelBedsResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")

        if "HotelValuedAvailRQ" in body:
                file = open("providersimulation/hotelBeds/Search 113715943-808B5D-DFROM_20190301_DTO_20190305_CTO_MDE_HotelValuedAvailRS.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "ServiceAddRQ" in body:
            if "MIA" in body:
                file = open("providersimulation/hotelBeds/Tarifa mas alta 113933827-F87ED6-DFROM_20190301_DTO_20190305_CTO_MDE_ServiceAddRS.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "PAR" in body:
                file = open("providersimulation/hotelBeds/Cambio de tarifa y descuento 113933827-F87ED6-DFROM_20190301_DTO_20190305_CTO_MDE_ServiceAddRS.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "BOG" in body:
                file = open("providersimulation/hotelBeds/Cambio de tarifa 113933827-F87ED6-DFROM_20190301_DTO_20190305_CTO_MDE_ServiceAddRS.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "ISA" in body:
                file = open("providersimulation/hotelBeds/Cambio de políticas 113933827-F87ED6-DFROM_20190301_DTO_20190305_CTO_MDE_ServiceAddRS.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "ADZ" in body:
                file = open("providersimulation/hotelBeds/Cambio de descuento 113933827-F87ED6-DFROM_20190301_DTO_20190305_CTO_MDE_ServiceAddRS.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
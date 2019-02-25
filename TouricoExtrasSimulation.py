class TouricoExtrasSimulation:

    def TouricoExtrasResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")

        if 'SearchActivityByDestinationIds' in body:
            if "2030-01-01" in body:
                file = open(
                        "providersimulation/TouricoExtras/search_1act_CurrencyEur.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-02" in body:
                file = open(
                        "providersimulation/TouricoExtras/search_3act.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-03" in body:
                file = open(
                        "providersimulation/TouricoExtras/search_1a_tax.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-04" in body:
                file = open(
                        "providersimulation/TouricoExtras/search1a_1_Cat_1Act_1ActOpt_2Avail.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-05" in body:
                file = open(
                        "providersimulation/TouricoExtras/search1a_2Cat.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "2030-01-06" in body:
                file = open(
                        "providersimulation/TouricoExtras/search1a_2Cat.xml",
                        "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
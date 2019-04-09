import datetime

class TouricoHotelsSimulation:

    def GetCheckin(self):
        return datetime.date.today() + datetime.timedelta(days=30)

    def GetCheckout(self):
        return datetime.date.today() + datetime.timedelta(days=33)

    def ReplaceDates(self, data):
        data = str.replace(data, "{START_DATE}", self.GetCheckin().strftime("%Y-%m-%d"))
        return data

    def TouricoResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml; charset=utf-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")

        # 1r1a
        if '<Destination xmlns="http://schemas.tourico.com/webservices/hotelv3">MIA</Destination>' in body:
            file = open("providersimulation/tourico/flow1r1a_searchresponse.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            data = self.ReplaceDates(data)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
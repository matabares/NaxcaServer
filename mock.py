from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from json2html import json2html
import os

from HotelBedsSimulation import HotelBedsSimulation
from TouricoExtrasSimulation import TouricoExtrasSimulation
from dingusProvider import dingusProviderSimulation
from jumboProvider import jumboProviderSimulation
from wegoProvider import wegoProviderSimulation
from AviancaSimulation import AviancaSimulation
from RtsSimulation import RtsSimulation
from RentingSimulation import RentingSimulation
from GimmonixSimulation import GimmonixSimulation
from VivaColombiaSimulation import VivaColombiaSimulation
from HotelDoSimulation import HotelDoSimulation
from OlympiaSimulation import OlympiaSimulation
from RezgainariSimulation import RezgainariSimulation
from ApitudeHotelesSimulation import ApitudeHotelesSimulation
from TouricoHotelsSimulation import TouricoHotelsSimulation

class NetSuiteProviderBaseHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if "providersimulationraw" in self.path:
            if (str(self.path).endswith(".json") or str(self.path).endswith(".xml")):
                self.send_response(200)
                if(str(self.path).endswith(".json")):
                    self.send_header('Content-Type', 'application/json')
                if (str(self.path).endswith(".xml")):
                    self.send_header('Content-Type', 'text/xml, application/xml')
                self.end_headers()
                path = self.path
                path = path.replace('providersimulationraw','providersimulation')
                filename = str(path)[1:]
                file = open(filename, "r", encoding='utf8')
                data = file.read()
                file.close()
                self.wfile.write(bytes(str(data), 'UTF-8'))
                return

        if "providersimulation" in self.path:
            if (str(self.path).endswith(".json") or str(self.path).endswith(".xml")):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                filename = str(self.path)[1:]
                file = open(filename, "r", encoding='utf8')
                data = file.read()
                file.close()
                if(str(self.path).endswith(".json")):
                    data = json2html.convert(json=json.loads(data), table_attributes="class=\"table table-condensed table-bordered table-hover\"")
                if (str(self.path).endswith(".xml")):
                    data = json.dumps(bf.data(fromstring(data)))
                    data = json2html.convert(json=json.loads(data), table_attributes="class=\"table table-condensed table-bordered table-hover\"")

                data = '<head><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"></head><body>' + data + "</body></html>"
                self.wfile.write(bytes(str(data), 'UTF-8'))
                return

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            rootDir = 'providersimulation/'
            rootRawDir = 'providersimulationraw/'
            htmlResponse = ''
            for subdir, dirs, files in os.walk(rootDir):
                for file in files:
                    fileLink = '<a href="/'+subdir +'/'+ file + '">' + file + '</a><br/>'
                    fileLinkRaw = '<a href="/'+ subdir +'/'+ file + '">[raw]</a><br/>'
                    fileLinkRaw = fileLinkRaw.replace(rootDir,rootRawDir)
                    htmlResponse = htmlResponse + '<tr> <td scope="row">'+subdir.split('/')[1]+'</td> <td>'+fileLink+ ' '+ fileLinkRaw +'</td> </tr>'


            htmlResponse = '<table class="table table-bordered"> <thead> <tr> <th scope="col">Provider</th> <th scope="col">File</th> </tr> </thead> <tbody> ' + htmlResponse + '</tbody> </table>'
            htmlResponse = '<html><head><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"></head><body>' + htmlResponse + "</body></html>"
            self.wfile.write(bytes(str(htmlResponse), 'UTF-8'))

            #self.wfile.write(bytes("<version>2.2.39</version>", 'UTF-8'))








        if "apitudehotelessimulation" in self.path:
            apitude = ApitudeHotelesSimulation()
            response = apitude.ApitudeGetResponse(self)
            return response

        if "wegosimulation" in self.path:
            wego = wegoProviderSimulation()
            response = wegoProviderSimulation(self)
            return response
        if "rentingsimulation" in self.path:
            renting = RentingSimulation()
            response = renting.RentingResponse(self)
            return response
        if "rezgainari/logs" in self.path:
            if(str(self.path).endswith(".log") or str(self.path).endswith(".txt")):
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                filename = str(self.path)[1:]
                file = open(filename,"r", encoding='utf8')
                data = file.read()
                file.close()
                self.wfile.write(bytes(str(data), 'UTF-8'))
                return

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            from os import listdir
            from os.path import isfile, join
            onlyfiles = [f for f in listdir("providersimulation/rezgainari/logs/") if isfile(join("providersimulation/rezgainari/logs/", f))]
            print(onlyfiles)
            htmlResponse = ""
            for file in onlyfiles:
                htmlResponse = htmlResponse + '<a href="/providersimulation/rezgainari/logs/'+str(file)+'">'+str(file)+'</a><br/>';
            htmlResponse = "<html><body>"+htmlResponse+"</body></html>"
            self.wfile.write(bytes(str(htmlResponse), 'UTF-8'))

        if "hoteldosimulation" in self.path:
            hoteldo = HotelDoSimulation()
            response = hoteldo.HotelDoResponse(self)
            return response

        if "version" in self.path:
            self.send_response(200)
            self.send_header('Content-Type', 'text/xml')
            self.end_headers()
            self.wfile.write(bytes("<version>2.2.42</version>", 'UTF-8'))



    def do_POST(self):
        if "vivacolombiasimulation" in self.path:
            vivacolombia = VivaColombiaSimulation()
            response = vivacolombia.VivaColombiaResponse(self)
            return response
        if "dingussimulation" in self.path:
            dingus = dingusProviderSimulation()
            response = dingus.dingusResponse(self)
            return response
        if "rentingsimulation" in self.path:
            renting = RentingSimulation()
            response = renting.RentingResponse(self)
            return response
        if "jumbosimulation" in self.path:
            jumbo = jumboProviderSimulation()
            response = jumbo.dingusResponse(self)
            return response

        if "aviancasimulation" in self.path:
            avianca = AviancaSimulation()
            response = avianca.AviancaResponse(self)
            return response

        if "rtssimulation" in self.path:
            rts = RtsSimulation()
            response = rts.RtsResponse(self)
            return response

        if "gimmonixsimulation" in self.path:
            gimmonix = GimmonixSimulation()
            response = gimmonix.GimmonixResponse(self)
            return response

        if "hoteldosimulation" in self.path:
            hoteldo = HotelDoSimulation()
            response = hoteldo.HotelDoResponse(self)
            return response

        if "olympiasimulation" in self.path:
            olympia = OlympiaSimulation()
            response = olympia.OlympiaResponse(self)
            return response

        if "hotelbeds" in self.path:
            hotelBeds = HotelBedsSimulation()
            response = hotelBeds.HotelBedsResponse(self)
            return response
        if "touricoextrasimulation" in self.path:
            touricoExtras = TouricoExtrasSimulation()
            response = touricoExtras.TouricoExtrasResponse(self)
            return response

        if "placetoplayaprobadoyrechazado" in self.path:
            self.send_response(200)
            self.send_header('Content-Type', 'text')
            self.end_headers()
            self.wfile.write(bytes("1,,00,Aprobada,000000,S,1550014251,10786860,,416900,CC,AUTH_CAPTURE,CC 789876,Johana,Gomez,,Virrey,,,,,9876789,,jgomez@netactica.com,Lautaro,Silva,,,,,,,0,,,,,26bf80fb175ca761658b38a8885ea0d3,P,,COP,1,416900,CR_VS,BANCO DE PRUEBAS,01fe9bf54bed5b62867d3d7aa77bb553,2,00,000000,1550014251,1467716914,000,****1111,,,,,,,,,,,,,,,,ES,10000,1597,0,99,88,82600", 'UTF-8'))

        if "rezgainari" in self.path:
            rezgain = RezgainariSimulation()
            response = rezgain.RezariResponse(self)
            return response

        if "apitudehotelessimulation" in self.path:
            apitudeHoteles = ApitudeHotelesSimulation()
            response = apitudeHoteles.ApitudePostResponse(self)
            return response

        if "touricohotelsimulation" in self.path:
            touricoHoteles = TouricoHotelsSimulation()
            response = touricoHoteles.TouricoResponse(self)
            return response






def Run(server_class=HTTPServer, handler_class=NetSuiteProviderBaseHTTPRequestHandler):
    port = 8000
    server_address = ('', port)
    print("Server Running on port {}".format(port))
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    Run()

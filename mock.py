from http.server import HTTPServer, BaseHTTPRequestHandler
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

class NetSuiteProviderBaseHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if "wegosimulation" in self.path:
            wego = wegoProviderSimulation()
            response = wegoProviderSimulation(self)
            return response
        if "rentingsimulation" in self.path:
            renting = RentingSimulation()
            response = renting.RentingResponse(self)
            return response
        if "version" in self.path:
            self.send_response(200)
            self.send_header('Content-Type', 'text/xml')
            self.end_headers()
            self.wfile.write(bytes("<version>2.2.11</version>", 'UTF-8'))
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


def Run(server_class=HTTPServer, handler_class=NetSuiteProviderBaseHTTPRequestHandler):
    port = 8000
    server_address = ('', port)
    print("Server Running on port {}".format(port))
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    Run()
from http.server import HTTPServer, BaseHTTPRequestHandler
from dingusProvider import dingusProviderSimulation
from jumboProvider import jumboProviderSimulation
from wegoProvider import wegoProviderSimulation
from AviancaSimulation import AviancaSimulation
from RtsSimulation import RtsSimulation
from RentingSimulation import RentingSimulation
from GimmonixSimulation import GimmonixSimulation

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
            self.wfile.write(bytes("<version>2.1.4</version>", 'UTF-8'))

    def do_POST(self):
        if "dingussimulation" in self.path:
            dingus = dingusProviderSimulation()
            response = dingus.dingusResponse(self)
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


def Run(server_class=HTTPServer, handler_class=NetSuiteProviderBaseHTTPRequestHandler):
    server_address = ('', 8000)
    print("Server Running")
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    Run()
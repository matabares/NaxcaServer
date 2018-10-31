from http.server import HTTPServer, BaseHTTPRequestHandler
from dingusProvider import dingusProviderSimulation
from jumboProvider import jumboProviderSimulation
from wegoProvider import wegoProviderSimulation
from AviancaSimulation import AviancaSimulation


class NetSuiteProviderBaseHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if "wegosimulation" in self.path:
            wego = wegoProviderSimulation()
            response = wegoProviderSimulation(self)
            return response


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


def Run(server_class=HTTPServer, handler_class=NetSuiteProviderBaseHTTPRequestHandler):
    server_address = ('', 8000)
    print("Server Running")
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    Run()
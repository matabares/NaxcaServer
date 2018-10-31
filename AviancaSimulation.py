import re
from datetime import datetime

class AviancaSimulation:

    def AviancaResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")
        print(body)
        print(info.path)


        if "NDC_AirShopping_16.1" in info.path:

            if "<Date>2030-01-01</Date>" in body:
                file = open("providersimulation/avianca/Domestic1AdtOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                print(data)
                return info
            if "<Date>2030-01-02</Date>" in body:
                file = open("providersimulation/avianca/Domestic1AdtRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-03</Date>" in body:
                file = open("providersimulation/avianca/Domestic2Adt1ChdOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-04</Date>" in body:
                file = open("providersimulation/avianca/Domestic2AdtOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-05</Date>" in body:
                file = open("providersimulation/avianca/Domestic2AdtRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-06</Date>" in body:
                file = open("providersimulation/avianca/Domestic2Adt1ChdRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-07</Date>" in body:
                file = open("providersimulation/avianca/Domestic1Adt1ChdOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-08</Date>" in body:
                file = open("providersimulation/avianca/Domestic3Adt2Chd1InfOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-09</Date>" in body:
                file = open("providersimulation/avianca/Domestic2Adt2ChdOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-10</Date>" in body:
                file = open("providersimulation/avianca/Domestic2Adt2ChdRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-11</Date>" in body:
                file = open("providersimulation/avianca/Domestic3Adt2Chd1InfRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-12</Date>" in body:
                file = open("providersimulation/avianca/Domestic2Adt1InfOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-13</Date>" in body:
                file = open("providersimulation/avianca/Domestic2Adt1InfRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-14</Date>" in body:
                file = open("providersimulation/avianca/DomesticOWNonStopFlight.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-15</Date>" in body:
                file = open("providersimulation/avianca/DomesticOWNonStopFlight1Flight.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            #######
            if "<Date>2030-01-16</Date>" in body:
                file = open("providersimulation/avianca/Domestic2Adt2ChdOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-17</Date>" in body:
                file = open("providersimulation/avianca/Domestic2Adt2ChdRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-18</Date>" in body:
                file = open("providersimulation/avianca/DomesticOWConnectionFlight.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-19</Date>" in body:
                file = open("providersimulation/avianca/DomesticOWDirectFlight.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-20</Date>" in body:
                file = open("providersimulation/avianca/DomesticRTConnectionFlight.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-21</Date>" in body:
                file = open("providersimulation/avianca/DomesticRTDirectFlight.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-22</Date>" in body:
                file = open("providersimulation/avianca/DomesticRTNonStopFlight.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-23</Date>" in body:
                file = open("providersimulation/avianca/International1Adt1ChdOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-24</Date>" in body:
                file = open("providersimulation/avianca/International1Adt1ChdRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-25</Date>" in body:
                file = open("providersimulation/avianca/International1AdtOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-26</Date>" in body:
                file = open("providersimulation/avianca/International1AdtRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-27</Date>" in body:
                file = open("providersimulation/avianca/International2Adt1ChdOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-28</Date>" in body:
                file = open("providersimulation/avianca/International2Adt1ChdRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-29</Date>" in body:
                file = open("providersimulation/avianca/International2Adt1InfOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-30</Date>" in body:
                file = open("providersimulation/avianca/International2Adt1InfRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-01-31</Date>" in body:
                file = open("providersimulation/avianca/International2Adt2Chd1InfOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-02-01</Date>" in body:
                file = open("providersimulation/avianca/International2Adt2Chd1InfRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-02-02</Date>" in body:
                file = open("providersimulation/avianca/International2Adt2ChdOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-02-03</Date>" in body:
                file = open("providersimulation/avianca/International2Adt2ChdRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-02-04</Date>" in body:
                file = open("providersimulation/avianca/International2AdtOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-02-05</Date>" in body:
                file = open("providersimulation/avianca/International2AdtRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-02-06</Date>" in body:
                file = open("providersimulation/avianca/International3Adt2Chd1InfOW.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-02-07</Date>" in body:
                file = open("providersimulation/avianca/International3Adt2Chd1InfRT.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-02-08</Date>" in body:
                file = open("providersimulation/avianca/InternationalOWConnectionFlight.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-02-09</Date>" in body:
                file = open("providersimulation/avianca/InternationalOWNonStopFlight.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-02-10</Date>" in body:
                file = open("providersimulation/avianca/InternationalRTConnectionFlight.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<Date>2030-02-11</Date>" in body:
                file = open("providersimulation/avianca/InternationalRTNonStopFlight.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info




#1
def getDates(data):
    regex = re.findall(r'[0-9]*-[0-9]*-[0-9]*', data)
    dateFrom = datetime.strptime(regex[0], '%Y-%m-%d')
    dateTo = datetime.strptime(regex[1], '%Y-%m-%d')
    if dateFrom > dateTo:
        dateFrom = datetime.strptime(regex.index(1), '%Y-%m-%d')
    return dateFrom - datetime.now()


class ApitudeHotelesSimulation:

    def ApitudeResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'application/json;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")

        #1r1a
        if '"rateKey": 10' in body:
            file = open("providersimulation/apitudehoteles/flow1r1a_searchresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        elif '"latitude": 11' in body:
            file = open("providersimulation/apitudehoteles/flow1r1a_searchresponse1.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

            ##1r2a1c
        elif '"latitude": 20' in body:
            file = open("providersimulation/apitudehoteles/flow1r2a1c_searchresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        elif '"latitude": 21' in body:
            file = open("providersimulation/apitudehoteles/flow1r2a1c_searchresponse1.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        ##1r2a2c
        elif '"latitude": 30' in body:
            file = open("providersimulation/apitudehoteles/flow1r2a2c_searchresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        elif '"latitude": 31' in body:
            file = open("providersimulation/apitudehoteles/flow1r2a2c_searchresponse1.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info


        ##1r2a_2r2a
        elif '"latitude": 40' in body:
            file = open("providersimulation/apitudehoteles/flow1r2a_2r2a_searchresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        elif '"latitude": 41' in body:
            file = open("providersimulation/apitudehoteles/flow1r2a_2r2a_searchresponse1.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info


        ##1r1a_2r2a1c
        elif '"latitude": 50' in body:
            file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_searchresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        elif '"latitude": 51' in body:
            file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_searchresponse1.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info


        ##1r2a2c_2r2a2c
        elif '"latitude": 60' in body:
            file = open("providersimulation/apitudehoteles/flow1r2a2c_2r2a2c_searchresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        elif '"latitude": 61' in body:
            file = open("providersimulation/apitudehoteles/flow1r2a2c_2r2a2c_searchresponse1.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info


        ##1r3a_2r4a
        elif '"rateKey": 70' in body:
            file = open("providersimulation/apitudehoteles/flow1r3a_2r4a_searchresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        elif '"rateKey": 71' in body:
            file = open("providersimulation/apitudehoteles/flow1r3a_2r4a_searchresponse1.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info


#check
        # 1r1a
        if '"rateKey": "10"' in body and '"language": null' in body:
            file = open("providersimulation/apitudehoteles/flow1r1a_checkresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        elif '"rateKey": "20"' in body  and '"language": null' in body:
            file = open("providersimulation/apitudehoteles/flow1r2a1c_checkresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info


        ##1r2a2c
        elif '"rateKey": "30"' in body  and '"language": null' in body:
            file = open("providersimulation/apitudehoteles/flow1r2a2c_checkresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info



        ##1r2a_2r2a
        elif '"rateKey": "40"' in body  and '"language": null' in body:
            file = open("providersimulation/apitudehoteles/flow1r2a_2r2a_checkresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info



        ##1r1a_2r2a1c
        elif '"rateKey": "50"' in body  and '"language": null' in body:
            file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_checkresponse.json", "r",
                        encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info



        ##1r2a2c_2r2a2c
        elif '"rateKey": "60"' in body  and '"language": null' in body:
            file = open("providersimulation/apitudehoteles/flow1r2a2c_2r2a2c_checkresponse.json", "r",
                        encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info



        ##1r3a_2r4a
        elif '"rateKey": "70"' in body  and '"language": null' in body:
            file = open("providersimulation/apitudehoteles/flow1r3a_2r4a_checkresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

#booking
        # 1r1a
        if '"rateKey": "10"' in body :
            file = open("providersimulation/apitudehoteles/flow1r1a_bookingresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        ##1r2a1c
        elif '"rateKey": "20"' in body  :
            file = open("providersimulation/apitudehoteles/flow1r2a1c_bookingresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info


        ##1r2a2c
        elif '"rateKey": "30"' in body  :
            file = open("providersimulation/apitudehoteles/flow1r2a2c_bookingresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info



        ##1r2a_2r2a
        elif '"rateKey": "40"' in body  :
            file = open("providersimulation/apitudehoteles/flow1r2a_2r2a_bookingresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info



        ##1r1a_2r2a1c
        elif '"rateKey": "50"' in body  :
            file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_bookingresponse.json", "r",
                        encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info



        ##1r2a2c_2r2a2c
        elif '"rateKey": "60"' in body  :
            file = open("providersimulation/apitudehoteles/flow1r2a2c_2r2a2c_bookingresponse.json", "r",
                        encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info



        ##1r3a_2r4a
        elif '"rateKey": "70"' in body  :
            file = open("providersimulation/apitudehoteles/flow1r3a_2r4a_bookingresponse.json", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

#cancel

# 1r1a
# file = open("providersimulation/apitudehoteles/flow1r1a_cancelresponse.json", "r", encoding='utf8')

##1r2a1c
#file = open("providersimulation/apitudehoteles/flow1r2a1c_aancelresponse.json", "r", encoding='utf8')

##1r2a2c
#file = open("providersimulation/apitudehoteles/flow1r2a2c_cancelresponse.json", "r", encoding='utf8')

##1r2a_2r2a
#file = open("providersimulation/apitudehoteles/flow1r2a_2r2a_cancelresponse.json", "r", encoding='utf8')

##1r1a_2r2a1c
#file = open("providersimulation/apitudehoteles/flow1r1a_2r2a1c_cancelresponse.json", "r",encoding='utf8')

##1r2a2c_2r2a2c
#file = open("providersimulation/apitudehoteles/flow1r2a2c_2r2a2c_cancelresponse.json", "r",encoding='utf8')

##1r3a_2r4a
#file = open("providersimulation/apitudehoteles/flow1r3a_2r4a_cancelresponse.json", "r", encoding='utf8')
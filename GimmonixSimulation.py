class GimmonixSimulation:

    def GimmonixResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")

        if "HotelsServiceSearchRequest" in body:
            if "<CheckIn>2020-01-01T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_3DayStay1Room1Adt.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckIn>2020-01-02T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_3DayStay1Room2Adt1Chd.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckIn>2020-01-03T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_3DayStay1Room2Adt1Inf.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckIn>2020-01-04T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_3DayStay1Room2Adt_2Room2Adt.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckIn>2020-01-05T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_3DayStay1Room1Adt_2Room2Adt1Chd.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckIn>2020-02-01T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_Refundable_3DayStay1Room1Adt.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckIn>2020-02-02T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_Refundable_3DayStay1Room2Adt1Chd.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckIn>2020-02-03T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_Refundable_3DayStay1Room2Adt1Inf.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckIn>2020-02-04T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_Refundable_3DayStay1Room2Adt_2Room2Adt.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckIn>2020-03-04T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_Refundable_3DayStay1Room2Adt_2Room2Adt-Copy.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckIn>2020-02-05T00:00:00</CheckIn>" in body:
                file = open("providersimulation/gimmonix/hotelSearch_Refundable_3DayStay1Room1Adt_2Room2Adt1Chd.xml","r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "HotelsSupplierDetailsRequest" in body:
            if "/110/127631/D20181212T214444/40a3513074ee49c6af2c25b4ae77968f" in body:
                file = open("providersimulation/gimmonix/hotelSupplierDetails_1Room1Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "/110/127631/D20181212T214843/83f0532f6c42451f98f87f51dd206d6e"  in body:
                file = open("providersimulation/gimmonix/hotelSupplierDetails_1Room2Adt1Chd.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "/110/127631/D20181212T215245/792f22a832624fbd95372744156eb9d4" in body:
                file = open("providersimulation/gimmonix/hotelSupplierDetails_1Room2Adt1Inf.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "/110/127631/D20181212T221715/c92583fe35d34159b927ad4afe08ab2d"  in body:
                file = open("providersimulation/gimmonix/hotelSupplierDetails_1Room2Adt_2Room2Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "/110/127631/D20181212T221715/c92583fe35d34159b927ad4afe08ab2f"  in body:
                file = open("providersimulation/gimmonix/hotelSupplierDetails_1Room2Adt_2Room2Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "/110/127631/D20181212T222007/527af9e839434fdeb78e6d5f44f80e08"  in body:
                file = open("providersimulation/gimmonix/hotelSupplierDetails_1Room1Adt_2Room2Adt1Chd.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "HotelPaymentPreferencesRequest" in body:
            if "<PackageID>8a2977d8-2d65-4dfd-a69a-aa566407e52c</PackageID>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room1Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<PackageID>0f67d4ec-06b4-4946-81a2-a86c127c7817</PackageID>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_NonRefundable_3DayStay1Room1Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            #
            if "<PackageID>093baf26-c7fe-4f4b-bfc8-13125492bb17</PackageID>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room2Adt1Chd.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<PackageID>2b69f8cb-2a8a-48dc-a0c4-404f0c179a9d</PackageID>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room2Adt1Inf.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<PackageID>8614c0d5-498e-456d-98a7-c298443ebfd4</PackageID>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room2Adt_2Room2Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<PackageID>8614c0d5-498e-456d-98a7-c298443ebfd4</PackageID>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room2Adt_2Room2Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<PackageID>8614c0d5-498e-456d-98a7-c298443ebfd9</PackageID>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room2Adt_2Room2Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<PackageID>8614c0d5-498e-456d-98a7-c298443ebfd5</PackageID>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room2Adt_2Room2Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<PackageID>663d2e7d-c9eb-4c8e-b99c-23c5e0f494f3</PackageID>" in body:
                file = open("providersimulation/gimmonix/cancelPolicies_3DayStay1Room1Adt_2Room2Adt1Chd.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "HotelBookRequest" in body:
            if "/110/127631/D20181212T214444/40a3513074ee49c6af2c25b4ae77968f" in body:
                file = open("providersimulation/gimmonix/successBooking_3DayStay1Room1Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "093baf26-c7fe-4f4b-bfc8-13125492bb17" in body:
                file = open("providersimulation/gimmonix/successBooking_3DayStay1Room2Adt1Chd.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "/110/127631/D20181212T215245/792f22a832624fbd95372744156eb9d4" in body:
                file = open("providersimulation/gimmonix/successBooking_3DayStay1Room2Adt1Inf.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            #if "8614c0d5-498e-456d-98a7-c298443ebfd4" in body:
            if "c6e43dbf-3ba1-4194-8a86-dac5f7d23345" in body:
                file = open("providersimulation/gimmonix/successBooking_3DayStay1Room2Adt_2Room2Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "663d2e7d-c9eb-4c8e-b99c-23c5e0f494f3" in body:
                file = open("providersimulation/gimmonix/successBooking_3DayStay1Room1Adt_2Room2Adt.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "00000000-0000-0000-0000-000000000000" in body:
                file = open("providersimulation/gimmonix/errorBooking.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "HotelBookCancelRequest" in body:
            if "3898604" in body:
                file = open("providersimulation/gimmonix/successBookingCancel.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "3898735" in body:
                file = open("providersimulation/gimmonix/successMultipleBookingCancel.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "111111" in body:
                file = open("providersimulation/gimmonix/onErrorBookingCancel.xml", "r",
                            encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

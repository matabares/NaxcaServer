class RtsSimulation:

    def RtsResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")


        if "HotelSearchListNetGuestCount" in body:
            # region Search
            if "<CheckInDate>2019-11-05</CheckInDate>"in body:
                file = open("providersimulation/rts/trelloSearch.xml",
                            # busqueda 1 adulto 1 dia destino bangkok
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-01-01</CheckInDate>" in body:
                file = open("providersimulation/rts/HotelSearch_3DayStay1Room1Adt.xml",
                            # busqueda 1 adulto 1 dia destino bangkok
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-01-02</CheckInDate>" in body:
                file = open("providersimulation/rts/HotelSearch_3DayStay1Room2Adt1Chd.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-01-04</CheckInDate>" in body:
                file = open("providersimulation/rts/HotelSearch_3DayStay1Room2Adt_2Room2Adt.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-01-05</CheckInDate>" in body:
                file = open("providersimulation/rts/HotelSearch_3DayStay1Room1Adt_2Room2Adt1Chd.xml",
                            # busqueda 1 adulto un cuarto, 2 adultos un niño en segundo cuarto destino bangkok
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-01-06</CheckInDate>" in body:
                file = open("providersimulation/rts/HotelSearch_3DayStay1Room2Adt1Inf.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-01-18</CheckInDate>" in body:
                file = open("providersimulation/rts/singleHotelSearch1adtBKK0001.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-02-01</CheckInDate>" in body or "<CheckInDate>2020-07-01</CheckInDate>" in body or "<CheckInDate>2020-06-12</CheckInDate>" in body:

                file = open("providersimulation/rts/hotelSearchVerify1adtBKK0001.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-02-02</CheckInDate>" in body or "<CheckInDate>2020-07-02</CheckInDate>" in body or "<CheckInDate>2020-07-12</CheckInDate>" in body:
                file = open("providersimulation/rts/hotelSearchVerify1Room2Adt1ChdBKK0001.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-02-04</CheckInDate>" in body or "<CheckInDate>2020-07-04</CheckInDate>" in body or "<CheckInDate>2020-07-14</CheckInDate>" in body or "<CheckInDate>2020-02-10</CheckInDate>" in body or "<CheckInDate>2020-02-20</CheckInDate>" in body:
                print("Search de 2adt en 2 cuartos")
                file = open("providersimulation/rts/hotelSearchVerify1room2adt2room2adtBKK0001.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-02-05</CheckInDate>" in body or "<CheckInDate>2020-07-05</CheckInDate>" in body or "<CheckInDate>2020-07-15</CheckInDate>" in body:
                file = open("providersimulation/rts/hotelSearchVerify1room1adt2room2adt1chd.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-02-11</CheckInDate>" in body:
                file = open("providersimulation/rts/hotelSearchVerify1adtBKK0001.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-02-12</CheckInDate>" in body:
                file = open("providersimulation/rts/hotelSearchVerify1Room2Adt1ChdBKK0001.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-02-14</CheckInDate>" in body:
                file = open("providersimulation/rts/hotelSearchVerify1room2adt2room2adtBKK0001.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-02-15</CheckInDate>" in body:
                file = open("providersimulation/rts/hotelSearchVerify1room1adt2room2adt1chd.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-02-16</CheckInDate>" in body:
                file = open("providersimulation/rts/hotelSearchSpecificCase1room1adt2room2adt1chd.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-02-17</CheckInDate>" in body:
                file = open("providersimulation/rts/hotelSearchVerifySpecificCase1room1adt2room2adt1chd.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info


        if "GetCancelDeadlineForCustormerCountResponse":
            if "<CheckInDate>2019-11-05</CheckInDate>"in body:
                file = open("providersimulation/rts/trelloCancelPolicies.xml",
                            # busqueda 1 adulto 1 dia destino bangkok
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-02-01</CheckInDate>" in body or "<CheckInDate>2020-07-01</CheckInDate>" in body or "<CheckInDate>2020-06-12</CheckInDate>" in body:
                file = open("providersimulation/rts/cancelPolicies1Adt.xml",
                            "r", encoding='utf8')
                data = file.read()
                print("2adt en 2 rooms")
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-02-02</CheckInDate>" in body or "<CheckInDate>2020-07-02</CheckInDate>" in body or "<CheckInDate>2020-07-12</CheckInDate>" in body:
                file = open("providersimulation/rts/cancelPolicies1room2adt1chd.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-02-04</CheckInDate>" in body or "<CheckInDate>2020-07-04</CheckInDate>" in body or "<CheckInDate>2020-07-14</CheckInDate>" in body or "<CheckInDate>2020-02-10</CheckInDate>" in body or "<CheckInDate>2020-02-20</CheckInDate>" in body:
                print("cancelPolicies de 2adt en 2 cuartos")
                file = open("providersimulation/rts/cancelPolicies1room2Adt_2Room2adt.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-02-05</CheckInDate>" in body or "<CheckInDate>2020-07-05</CheckInDate>" in body or "<CheckInDate>2020-07-15</CheckInDate>" in body or "<CheckInDate>2020-02-17</CheckInDate>" in body:
                file = open("providersimulation/rts/cancelPolicies1room1Adt_2Room2adt1chd.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-02-08</CheckInDate>" in body:
                file = open("providersimulation/rts/emptyCancellationPolicies.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-02-11</CheckInDate>" in body:
                file = open("providersimulation/rts/cancelPolicies_nonRefundable_1Room1Adt.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<CheckInDate>2020-02-12</CheckInDate>" in body:
                file = open("providersimulation/rts/cancelPolicies_nonRefundable_1Room2Adt1Chd.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-02-14</CheckInDate>" in body:
                file = open("providersimulation/rts/cancelPolicies_nonRefundable_1Room2Adt_2Room2Adt.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<CheckInDate>2020-02-15</CheckInDate>" in body:
                file = open("providersimulation/rts/cancelPolicies_nonRefundable_1Room1Adt_2Room2Adt1Chd.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        #region info
        if "GetHotelInformation" in body:
            if "<ItemCode>LAX0240</ItemCode>" in body:
                file = open("providersimulation/rts/infoTrello.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<ItemCode>BKK0001</ItemCode>" in body and "<LanguageCode>AR</LanguageCode>" in body:
                file = open("providersimulation/rts/HotelInfoEs.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<ItemCode>BKK0001</ItemCode>" in body and "<LanguageCode>BR</LanguageCode>" in body:
                file = open("providersimulation/rts/HotelInfoBr.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<ItemCode>BKK0001</ItemCode>" in body and "<LanguageCode>EN</LanguageCode>" in body:
                file = open("providersimulation/rts/HotelInfoEn.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<ItemCode>BKK0003</ItemCode>" in body:
                file = open("providersimulation/rts/HotelInfoNoAmmeintyDt02.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<ItemCode>BKK0002</ItemCode>" in body:
                if "<LanguageCode>EN</LanguageCode>" in body:
                    file = open("providersimulation/rts/HotelInfoBkk0002EN.xml",
                                "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

                if "<LanguageCode>AR</LanguageCode>" in body:
                    file = open("providersimulation/rts/HotelInfoBkk0002AR.xml",
                                "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

                if "<LanguageCode>BR</LanguageCode>" in body:
                    file = open("providersimulation/rts/HotelInfoBkk0002BR.xml",
                                "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

            if "<ItemCode>NOHOTELCODE</ItemCode>" in body:
                file = open("providersimulation/rts/HotelInfoError.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<ItemCode>MAD0327</ItemCode>" in body:
                if "<LanguageCode>EN</LanguageCode>" in body:
                    file = open("providersimulation/rts/infoOnErrorEn.xml",
                                "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

                if "<LanguageCode>AR</LanguageCode>" in body:
                    file = open("providersimulation/rts/infoOnErrorEs.xml",
                                "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

                if "<LanguageCode>BR</LanguageCode>" in body:
                    file = open("providersimulation/rts/infoOnErrorBr.xml",
                                "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

            if "<ItemCode />" in body:
                file = open("providersimulation/rts/HotelInfoHotelCodeIsMissing.xml",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
        #endregion
        #region booking
        if "CreateSystemBookingForGuestCount" in body:
            if "<AppliedFromDate>2019-11-05</AppliedFromDate>" in body:
                file = open("providersimulation/rts/trelloBookingRS.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<AppliedFromDate>2020-06-11</AppliedFromDate>" in body:
                file = open("providersimulation/rts/successBooking1Room1Adt.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "<AppliedFromDate>2019-07-02</AppliedFromDate>" in body:
                file = open("providersimulation/rts/successBooking1Room2Adt1Chd.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<AppliedFromDate>2019-07-04</AppliedFromDate>" in body:
                file = open("providersimulation/rts/successBooking1Room2Adt_2Room2Adt.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<AppliedFromDate>2019-07-05</AppliedFromDate>" in body:
                file = open("providersimulation/rts/successBooking1Room1Adt_2Room2Adt1Chd.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            # errorReservation
            if "<AppliedFromDate>2019-07-11</AppliedFromDate>" in body:
                file = open("providersimulation/rts/errorBooking1Room1Adt.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<AppliedFromDate>2019-07-12</AppliedFromDate>" in body:
                file = open("providersimulation/rts/errorBooking1Room2Adt1Chd.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<AppliedFromDate>2019-07-15</AppliedFromDate>" in body:
                file = open("providersimulation/rts/errorBooking1Room1Adt_2Room2Adt1Chd.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<AppliedFromDate>2019-07-16</AppliedFromDate>" in body:
                file = open("providersimulation/rts/successBooking1Room2Adt.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<AppliedFromDate>2020-02-10</AppliedFromDate>" in body:
                file = open("providersimulation/rts/bookingRigth.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<AppliedFromDate>2020-02-20</AppliedFromDate>" in body or "<AppliedFromDate>2020-06-12</AppliedFromDate>" in body or "<AppliedFromDate>2020-07-14</AppliedFromDate>" in body:
                file = open("providersimulation/rts/bookingWrong.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        #endregion
        #region cancel
        if "BookingCancel" in body:
            # Error Cancel
            if "<BookingCode>BUEF212724</BookingCode>" in body:
                file = open("providersimulation/rts/successBookingCancel.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<BookingCode>BUEF212722</BookingCode>" in body:
                file = open("providersimulation/rts/errorBookingCancel.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "<BookingCode>BUEF26535</BookingCode>" in body:
                file = open("providersimulation/rts/errorBookingCancel.xml", "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
        #endregion
        #region voucher
        if "GetBookingVoucher" in body:
            file = open("providersimulation/rts/bookingVoucher1Room2Adt_2Room2Adt.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            info.wfile.write(bytes(data, 'UTF-8'))
            return info

        #endregion
        #region Hotel Remarks
        if "GetRemarkHotelInformationForCustomerCount" in body:
            file = open("providersimulation/rts/RemarkHotelInformationRemarks.xml", "r", encoding='utf8')
            data = file.read()
            file.close()
            data = self.ReplaceValuesInGetRemarkHotelInformationForCustomerCountResponse(body, data)
            info.wfile.write(bytes(data, 'UTF-8'))
            return info
        #endregion
    #region method
    def ReplaceValuesInGetRemarkHotelInformationForCustomerCountResponse(self, body, responseData):
        try:
            from bs4 import BeautifulSoup
            parsedBody = BeautifulSoup(body, 'xml')
            itemCode = parsedBody.Body.GetRemarkHotelInformationForCustomerCount.HotelSearchListNetGuestCount.ItemCodeList.ItemCodeInfo.ItemCode.get_text()
            itemNo = parsedBody.Body.GetRemarkHotelInformationForCustomerCount.HotelSearchListNetGuestCount.ItemCodeList.ItemCodeInfo.ItemNo.get_text()
            roomTypeCode = parsedBody.Body.GetRemarkHotelInformationForCustomerCount.RoomTypeCode.get_text()
            responseData = str.replace(responseData, "{ITEM_CODE}", itemCode)
            responseData = str.replace(responseData, "{ITEM_NO}", itemNo)
            responseData = str.replace(responseData, "{ROOM_TYPE_CODE}", roomTypeCode)
            return responseData
        except Exception as e:
            return "<error>{}</error>".format(str(e))
    #endregion
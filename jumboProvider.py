import re
from datetime import datetime


class jumboProviderSimulation:

    def jumboResponse(self, info):

        info.send_response(200)
        info.send_header('Content-Type', 'text/xml; charset=utf-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")

        # Search
        if "availableHotelsByMultiQueryV22" in body:
            days = getDates(body).days
            print(days)

            if days == 20:
                file = open("providersimulation\jumbotours\HotelConnector_HotelSearch_AvailCostisOk.xml",
                            "r", encoding='utf8')
                return returnFile(file, info)

            if days == 33:
                file = open("providersimulation\jumbotours\HotelConnector_HotelSearch_ReturnNonRefundableHotel.xml",
                            "r", encoding='utf8')
                return returnFile(file, info)

            elif days == 34:
                file = open(
                    "providersimulation\jumbotours\JumboConnector_HotelSearch_HotelResponseOnlyOnRequestFalse.xml",
                    "r", encoding='utf8')
                return returnFile(file, info)

            elif days == 35:
                file = open(
                    "providersimulation\jumbotours\JumboConnector_HotelSearch_HotelResponseNoneAvailable.xml",
                    "r", encoding='utf8')
                return returnFile(file, info)

            elif days == 37:
                file = open(
                    "providersimulation\jumbotours\JumboConnector_HotelConfirm_HotelResponseCommentDates.xml",
                    "r", encoding='utf8')
                return returnFile(file, info)

            elif days == 38:
                file = open(
                    "providersimulation\jumbotours\JumboConnector_HotelConfirm_HotelResponseCommentDates.xml",
                    "r", encoding='utf8')
                return returnFile(file, info)

            elif days == 39:
                file = open(
                    "providersimulation\jumbotours\JumboConnector_HotelSearch_HotelInfoMustHaveHotelCodeCatCategoryDescription_Test.xml",
                    "r", encoding='utf8')
                return returnFile(file, info)


            elif days == 100:
                file = open(
                    "providersimulation\jumbotours\completeflow\HotelConnector_CompleteFlow_Search_test.xml",
                    "r", encoding='utf8')
                return returnFile(file, info)

        # Verify
        if "ValuationRQV22" in body:
            if days == 40:
                file = open("providersimulation\jumbotours\HotelConnector_HotelVerify_ReservationOk.xml", "r",
                            encoding='utf8')
                return returnFile(file, info)

            if days == 43:
                file = open(
                    "providersimulation\jumbotours\HotelConnector_HotelVerify_HotelVerifyChangeThePricesinTheVerify_Test.xml",
                    "r",
                    encoding='utf8')
                return returnFile(file, info)
            if days == 42:
                file = open(
                    "providersimulation\jumbotours\JumboConnector_HotelVerify_HotelRoomBookingMustHaveCancellationPolicies_Test.xml",
                    "r",
                    encoding='utf8')
                return returnFile(file, info)

            if days == 32:
                file = open("providersimulation\jumbotours\HotelConnector_HotelVerify_OfferAvailable_Test.xml",
                            "r", encoding='utf8')
                return returnFile(file, info)

            if days == 100:
                file = open("providersimulation\jumbotours\completeflow\HotelConnector_CompleteFlow_HotelVerify.xml",
                            "r",
                            encoding='utf8')
                return returnFile(file, info)
        # Confirm
        if "ConfirmExtendsRSV22" in body:
            if days == 100:
                file = open(
                    "providersimulation\jumbotours\completeFlow\HotelConnector_CompleteFlow_HotelConfirm_Test.xml", "r",
                    encoding='utf8')
                return returnFile(file, info)

        # Cancel
        if "CancelRSV22" in body:
            if '<basketId>7983293918</basketId>' in body:
                file = open("providersimulation\jumbotours\HotelConnector_HotelCancel_HotelCancelStatus_Test.xml", "r",
                            encoding='utf8')
                return returnFile(file, info)

            if '<basketId>7983293999</basketId>' in body:
                file = open("providersimulation\jumbotours\completeFlow\HotelConnector_CompleteFlow_HotelCancel_Test.xml", "r",
                            encoding='utf8')
                return returnFile(file, info)

        # Info
        if "EstablishmentDataRQV22" in body:
            if '<establishmentId>42085</establishmentId>' in body:
                file = open("providersimulation\jumbotours\HotelConnector_HotelInformation_DestinationIsNotChangedByConnector.xml", "r",
                            encoding='utf8')
                return returnFile(file, info)

            if '<establishmentId>828473</establishmentId>' in body:
                file = open("providersimulation\jumbotours\HotelConnector_HotelInformation_DestinationIsNotChangedByConnector2.xml", "r",
                            encoding='utf8')
                return returnFile(file, info)

        info.send_error(404, "File not found from JumboSimulation")


def getDates(data):
    regex = re.findall(r'[0-9]*-[0-9]*-[0-9]*', data)
    print(regex)
    dateFrom = datetime.strptime(regex[0], '%Y-%m-%d')
    dateTo = datetime.strptime(regex[1], '%Y-%m-%d')
    if dateFrom > dateTo:
        dateFrom = datetime.strptime(regex.index(1), '%Y-%m-%d')
    return dateFrom-datetime.now()


def returnFile(file, info):
    data = file.read()
    file.close()
    info.wfile.write(bytes(data, 'UTF-8'))
    return info

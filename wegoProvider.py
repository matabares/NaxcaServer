class wegoProviderSimulation:

    def wegoResponse(self, info):
            info.send_response(200)
            info.send_header('Content-Type', 'application/json; charset=utf-8')
            info.end_headers()

            if "hotels/v1/hotels" in info.path:

                if "258101" in info.path:
                    # HotelConnector_HotelInformation_HotelInfoAllImagesLoaded
                    file = open("providersimulation\wego\HotelConnector_HotelInformation_HotelCategoryOk.json",
                                "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

                if "258102" in info.path:
                    # HotelConnector_HotelInformation_HotelInfoAllImagesLoaded
                    file = open(
                        "providersimulation\wego\HotelConnector_HotelInformation_DestinationIsNotChangedByConnector.json",
                        "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

                if "258103" in info.path:
                    # HotelConnector_HotelInformation_HotelInfoAllImagesLoaded
                    file = open("providersimulation\wego\HotelConnector_HotelInformation_HotelInfoAllImagesLoaded.json",
                                "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return info

                if "258104" in info.path:
                    # HotelConnector_HotelInformation_HotelInfoAllImagesLoaded
                    file = open("providersimulation\wego\HotelConnector_HotelInformation_DescriptionMustExist.json",
                                "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return

                if "258105" in info.path:
                    # HotelConnector_HotelInformation_HotelInfoAllImagesLoaded

                    file = open("providersimulation\wego\HotelConnector_HotelInformation_HotelIsActive.json",
                                "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return

            if "metasearch/hotels/searches" in info.path:
                contentLen = int(info.headers.getheader('content-length', 0))
                postBody = info.rfile.read(contentLen)

                # HotelConnector_HotelSearch_HotelNameIsMandatory
                if "2033-03-11" in postBody:
                    file = open("providersimulation\wego\HotelConnector_HotelSearch_HotelNameIsMandatory_search.json",
                                "r", encoding='utf8')
                    data = file.read()
                    file.close()
                    info.wfile.write(bytes(data, 'UTF-8'))
                    return

            # HotelConnector_HotelSearch_HotelNameIsMandatory
            if "metasearch/hotels/searches/hotelnameismandatorytest/results" in info.path:
                file = open("providersimulation\wego\HotelConnector_HotelSearch_HotelNameIsMandatory_result.json",
                            "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return

            else:
                info.send_error(404,"File not found")
                return info
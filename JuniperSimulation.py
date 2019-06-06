class juniperProviderSimulation:

    def juniperResponse(self, info):
        info.send_response(200)
        info.send_header('Content-Type', 'text/xml;charset=UTF-8')
        info.end_headers()
        contentLen = int(info.headers['Content-Length'])
        postBody = info.rfile.read(contentLen)
        body = str(postBody, "utf-8")

        if "OTA_HotelAvail" in body:
                file = open(
                    "providersimulation/Juniper/1adtSearchMIA.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

        if "OTA_HotelBookingRule" in body:
            if ("d937LcVHhvAuBDSrfyF4t6/buu45BGMeiwhIdpZtnY5QT+IstmBhuOj9NP2St5RDyM3SZT4WRi7y6uHq1oPLT07dQptFLJAXCJogf/zrL2nyg5LBi22d1UeKi4AbSHSrhjD1AhRzb8S7VOup0Mz3swMjWtRuIkqmISy0Da28yCDHXVMVOP/fYVlVOAxi1JNwXBr+igqGNlae40v1WZic0+ntBGdYLvvBIuUq6lrYz6FNGsaV9duFFXjGGfGnx9NQyLqZlNuwoV6Wm74Vv5Z+gDlnUqQL8jl+LMXeQUYMTaQqxkzL+dgoRpJlevgaaFwumrkfqiSkoPRMXVkAsFEHTI0oWDqr5Xhy9OWM92/Ec/pUyHvQYDDQvhByE/svC5jkJxb6P2JbpDE5shXV4iRpJLy+XgWd0JFBZ953iU7joFhbCZLHdpZ9WYuVfla39ELA2mPRR7TwHEuPzOJxv4d/9SsZ1LTM4hf3MdYDU3Ez/YW8iigJ6qo0gj/5GRNqLLRRjOMKRrL3odHSvkbyvV9f+kivEpK4bO7A0eOlR+p7OQaQbog/PIlLKGuyQrfO90JXfXqJg0wc6/WASzuliIdaSNIQk65prQ9PeqNVcA1t2YY=" in body):
                file = open(
                  "providersimulation/Juniper/BookingRuleService.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if ("d937LcVHhvAuBDSrfyF4t6/buu45BGMeiwhIdpZtnY5V4LX1oYDOehxGOe3iXzhfu4SoK8RunfZNayK1M1xmpQKv7URa/rIWvp2Xl9Rv/eMeCfk7xekAFWI0AOhM9rdwcx3KggYi6uPp1Yj+LMMUSlYwg/1aAFGQdMjGvvZVl7wjjQngLpOHI/SGTf/NRMQcYb1zupfIaPnNCBQciOXRl3Wh+HQlhjKtoWFOGLNCu9QDYLxASJWcAagaYyBvs9urompo/gXsZpdQx7RWNdkfL0Ujv9Bcdv6qElXNNgS9E7pkVzp89xoMRz63DGCzN1zwVb59Ae0U96wNNMtpPEH2EfdTMtRLjWBo27HsaqWhJ01vZyobvhQqAQoGT1y5RskMwAJZ04hAnQoatDJFV1QWS2EnANCZcfBXRL/KTMW22FlvZC9aRlA1ZWcA8dCyuSLMOKB7yEWLe5XOtOCuqq4EvJX1zqKxVAjCkTlrXYItkmBDqtEO3npmi2E+lOQTz0fSnf5ufDhGk0jHx4279ZBrL5qGFHztmHROKU/TAcHk7Tz+LcmpN8yfTR2+ihq5vLqy" in body):
                file = open(
                    "providersimulation/Juniper/BookingRuleServiceBadDown.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if ("d937LcVHhvAuBDSrfyF4t6/buu45BGMeiwhIdpZtnY5QT+IstmBhuOj9NP2St5RDi4EdmHBOoXznPT20vhqr5g3HuMRlQigZL4Yerv/4MQD35ShNyao2slGmi3xXAJVVqmFjbXBQm85xSLdAszkELqcxPAmJljVMqIwkn3rCP+18h3RvbPcsGMdQm1LP3CCQ2ZirJLvECv+1zVweOYzIU/ks4hG0721JwbDi+qjF3Ncwofw/+hn82d0qpPObbdJPO/u3R8EDyPWV3Zvop/i7CmGSlnfqHbpRi63Mu0j9ZaB/wjFZo8FHUbiDOmCnraMSgZfIaZUVja02keL7T92NlP8mkmcjmuGGuEnRHNMx9TVBPK0DRNwE9iSsryasg+1fFpMMDxs2di86a56VA1HjIoNzwo2trFWGhDj+ZAT1H95dw+TQK876F4tIxd330un8+TdFe0Vvu1eWr0oKjQIZTUk+0yLNrsa7ViJcAErHQOU9M2NKfYNnnM+GkafiIFpyFZFLvnJscVARU53z+O7EVahPaaDdR4mLCYuwJB2/5FvH3EFyDZNMxY3I4Q6ztZi2" in body):
                file = open(
                    "providersimulation/Juniper/BookingRuleServiceBadUp.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if ("d937LcVHhvAuBDSrfyF4t6/buu45BGMeiwhIdpZtnY5V4LX1oYDOehxGOe3iXzhfu4SoK8RunfZNayK1M1xmpQKv7URa/rIWvp2Xl9Rv/eMeCfk7xekAFWI0AOhM9rdwcx3KggYi6uPp1Yj+LMMUSlYwg/1aAFGQdMjGvvZVl7wjjQngLpOHI/SGTf/NRMQcYb1zupfIaPnNCBQciOXRl3Wh+HQlhjKtoWFOGLNCu9QDYLxASJWcAagaYyBvs9ur/efH4S0h7sWC7HJu00rIr0zxX+c7N7a1iXho9a+yiA5CeIzsRUPt4LoSU4UBJ6r2AztntSFhNPQp0J41S5SLj7ts3b6xdY4vdUA3Nw+By2lW/ZTnajEJus5PY+wOmkn0bSXoJn5WYeSzmeqa75Kf1DP/1dvWuCWM7lsYGUPO3hlnmm0p/op4m473ccCBmpd7I66xd2025rH8yQTts6+7qat0AGv1w4Jv5BxDYBkwTyF0f1DP+aG8jO57l/yhFNX/vdbSskrSI6yEUtng0H25DVpJctYmqEz98ThYi6tNCZt2VPupXY2/nKaLlvBMaZyl" in body):
                file = open(
                    "providersimulation/Juniper/BookingRuleServiceGoodDown.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if ("d937LcVHhvAuBDSrfyF4t6/buu45BGMeiwhIdpZtnY5V4LX1oYDOehxGOe3iXzhfu4SoK8RunfZNayK1M1xmpQKv7URa/rIWvp2Xl9Rv/eMeCfk7xekAFWI0AOhM9rdwcx3KggYi6uPp1Yj+LMMUSlYwg/1aAFGQdMjGvvZVl7wjjQngLpOHI/SGTf/NRMQcYb1zupfIaPnNCBQciOXRl3Wh+HQlhjKtoWFOGLNCu9QDYLxASJWcAagaYyBvs9urompo/gXsZpdQx7RWNdkfL0Ujv9Bcdv6qElXNNgS9E7obnrA7Db00AzNeprS3qGm28rPmS0bz4r3y4QNBPmUTZd2P165TlACvx93UIHjheAS9oHzdUZsvstiWo+fXfmKvP+Uw8/ISDPFUg4EGqVbN+FltwTmEjiVFk9gAUy12G1uSi3oIAQRZ0azKPwZX1U2oUOOO7/haeIgnH6YZCrn+OQWw5XQ2WauJkSN5YL4NAyBtX1sOQ2aCMM3K8EnIyHPwvln/QTc1ujgliIzj9F5onqdnDAbZbH+AVBNeKh4ODwoeXkew+/aRIRzh7dFnJ4an" in body):
                file = open(
                    "providersimulation/Juniper/BookingRuleServiceGoodUp.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info


        if "OTA_HotelRes" in body:
            if "500" in body:
                file = open(
                    "providersimulation/Juniper/HotelRes.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "501" in body:
                file = open(
                    "providersimulation/Juniper/HotelResErrorDown.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info

            if "600" in body:
                file = open(
                    "providersimulation/Juniper/HotelResErrorUp.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "400" in body:
                file = open(
                    "providersimulation/Juniper/HotelResGoodDown.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
            if "499" in body:
                file = open(
                    "providersimulation/Juniper/HotelResGoodUp.xml",
                    "r", encoding='utf8')
                data = file.read()
                file.close()
                info.wfile.write(bytes(data, 'UTF-8'))
                return info
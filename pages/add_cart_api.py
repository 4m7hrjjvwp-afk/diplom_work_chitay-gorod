import requests
import allure

class CartApi:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.cart_url = f"{self.base_url}web/api/v1/cart/product"

    @allure.step("Добавление товара в корзину")
    def add_to_cart(self, product_id: int):
        payload = {
            "product_id": product_id
        }
        headers = {"Authorization":"Bearer {eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3ODM2NzQ0MTksImlhdCI6MTc4MzUwNjQxOSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImQyZmRkN2NkMzJjZWRmMTc3MmM5ZjhhMTllNDU3N2VkOGI2MGRkMGQ1NzE2N2QwMmQwN2Q2ZmYxZDExMGJlMWQiLCJ0eXBlIjoxMH0.G784FMMbeOdSnoByB-nXlkQS_vfKTuXDL27nMnjXhtBIi6sp1YtW6uZjaAKKroZziU-JO4SPbLBfxhEc0GFVuK0ibnCfu5Tt8ikfmjeS45TrZdkJ53iTwcXtWou_zqhbtlOR4KwSDPgs7C1_WKrMnsvFW7G23y4ssDzTVwE4g8fS0IPGHM6sqntb7gnCFZkeMp_XF0r0aU1fSXdV0_u2k-GH2GlNWoETCN7EAf73swAVy7ZsAGvVh1qPRDshQV7oGL3L9PwAFUXzga65xByyN4ejv26SCDRtX-Wgt7GkgkUttlvYAG-xQTMsK4wEOcF5PLPhy4uM4rVSflv85l0jaA}"}
                
        response = requests.post(self.cart_url, json=payload, headers=headers)
        return response
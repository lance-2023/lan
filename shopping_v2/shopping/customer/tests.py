from django.test import TestCase

# Create your tests here.
import requests
url = 'https://api.bigcommerce.com/stores/rmz2xgu42d/v2/customers'
headers = {'x-auth-token': 'ol999cchp7xq536507sq3pbjia3fi43', 'Accept': 'application/json'}
requests.post(url=url, data={
            "first_name": "yu",
            "last_name": "shu",
            "phone": "19022123315",
            "email": "yushu@qq.com",
            "_authentication": {
                "password": "lxy123456"
            },
            "company": "silk",
            "store_credit": 0,
            "registration_ip_address": "132.1.123.123",
            "customer_group_id": 0,
            "notes": "note",
            "tax_exempt_category": "nothing"
}, headers=headers)
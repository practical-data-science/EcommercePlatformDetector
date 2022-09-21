from ecommerce_platform_detector import detector
import pandas as pd

# Known platforms
urls = [
    'https://www.copperandbrass.net',  # Wix
    'https://codyblue.sellfy.store',  # Sellfy
    'https://graze.com',  # Shopify
    'https://www.swelluk.com',  # Magento
    'https://www.bensonsforbeds.co.uk',  # BigCommerce
    'https://www.huygens.fr/en/',  # PrestaShop
    'https://tails.com',  # Prismic
    'https://www.purelypetsupplies.com',  # WooCommerce
    'https://gretelny.com',  # Squarespace
    'https://shop.fieldmag.com',  # BigCartel
    'https://sockbroker.com',  # OpenCart
    'https://argoadventure.com',  # 3DCart
    'https://partswarehouse.com',  # Volusion
    'https://acmetools.com',  # Demandware
]

df = detector.get_platforms(urls, verbose=True)
print(df)

# Ecommerce Platform Detector

Ecommerce Platform Detector is a simple Python library that detects the ecommerce platform used by a website. It is designed to be used in web scraping projects, where you may be able to save time by scraping similar sites using the same code. For example, Shopify sites can be quickly scraped using my [Shopify Scraper](https://github.com/practical-data-science/ShopifyScraper) Python package.

### Usage
Simply pass a Python list of fully qualified URLs to the `get_platforms()` function, and it will check each site and try to identify the ecommerce platform used. Results are returned in a Pandas dataframe. 

```python
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

```

### Output
                                      url     platform
    11          https://argoadventure.com       3DCart
    9           https://shop.fieldmag.com    BigCartel
    4    https://www.bensonsforbeds.co.uk  BigCommerce
    13              https://acmetools.com   Demandware
    3             https://www.swelluk.com      Magento
    10             https://sockbroker.com     OpenCart
    5          https://www.huygens.fr/en/   PrestaShop
    6                   https://tails.com      Prismic
    1       https://codyblue.sellfy.store       Sellfy
    2                   https://graze.com      Shopify
    8                https://gretelny.com  Squarespace
    12         https://partswarehouse.com     Volusion
    0      https://www.copperandbrass.net          Wix
    7   https://www.purelypetsupplies.com  WooCommerce


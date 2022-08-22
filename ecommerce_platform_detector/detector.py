"""
Name: Ecommerce Platform Detector
Author: Matt Clarke
"""

import requests


def is_shopify(url):
    response = requests.get(f'{url}', timeout=5)

    if response.status_code == 200 and 'shopify' in response.text:
        return True
    else:
        return False


def is_bigcommerce(url):
    response = requests.get(f'{url}', timeout=5)

    if response.status_code == 200 and 'bigcommerce' in response.text:
        return True
    else:
        return False


def is_woocommerce(url):
    response = requests.get(f'{url}', timeout=5)

    if response.status_code == 200 and 'woocommerce' in response.text:
        return True
    else:
        return False


def is_magento(url):
    response = requests.get(f'{url}', timeout=5)

    if response.status_code == 200 and 'magento' in response.text:
        return True
    else:
        return False


def get_platform(url):

    if is_shopify(url):
        return 'shopify'
    elif is_bigcommerce(url):
        return 'bigcommerce'
    elif is_woocommerce(url):
        return 'woocommerce'
    elif is_magento(url):
        return 'magento'
    else:
        return 'unknown'


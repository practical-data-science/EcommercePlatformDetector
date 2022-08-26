"""
Name: Ecommerce Platform Detector
Author: Matt Clarke
"""

import requests


def is_shopify(url):
    try:
        response = requests.get(f'{url}', timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

        if response.status_code == 200 and 'shopify' in response.text:
            return True
        else:
            return False
    except Exception as e:
        return False


def is_bigcommerce(url):
    response = requests.get(f'{url}', timeout=5,  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

    if response.status_code == 200 and 'bigcommerce' in response.text:
        return True
    else:
        return False


def is_woocommerce(url):
    response = requests.get(f'{url}', timeout=5,  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

    if response.status_code == 200 and 'woocommerce' in response.text:
        return True
    else:
        return False


def is_magento(url):
    response = requests.get(f'{url}', timeout=5,  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

    if response.status_code == 200 and '/mage/' in response.text:
        return True
    else:
        return False


def is_prismic(url):
    response = requests.get(f'{url}', timeout=5,  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

    if response.status_code == 200 and 'prismic' in response.text:
        return True
    else:
        return False


def is_netsuite(url):
    response = requests.get(f'{url}', timeout=5,  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

    if response.status_code == 200 and 'netsuite' in response.text:
        return True
    else:
        return False


def is_prestashop(url):
    response = requests.get(f'{url}', timeout=5,  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

    if response.status_code == 200 and 'prestashop' in response.text:
        return True
    elif response.status_code == 200 and 'MyWishList' in response.text:
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
    elif is_prismic(url):
        return 'prismic'
    elif is_netsuite(url):
        return 'netsuite'
    elif is_prestashop(url):
        return 'prestashop'
    else:
        return 'unknown'


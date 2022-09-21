"""
Name: Ecommerce Platform Detector
Author: Matt Clarke
"""

import requests
import pandas as pd


def get_response(url):
    """Return the response object for a given URL.

    Args:
        url (str): The URL to check.

    Returns:
        requests.Response: The response object.
    """
    try:
        response = requests.get(f'{url}', timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
        return response
    except requests.exceptions.RequestException as e:
        return e


def is_shopify(response):
    """Return True if the URL is a Shopify store.

    Args:
        response (requests.Response): The response object.

    Returns:
        bool: True if the URL is a Shopify store, False otherwise.
    """

    if response.status_code == 200 and 'shopify' in response.text:
        return True
    else:
        return False


def is_bigcommerce(response):
    """Return True if the URL is a BigCommerce store.

    Args:
        response (requests.Response): The response object.

    Returns:
        bool: True if the URL is a BigCommerce store, False otherwise.
    """

    if response.status_code == 200 and 'bigcommerce' in response.text:
        return True
    else:
        return False


def is_woocommerce(response):
    """Return True if the URL is a WooCommerce store.

    Args:
        response (requests.Response): The response object.

    Returns:
        bool: True if the URL is a WooCommerce store, False otherwise.
    """

    if response.status_code == 200 and 'woocommerce' in response.text:
        return True
    else:
        return False


def is_magento(response):
    """Return True if the URL is a Magento store.

    Args:
        response (requests.Response): The response object.

    Returns:
        bool: True if the URL is a Magento store, False otherwise.
    """

    if response.status_code == 200 and '/mage/' in response.text:
        return True
    else:
        return False


def is_prismic(response):
    """Return True if the URL is a Prismic store.

    Args:
        response (requests.Response): The response object.

    Returns:
        bool: True if the URL is a Prismic store, False otherwise.
    """

    if response.status_code == 200 and 'prismic' in response.text:
        return True
    else:
        return False


def is_prestashop(response):
    """Return True if the URL is a Prestashop store.

    Args:
        response (requests.Response): The response object.

    Returns:
        bool: True if the URL is a Prestashop store, False otherwise.
    """

    if response.status_code == 200 and 'prestashop' in response.text:
        return True
    elif response.status_code == 200 and 'MyWishList' in response.text:
        return True
    else:
        return False


def is_wix(response):
    """Return True if the URL is a Wix store.

    Args:
        response (requests.Response): The response object.

    Returns:
        bool: True if the URL is a Wix store, False otherwise.
    """

    if response.status_code == 200 and 'wixstatic' in response.text:
        return True
    else:
        return False


def is_sellfy(response):
    """Return True if the URL is a Sellfy store.

    Args:
        response (requests.Response): The response object.

    Returns:
        bool: True if the URL is a Sellfy store, False otherwise.
    """

    if response.status_code == 200 and 'sellfy.com' in response.text:
        return True
    else:
        return False


def is_squarespace(response):
    """Return True if the URL is a Squarespace store.

    Args:
        response (requests.Response): The response object.

    Returns:
        bool: True if the URL is a Squarespace store, False otherwise.
    """

    if response.status_code == 200 and 'squarespace' in response.text:
        return True
    else:
        return False


def is_bigcartel(response):
    """Return True if the URL is a BigCartel store.

    Args:
        response (requests.Response): The response object.

    Returns:
        bool: True if the URL is a BigCartel store, False otherwise.
    """

    if response.status_code == 200 and 'bigcartel' in response.text:
        return True
    else:
        return False


def is_opencart(response):
    """Return True if the URL is a OpenCart store.

    Args:
        response (requests.Response): The response object.

    Returns:
        bool: True if the URL is a OpenCart store, False otherwise.
    """

    if response.status_code == 200 and 'OpenCart' in response.text:
        return True
    else:
        return False


def is_3dcart(response):
    """Return True if the URL is a 3dCart store.

    Args:
        response (requests.Response): The response object.

    Returns:
        bool: True if the URL is a 3dCart store, False otherwise.
    """

    if response.status_code == 200 and '3dcart' in response.text:
        return True
    else:
        return False


def is_volusion(response):
    """Return True if the URL is a Volusion store.

    Args:
        response (requests.Response): The response object.

    Returns:
        bool: True if the URL is a Volusion store, False otherwise.
    """

    if response.status_code == 200 and 'volusion' in response.text:
        return True
    else:
        return False


def is_demandware(response):
    """Return True if the URL is a Demandware store.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is a Demandware store, False otherwise.
    """

    if response.status_code == 200 and 'demandware' in response.text:
        return True
    else:
        return False


def get_platform(url):
    """Return the platform for a given URL.

    Args:
        url (str): The URL to check.

    Returns:
        str: The platform for the URL.
    """

    response = get_response(url)

    if is_shopify(response):
        return 'Shopify'
    elif is_bigcommerce(response):
        return 'BigCommerce'
    elif is_woocommerce(response):
        return 'WooCommerce'
    elif is_magento(response):
        return 'Magento'
    elif is_prismic(response):
        return 'Prismic'
    elif is_prestashop(response):
        return 'PrestaShop'
    elif is_wix(response):
        return 'Wix'
    elif is_sellfy(response):
        return 'Sellfy'
    elif is_squarespace(response):
        return 'Squarespace'
    elif is_bigcartel(response):
        return 'BigCartel'
    elif is_opencart(response):
        return 'OpenCart'
    elif is_3dcart(response):
        return '3DCart'
    elif is_volusion(response):
        return 'Volusion'
    elif is_demandware(response):
        return 'Demandware'
    else:
        return 'Unknown'


def get_platforms(urls, verbose=False):
    """Return the platforms for a list of URLs in a DataFrame.

    Args:
        urls (list): The URLs to check.
        verbose (bool): Whether to print the results.

    Returns:
        pandas.DataFrame: The platforms for the URLs.
    """

    df = pd.DataFrame(columns=['url', 'platform'])

    for url in urls:
        if verbose:
            print(f' - Checking {url}')

        row = {'url': url, 'platform': get_platform(url)}
        df = pd.concat([df, pd.DataFrame(row, index=[0])], ignore_index=True)
    return df.sort_values(by='platform')


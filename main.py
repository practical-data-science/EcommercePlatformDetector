from ecommerce_platform_detector import detector
import pandas as pd


urls = [

    # Swell Reptiles
    'https://www.internetreptile.com',
    'https://reptiles.swelluk.com',
    'https://www.reptilecentre.com',
    'https://www.thepetexpress.co.uk',
    'https://www.slitherinreptiles.com',
    'https://www.onlinereptileshop.co.uk',
    'https://www.bluelizardreptiles.co.uk',
    'https://www.exotic-pets.co.uk',
    'https://www.zillarules.com',
    'https://reptilesupply.com',

]

df = pd.DataFrame(columns=['url', 'platform'])

for url in urls:
    row = {'url': url, 'platform': detector.get_platform(url)}
    print(row)

    df = pd.concat([df, pd.DataFrame(row, index=[0])], ignore_index=True)

print(df.sort_values(by='platform'))


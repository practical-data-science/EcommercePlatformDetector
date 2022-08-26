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

    # Swell UK
    'https://www.swelluk.com',
    'https://www.pondkeeper.co.uk',
    'https://www.allpondsolutions.co.uk',
    'https://www.bradshawsdirect.co.uk',
    'https://www.fishkeeper.co.uk',
    'https://www.completeaquatics.co.uk',
    'https://www.rocketaquatics.co.uk',
    'https://www.pond-planet.co.uk',
    'https://www.realaquatics.co.uk',


    'https://www.swellpets.co.uk',
    'https://fetch.co.uk',
    'https://www.petsathome.com',
    'https://tails.com',
    'https://www.zooplus.co.uk',
    'https://www.monsterpetsupplies.co.uk',
    'http://www.petsdirect.co.uk',
    'https://www.therange.co.uk/pets',
    'https://www.pet-supermarket.co.uk',
    'https://www.petshop.co.uk',
    'https://www.purelypetsupplies.com',
    'https://www.viovet.co.uk'

]


df = detector.get_platforms(urls, verbose=True)
print(df)


from settings import dev

from apps.public.models import *

from decimal import Decimal

with open('tab_delimited_food_codes.txt') as f:
    for line in f:
        line = line.split('\t')
        if line[2] and line[2] != "Null" and line[2] != 'GI Value':
            #
            # try:
            #     Decimal(line[2])
            # except:
            #     print line[2]

            ingredient = Ingredient(name=line[1], glycemic_index=Decimal(line[2]))
            ingredient.save()
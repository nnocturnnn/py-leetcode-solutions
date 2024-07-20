import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    area = 3000000
    population = 25000000
    df = world[(world['population'] >= population) | (world['area'] >= area)]
    return df[['name', 'population', 'area']]
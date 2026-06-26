from src.preprocessing.loader import DatasetLoader

loader = DatasetLoader()

df = loader.merge()

print(df.head())

print(df.shape)
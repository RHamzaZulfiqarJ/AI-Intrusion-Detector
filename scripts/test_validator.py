from src.preprocessing.loader import DatasetLoader
from src.preprocessing.validator import DatasetValidator

loader = DatasetLoader()

df = loader.merge()

validator = DatasetValidator(df)

report = validator.run()

validator.export(report)

print(report)
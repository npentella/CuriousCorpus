from app import db
from app import Text
from sklearn.externals import joblib
import gc

#Train Data Set
training_collection = Text.query.filter_by(data_set = "train").all()

training_targets = []
training_text_collection = []

gc.disable()

for text in training_collection:
  training_targets.append(text.period_start_year)
  training_text_collection.append(text.text_content)

gc.enable()

save_training_text_collection = open("training_text_collection.pkl", "wb")
joblib.dump(training_text_collection, save_training_text_collection)
save_training_text_collection.close()

save_training_targets = open("training_targets.pkl", "wb")
joblib.dump(training_targets, save_training_targets)
save_training_targets.close()

#Test Data Set
testing_collection = Text.query.filter_by(data_set = "test").all()

testing_targets = []
testing_text_collection = []

gc.disable()

for text in testing_collection:
  testing_targets.append(text.period_start_year)
  testing_text_collection.append(text.text_content)

gc.enable()

save_testing_text_collection = open("testing_text_collection.pkl", "wb")
joblib.dump(testing_text_collection, save_testing_text_collection)
save_testing_text_collection.close()

save_testing_targets = open("testing_targets.pkl", "wb")
joblib.dump(testing_targets, save_testing_targets)
save_testing_targets.close()

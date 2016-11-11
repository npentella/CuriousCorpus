import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from sklearn import metrics

svm_tfidf_f = open("pickles/svm_tfidf_vect.pkl")
svm_tfidf_vectorizer = joblib.load(svm_tfidf_f)
svm_tfidf_f.close()

clf_f = open("pickles/svm_clf.pkl", "rb")
svm_clf = joblib.load(clf_f)
clf_f.close()

nb_tfidf_f = open("pickles/nb_tfidf_vect.pkl", "rb")
nb_tfidf_vectorizer = joblib.load(nb_tfidf_f)
nb_tfidf_f.close()

nb_clf_f = open("pickles/nb_clf.pkl", "rb")
nb_clf = joblib.load(nb_clf_f)
nb_clf_f.close()

rf_tfidf_f = open("pickles/rf_tfidf_vect.pkl", "rb")
rf_tfidf_vectorizer = joblib.load(rf_tfidf_f)
rf_tfidf_f.close()

rf_clf_f = open("pickles/rf_clf.pkl", "rb")
rf_clf = joblib.load(rf_clf_f)
rf_clf_f.close()

# text_f = open("pickles/testing_text_collection.pkl", "rb")
# testing_text = joblib.load(text_f)
# text_f.close()


# target_f = open("pickles/testing_targets.pkl", "rb")
# testing_targets = joblib.load(target_f)
# target_f.close()


def svm_predict(text_to_check):
  vectorized_text = svm_tfidf_vectorizer.transform(text_to_check)
  return  svm_clf.predict(vectorized_text)

def svm_predict_all():
  prediction = svm_predict(testing_text)
  accuracy = np.mean(prediction == testing_targets)
  confusion_matrix = metrics.confusion_matrix(testing_targets, prediction)
  return {'confusion_matrix': confusion_matrix, "accuracy": accuracy}


def rf_predict(text_to_check):
  vectorized_text = rf_tfidf_vectorizer.transform(text_to_check)
  return rf_clf.predict(vectorized_text)

def rf_predict_all():
  prediction = rf_predict(testing_text)
  accuracy = np.mean(prediction == testing_targets)
  confusion_matrix = metrics.confusion_matrix(testing_targets, prediction)
  return {'confusion_matrix': confusion_matrix, "accuracy": accuracy}

def nb_predict(text_to_check):
  vectorized_text = nb_tfidf_vectorizer.transform(text_to_check)
  return nb_clf.predict(vectorized_text)

def nb_predict_all():
  prediction = nb_predict(testing_text)
  accuracy = np.mean(prediction == testing_targets)
  confusion_matrix = metrics.confusion_matrix(testing_targets, prediction)
  return {'confusion_matrix': confusion_matrix, "accuracy": accuracy}

def predict(text_to_check):
  return {"svm": svm_predict(text_to_check)[0], "rf": rf_predict(text_to_check)[0], "mnb": nb_predict(text_to_check)[0]}

def predict_all():
  return {"rf": rf_predict_all(), "svm": svm_predict_all(), "nb": nb_predict_all()}

# prediction =  predict("dummy")
# print prediction['svm']
# nb: nb_predict(text_to_check), rf: rf_predict(text_to_check)

# print predict_all()

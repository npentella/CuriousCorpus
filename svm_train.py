from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.externals import joblib

print "Grabbing data..."

training_text_collection_f = open("training_text_collection.pkl", "rb")
training_text_collection = joblib.load(training_text_collection_f)
training_text_collection_f.close()

training_targets_f = open("training_targets.pkl", "rb")
training_targets = joblib.load(training_targets_f)
training_targets_f.close()

print("Vectorizing data...")

vectorizer = TfidfVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = "english",   \
                             max_features = 2500, \
                             min_df = 5, \
                             max_df = 0.5)

train_tfidf = vectorizer.fit_transform(training_text_collection)

save_vect = open("svm_tfidf_vect.pkl", "wb")
joblib.dump(vectorizer, save_vect)
save_vect.close()

clf = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5, random_state=42).fit(train_tfidf, training_targets)

save_clf = open("svm_clf.pkl", "wb")
joblib.dump(clf, save_clf)
save_clf.close()

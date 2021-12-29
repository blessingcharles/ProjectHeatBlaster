
import os

pwd = os.getcwd()

UA_FILE_PATH = f"{pwd}/blasterModels/user_agents_models"
UA_ML_MODELS = {
    "LogisticRegression":"lg_cv_pipe.pkl",
    "SupportVectorClassifier":"svc_cv_pipe.pkl",
    "KnearestNeighbours":"knn_cv_pipe.pkl",
    "DecisionTreeClassifier":"dtc_cv_pipe.pkl",
    "MultinomialNaiveBayes":"mnb_cv_pipe.pkl"  ,
    "RandomForest":"rfc_cv_pipe.pkl"
}


PAYLOADS_FILE_PATH = f"{pwd}/blasterModels/payloads_models"
PAYLOADS_ML_MODEL = {
    "LogisticRegression":"lg_cv_pipe.pkl",
    "SupportVectorClassifier":"svc_cv_pipe.pkl",
    "KnearestNeighbours":"knn_cv_pipe.pkl",
    "DecisionTreeClassifier":"dtc_cv_pipe.pkl",
    "MultinomialNaiveBayes":"mnb_cv_pipe.pkl"  ,
    "RandomForest":"rfc_cv_pipe.pkl"
}
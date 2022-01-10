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
    #nltk models
    "LogisticRegression":"lg_cv_pipe.pkl",
    "SupportVectorClassifier":"svc_cv_pipe.pkl",
    "KnearestNeighbours":"knn_cv_pipe.pkl",
    "DecisionTreeClassifier":"dtc_cv_pipe.pkl",
    "MultinomialNaiveBayes":"mnb_cv_pipe.pkl"  ,
    "RandomForest":"rfc_cv_pipe.pkl",

    # feature models
    "LogisticRegressionCustomFeature":"lg_feature_model.pkl",
    "SupportVectorClassifierCustomFeature":"svc_feature_model.pkl",
    "KnearestNeighboursCustomFeature":"knn_feature_model.pkl",
    "DecisionTreeClassifierCustomFeature":"dtc_feature_model.pkl",
    "MultinomialNaiveBayesCustomFeature":"mnb_feature_model.pkl"  ,
    "RandomForestCustomFeature":"rfc_feature_model.pkl",

}
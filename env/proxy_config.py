import os

user_home_dir = os.path.expanduser("~") 

# create new blaster directory if not exist
isExist = os.path.exists(f"{user_home_dir}/blaster")

if not isExist:
    os.makedirs(f"{user_home_dir}/blaster")

LOGFILE_CONFIG = {
    "info_logfilepath":f"{user_home_dir}/blaster/info.log",
    "error_logfilepath":f"{user_home_dir}/blaster/error.log",
    "warning_logfilepath":f"{user_home_dir}/blaster/warning.log",
    "critical_logfilepath":f"{user_home_dir}/blaster/critical.log"
}

ROASTING_ML_MODELS = {
    "user-agents":"SupportVectorClassifier",
    "payloads":"MultinomialNaiveBayesCustomFeature"
}

UPSTREAM_BACKENDSERVERS = [ 
    "http://localhost:5000"
]



## INTRODUCTION :

Heat Blaster is a reverse proxy which can act as a load
balancer and web application firewall , which is powered by the ML
model to detect malicious http requests and prevent it by reaching the
backend servers. The web application firewall is developed in a
layered architecture , each layer has a ML model which has its own
functionality to analyse the http request and forward it to the next
layer. As the WAF follows layered architecture so we can enable or
disable any layer according to our wish. The proxy server also logs
both normal and malicious request information in log files for future
analysis. The load balancer in the reverse proxy is implemented in
round robin fashion and it also keeps a log file for uptime for each
backend server.

### Reverse Proxy :

A Reverse Proxy Server, sometimes also called a reverse proxy web server, often a
feature of a load balancing solution, stands between web servers and users, similar to a forward
proxy. However, unlike the forward proxy which sits in front of users, guarding their privacy, the
reverse proxy sits in front of web servers, and intercepts requests. In other words, a reverse
proxy acts on behalf of the server, while a proxy acts for the client.

A reverse proxy server acts like a middleman, communicating with the users so the
users never interact directly with the origin servers. It also balances client requests based on
location and demand, and offers additional security.

Benefits of reverse proxy servers include:

```
● load balancing
● caching content and web acceleration for improved performance
● more efficient and secure SSL encryption, and
● protection from DDoS attacks and web application firewall
```
### Web application Firewall

A WAF or web applicationfirewall helps protect webapplications by filtering and
monitoringHTTP traffic between a web applicationand the Internet. It typically protects web
applications from attacks such ascsrf,xss, fileinclusion, andsql injection, among others. A
WAF is a protocollayer 7 defense (in the osi model),and is not designed to defend against all
types of attacks. This method of attack mitigation is usually part of a suite of tools which
together create a holistic defense against a range of attack vectors.

By deploying a WAF in front of a web application, a shield is placed between the web
application and the Internet. While a proxy server protects a client machine’s identity by using
an intermediary, a WAF is a type ofreverse proxy,protecting the server from exposure by
having clients pass through the WAF before reaching the server.


### BLOCK DIAGRAM


### ARCHITECTURE DIAGRAM


### Complete Flow

Thehttp requestsendbytheuserisfirstprocessedbyeachlayerin

the webapplicationfirewall.Allthese modelsare highlyconfigurable like
whichalgorithmtouse,oralayercanbecompletelydisabledasperwish
of the developer.

The Two Layers of WAF :
1) User Agent Classifier
2) Payloads Detector

**User Agent Classifier** :

The first ml model is used to analyze theuser agent ofthe

request andclassifyit,iftherequestisgeneratedbyanormalbrowserit
contains a user agent which follows from standardization , if it is
generated by various security tools(sqlmap) orautomatedbots wecan
capture therequestandblockit.Sothemlmodelcanclassify between
iftheuseragentismaliciousornot.Sinceuseragentscan beforgedby
hackers , it is not completely fool proof but it can protect from script
kiddies and roast the request in the first layer itself.

### Payload Predictor :

Thesecond MLmodel is used to analysethe inputsgivenby the

usersfromhttpparameters,queryandhttpPOSTrequestbody, classify
themifitisanormalinputgivenbytheuserorifitisa maliciouspayload


from the hackers. The ML model is trained with malicious payload
vectorsforxss,sql,nosql,ssrf,xxeattacks.So theMLmodelisable
to classify normal requests from malicious requests. The malicious
requestsareroastedinthislayerandonly normalrequestsareservedto
the backend.

**Overall Algorithm**

Get http data as input to reverse proxy :

```
Bog = CountVectorizer(user-agent);
If user_agent_model(Bog) is malicious:
Block_request();
Else :
Payload = feature_extractor(user_input);
If payload_model(Payload) is malicious:
Block_request();
Else:
Route_request()
Load_Balance(backend_servers);
```

### ML models Algorithms Available

```
The developer can configure which dumped model should be used in
```
production environment by changing in the environment variable of the reverse

proxy application. The classification algorithms supported are

1) Support Vector Classifier

2) Logistic Regression

3) Decision Tree

4) Multinomial Naïve Bayes

5) Random Forest

## MODULES OVERVIEW

### Tree View of modules

#### .

├── blasterDB
├── blasterModels
│ ├── payloads_models
│ └── user_agents_models
├── env
├── heatblaster
│ ├── build


│ ├── data_collection
│ ├── datasets
│ ├──ml_notebooks
├── README.md
├── requirements.txt
├── ReverseProxy
│ ├── load_balancer
│ ├── mod_request_handlers
│ ├── mod_roaster
│ ├── templates
│ └── utils
├── run.py

**Reverse Proxy module** :

```
It’s the Core module which co-operates the load balancing , routing and the
```
web application firewall where the layers of ml model presents.

It further consists of sub modules

```
1) load_balancer : contains logic of how to load balance among the backend
```
servers

```
2) mod_request_handlers : contains logic of how to route requests
3) mod_roaster : contains the layers of web application firewall
4) templates : html templates for the reverse proxy
5) utils : utility functions for all sub modules
```

HEAT BLASTERMODULE

```
It contains all the Machine Learning Model training functions and preprocessing
```
steps in jupyter notebook. From here only ml models are dumped using joblib library

, then they are loaded into reverse proxy according to environmental configurations

mentioned by the developer.

### BlasterDb :

```
It contains all the data needed for the reverse proxy , which actually acts
```
similar to database to all the modules.

### ENV :

```
It contains all the environment variables for configuring the reverse proxy , the
```
configs are httpconfig , proxyconfig , mlconfig , serverconfig.

### Blaster Models :

```
It contains all the dumped ml model in two different sub directories of
1) payload models
2) user agents models
```

The different Ml models available for each layer:

User Agent Classifier(Layer 1) :

```
i) Count Vectorizer models
```
Payload Predictor

```
i) Custom Feature extraction (like special characters etc)
ii) Count Vectorizer models
```
### LIST OF MODELS


## Machine Learning in the Reverse Proxy

The heat blaster modules contains the jupyter notebooksof the
machine learning models where the preprocessing steps and training of the
model occurs. The trained model are then dumped into blasterModels directory ,
from where they can be loaded into the reverse proxy , which acts to filter out
malicious requests.

Datasets Collection

### User Agents Dataset

```
Common Browsers Dataset:
All common user agents names are collected from various github pages
```
1) https://gist.github.com/pzb/b4b6f57144aea7827ae

2)https://raw.githubusercontent.com/yusuzech/top-50-user-agents/master/user_agent.csv

3) https://www.networkinghowtos.com/howto/common-user-agent-list/

4) https://github.com/N0taN3rd/userAgentLists

Malicious Tools Dataset :


1) https://github.com/herrbischoff/user-agents/tree/master/data

**Payloads Dataset**

Common Payloads :

1) https://www.kaggle.com/dhruvildave/google-trends-dataset

Malicious Payloads :

1) https://github.com/payloadbox/xss-payload-list

2)https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side

%20Request%20Forgery

3)https://github.com/foospidy/payloads

```
All the Combined datasets can be found in the project url
```
https://github.com/blessingcharles/ProjectHeatBlaster

Preprocessing Steps :

UserAgents Model Preprocessing Steps

The useragent is extracted from the http headersof the http request
which is then converted into bag of words using countvectorizer.

CountVectorizer tokenizes ( tokenization means dividing the sentences
in words) the text along with performing very basic preprocessing. It


removes the punctuation marks and converts all the words to lowercase.
The vocabulary of known words is formed which is also used for encoding
unseen text later. The vocabulary of known words is formed which is also
used for encoding unseen text later.

**CountVectorizer** is a great tool provided by the scikit-learnlibrary in
Python. It is used to transform a given text into a vector on the basis of the
frequency (count) of each word that occurs in the entire text. This is helpful
when we have multiple such texts, and we wish to convert each word in
each text into vectors

### Preprocessing Steps :

The normal payloads inputs are collected from google trends
dataset from kaggle and the malicious payloads are collected from different
payloads of xss , sql , ssrf , xxe attacks used by security researchers and
pentesters in the wild. There are two types of feature extraction is done in
the payload data , the first one is similar to the previous user agent model
ie. count vectorizer and the second one is getting the characters count
which are not normally found in normal user inputs.

The custom Features are

```
1.Length
2.Nonprintable_keywords
3.Special_chars
4.Punctuation_chars
5.Js_events
6.Html_tags
7.Sql_keywords
8.Percentage_count
9. spaces_count
```



The developer can configure any models from thesenlp
preprocessing and custom feature preprocessing models in the reverse
proxy , as all the 6 classification algorithms are trained in this two different
datasets which leads to 12 different models available for the developer to
choose.


### Training the models

As there are 18 models to train , 6 models for user agents , 6 count vectorizer models for
payloads and 6 custom feature payload models to train .The algorithm are imported from
sklearn library and they are dumped using joblib library. The classification algorithms used in
the project are

1. Support vector classifier
2. Logistic Regression
3. K nearest neighbours
4. Decision Tree
5. Random Forest
6. Multinomial Naive Bayes

### Hyper Parameter Tuning

In machine learning, hyperparameter optimization or tuning is the problem of choosing a
set of optimal hyperparameters for a learning algorithm. A hyperparameter is a parameter
whose value is used to control the learning process. By contrast, the values of other parameters
(typically node weights) are learned.


Since it will takes lot of slides , the results can be seen in the project github
https://github.com/blessingcharles/ProjectHeatBlaster

### Model Evaluation Metrics 
##### all evaluation metrics can be found in heatblaster directory (jupyter notebooks) 

## REFERENCE PAPERS

1) Web Application Attacks Detection Using Machine Learning Techniques
https://ieeexplore.ieee.org/document/8614199

2) Development of a hybrid web application firewall to prevent web based
attacks
https://ieeexplore.ieee.org/document/7035910



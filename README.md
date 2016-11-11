# CuriousCorpus
## Purpose
CuriousCorpus is an algorithmic solution to identify the period of origin of an inputted passage of text using Natural Language Processing and machine-learning.

Leveraging the Guttenberg corpora and Scikit-learn libraries, we implemented three models: Naive Bayes, Support Vector Machine and Random Forest classifier. Through the training of our models, we were able to improve accuracy rates from as low as 38% to 81%.

We provide a simple web app to quickly input text and view predictions from each model, however, the strength of this project lies in the backend processing rather than a user interface.




## Dependencies
* click==6.6
* Flask==0.11.1
* itsdangerous==0.24
* Jinja2==2.8
* MarkupSafe==0.23
* numpy==1.9.2
* scikit-learn==0.18
* scipy==0.15.1
* sklearn==0.0
* Werkzeug==0.11.11
* gunicorn==19.6.0

##Configuration Instructions

1. Activate your environment
 ```{r, engine='bash'}
   $ source env/bin/activate
 ```

2. Install all dependencies
 ```{r, engine='bash'}
 $ pip install -r requirements.txt
 ```


3. Start virtual environment
 ```{r, engine='bash'}
$ echo "source `which activate.sh`" >> ~/.bashrc
$ source ~/.bashrc
 ```

4. Run app_settings variable
 ```{r, engine='bash'}
  $ export APP_SETTINGS="config.DevelopmentConfig"
```



##Contributors
* Nicolas Pentella - [@npentella](https://github.com/npentella)
Rachael Lunney - @rakaloo
Molly Fitzharris - @mfitzharris
Laura Moreno - @lauframo

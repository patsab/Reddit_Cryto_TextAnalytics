# Get data about Crypto
## Usage
### Prerequisits
Install dependencies with:  
```pip3 install requirements.txt```  

Add data for authentification. A reddit account is needed and an application which can be created under (https://www.reddit.com/prefs/apps "Reddit Apps").  
The config needs to be saved as 'reddit_auth_config.py'

### Run
```python3 scrape_reddit.py```  
The folder for the output ../data should be created if not existing

### Test
To check if the database was created correctly, the 'test_db.py' can be used  
```python3 test_db.py```
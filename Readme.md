# Self-Hosted_LLM
Start hosting your own Large Language model like ChatGPT or bard server for free

## Getting Stated

Download [python](https://www.python.org/downloads/)
Not sure how to download [Guide to install python on windows](https://www.simplilearn.com/tutorials/python-tutorial/python-installation-on-windows)

> Open your favorite command line tool inside the location where you have downloaded the files

> Make sure you have python installed
```
python --version
```

Install requirments (This requirments will work on CPU only, if you know what you are doing feel free to install GPU version)
```
pip install -r requirements.txt
```

## Generate API Key (It's free)
Go to [MakerSuite](https://makersuite.google.com/app/apikey)

> Copy the API Key and paste the newly created API Key in line 9 of LocalLLM.py file without the angle brackets <>

Example:
```
APIKEY = 'AAA111222333qwerty'
```

> Provide a convenient location in line 10 where the models are stored locally

Example:
```
os.environ['TRANSFORMERS_CACHE'] = r'D:\HuggingFaceModels'
```

### [Optional]Generate self signed certificates

> Open gitbash and run the command

```
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365
```

follow the instruction and fill up the run.bat file

> This is totally optional if you don't want to add self-signed certificate edit the run.bat and change it to following command instead:

```
streamlit run LocalLLM.py --server.port 5000
```

# Python Console Chat
This repository has a simple chat to ask to the SoldAI's Artificial Intelligenge using a python console applicattion.

## Install
Simply clone this repository using:
```bash
    git clone https://github.com/SoldAI/python-console-chat.git
```

Change to the repository directory and execute the python file included:
```bash
    cd python-console-chat
    python python-console-chat.py
```

## Use
Simply ask questions in spanish about SoldAI company. To end the program just give an enter with no text.

## Customize
To ask to your own bot change the lines 4 and 5 to include the correct service URL, and your bot key. You can see the versions of the service URL in [https://api.soldai.com/versions/](https://api.soldai.com/versions)
```python
serviceurl = 'http://www.soldai.com/hermes/api/v2/hacerpregunta?'
key='key=f56b11cc51bc8cb9643ebc9139ba45a411b94ac6'
```

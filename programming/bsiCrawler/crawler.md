#BSI Crawler
### Install scrapy for python3
    pip3 install scrapy
###How to start the crawler
    scrapy runspider crawli.py
###JSON Format for components
````javascript
{ "h1": "Title",

  "description":{
    "h2": "Title",  
    "content":[
      "Text1",
      "Text2",
      ...
      ]
    }
    
   "recommandations":{
        "h2": "Title",
        "subheaders":[ 
            { 
                "h3": "Title",
                "content": [
                    "Text1",
                    "Text2",
                    ...
             ]
            },
            ...
           ]
    }
  }
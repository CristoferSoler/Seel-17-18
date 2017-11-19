#BSI Crawler
### Install needed software for the crawler 
     python3: apt-get install python3.6
     pip3: sudo apt-get -y install python3-pip
     pip3: install scrapy
###How to start the crawler
    scrapy runspider crawli.py
###JSON Format for components
````json
{ "h1": "Title",
  "description":{
    "h2": "Title",  
    "content":[
      "Text1",
      "Text2"
      ]
    },
    
   "recommandations":{
        "h2": "Title",
        "subheaders":[ 
            { 
                "h3": "Title",
                "content": [
                    "Text1",
                    "Text2"
             ]
            }
           ]
    }
  }
  
 ````
 
 ####JSON Format for Threads und Counter Measures
 ````json
{ "h1": "Title",
  "description":{
    "h2": "Title",  
    "content":[
      "Text1",
      "Text2"
      ]
    },
    
   "recommandations":{
        "h2": "Title",
        "subheaders":[ 
            { 
                "h3": "Title",
                "content": [
                    "Text1",
                    "Text2"
             ]
            }
           ]
    }
  }
  
 ````
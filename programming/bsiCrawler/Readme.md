    This Python program is able to crawl and translate the contents of the 
    BSI Compendium into English. The scrapy library was used for crawling and googleTrans
    for translating. The selected output format is Markdown. 
### Overview
    main.py start the progress
    crawli.py fetch all the bsi content
    crawliTree.py fetch the treeview 
    translatorMultiProcessing.py translate the bsi content into md files
### Software for the crawler 
     python3: apt-get install python3.6
     pip3: sudo apt-get -y install python3-pip
     pip3: install scrapy
     pip3 install progressbar2
     pip3 install googletrans
###How to start
     python3 main.py
    
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
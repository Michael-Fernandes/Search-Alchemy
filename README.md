# Search Alchemy: Your Searches Over Time 

Search Alchemy uses [IBM's Alchemy API](https://console.ng.bluemix.net/catalog/services/alchemyapi "Alchemy API")  to analyze [Google User Search Queries](https://history.google.com/history/?utm_source=help "Download Google User Search Data").
V. 1.2

Ever catch yourself google an obscurely urgent topic, "How to peel a frozen banana?". Or maybe you've gone through a brief fascination with the latest dance trend, "How do you whip? and why do you nay nay?". Undoubtedly what we search is reflective of who we are, at least at that moment. Like us, what we Google changes. 

Search Alchemy creates personality insights from Google User Search Data, by providing visualizations of the type of sentiments included in Google Searches and how those searches change over time.

The files included in this respository use [Google User Data](https://history.google.com/history/?utm_source=help "Download Google User Search Data") and [IBM's Watson Cognitive Analytics API](https://console.ng.bluemix.net/catalog/services/alchemyapi "Alchemy API") to create personality insights.

![Graphs](https://drive.google.com/file/d/0B4-9LU1LGdnVOHZlUkRWaGhaWkU/view?usp=sharing)

##Installation:
	Requirements
		Writen with python 2.7
		IBM bluemix account-
			Signing up for a bluemix account is free. googleSearch.py uses the IBM Alchemy API which allows for up to 100 queries a month. This is not a lot of queries, but should suffice for personal use. 
		Google Account Search Data-
			To download your google search data follow the directions at this link:
			https://support.google.com/websearch/answer/6068625?hl=en



1. If you haven't already, download your Google User Search Data.
2. Make sure that googleSearch.py and reStructure.py are placed in the same directory as the Google Data.
3. If you havn't already update your bluemix account information in googleSearch.py
4. Run googleSearch.py

Note: The Alchemy API allows up to 200 free calls a month. This should be fine for 3-4 user's data.


Like what you see or want to find out more? Contact Michael at mfern93@gmail.com

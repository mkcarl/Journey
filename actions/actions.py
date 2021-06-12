# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import json
import matplotlib.pyplot as plt
from datetime import datetime as dt
from bs4 import BeautifulSoup
from requests_html import HTML, HTMLSession
#

def graph_pie(total, paid, id):
	outstanding = total - paid
	labels = ['Paid', 'Outstanding']
	size= [paid, outstanding]
	explode = (0, 0.1)
	fig1, ax1 = plt.subplots()
	ax1.pie(size, explode = explode, labels = labels, shadow=True, startangle=90)
	ax1.axis('equal')
	plt.legend(labels)
	plt.imsave(f"./images/{id}")



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        most_recent_state = tracker.current_state()
        print(most_recent_state["sender_id"])
        dispatcher.utter_message(
            template="utter_helloworld", 
            example_text="testing from custom action"
            )

        return []

class ActionEligibilityBussSec(Action):

    def name(self) -> Text:
        return "action_eligibility_buss_sec"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = tracker.latest_message["text"]
        return [SlotSet("buss_sec", msg)]
        
class ActionEligibilityOperation(Action):

    def name(self) -> Text:
        return "action_eligibility_operation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = tracker.latest_message["text"]
        return [SlotSet("operation", msg)]
        
class ActionEligibilityAnnRev(Action):

    def name(self) -> Text:
        return "action_eligibility_ann_rev"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = tracker.latest_message["text"]
        return [SlotSet("ann_rev", msg)]

class ActionEligibilityFacility(Action):

    def name(self) -> Text:
        return "action_eligibility_facility"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = tracker.latest_message["text"]
        return [SlotSet("facility", msg)]

class ActionEligibilityFacility(Action):

    def name(self) -> Text:
        return "action_eligibility_facility"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = tracker.latest_message["text"]
        return [SlotSet("facility", msg)]

class ActionEligibilityShareholder(Action):

    def name(self) -> Text:
        return "action_eligibility_shareholder"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = tracker.latest_message["text"]
        return [SlotSet("shareholder", msg)]

class ActionEligibilityForeign(Action):

    def name(self) -> Text:
        return "action_eligibility_foreign"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = tracker.latest_message["text"]
        return [SlotSet("foreign", msg)]

class ActionEligibilityFacility(Action):

    def name(self) -> Text:
        return "action_eligibility_facility"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = tracker.latest_message["text"]
        return [SlotSet("facility", msg)]

class ActionEligibilityGuarantorAge(Action):

    def name(self) -> Text:
        return "action_eligibility_guarantor_age"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = tracker.latest_message["text"]
        return [SlotSet("guarantor_age", msg)]

class ActionEligibilityPartnership(Action):

    def name(self) -> Text:
        return "action_eligibility_partnership"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = tracker.latest_message["text"]
        return [SlotSet("partnership", msg)]

class ActionEligibilityPartnership(Action):

    def name(self) -> Text:
        return "action_eligibility_immediate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = tracker.latest_message["text"]
        return [SlotSet("immediate", msg)]

class ActionPrintSlot(Action):

    def name(self) -> Text:
        return "action_print_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slot = {
            "buss_sec" : tracker.get_slot("buss_sec"), 
            "operation" : tracker.get_slot("operation"), 
            "ann_rev" : tracker.get_slot("ann_rev"), 
            "facility" : tracker.get_slot("facility"),
            "shareholder" : tracker.get_slot("shareholder"),
            "foreign" : tracker.get_slot("foreign"),
            "grarantor_age" : tracker.get_slot("grarantor_age"),
            "partnership" : tracker.get_slot("partnership"),
            "immediate" : tracker.get_slot("immediate"),
        }
        for k, v in slot.items(): 
            print(f"{k} : {v}")

        return []

class ActionRecomendNews(Action):
    
    def scrap_star(self, keyword):
        x = []
        session = HTMLSession()
        r = session.get('https://www.thestar.com.my/tag/technology')
        r.html.render()
        soup = BeautifulSoup(r.html.html, 'lxml')
        all_news = soup.find_all('a', {"data-content-category": "Tech/Tech News"})
        all_newss = set(all_news)
        for news in all_newss:
            news_content = news['data-content-title']
            news_link = 'https://www.thestar.com.my'+ news['href']
            if keyword in news_content:
                x.append(news_content)
                x.append(news_link)
                break
        return x

    def scrap_fmt(self, keyword):
        x = []
        session = HTMLSession()
        r = session.get('https://www.freemalaysiatoday.com/category/category/business/local-business/')
        r.html.render()
        soup = BeautifulSoup(r.html.html, 'lxml')
        all_news = soup.find_all('div', {"class": "td_module_2 td_module_wrap td-animation-stack"})
        for news in all_news:
            news_content = news.h3.a['title']
            news_link = news.h3.a['href']
            if keyword in news_content:
                x.append(news_content)
                x.append(news_link)
            break
        return x


    def name(self) -> Text:
        return "action_recommend_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        keyword = "Bitcoin"
        star_news = self.scrap_star(keyword)
        fmt_news = self.scrap_fmt(keyword)
        
        if star_news != '':
            news = star_news.copy()
        elif fmt_news != '':
            news = fmt_news.copy()
        else:
            return[]

        dispatcher.utter_message(
            templete="utter_recommend_news",
            news_title= news[0],
            news_url= news[1]
            )

        return[]

class ActionShowLoanStatus(Action):

    def name(self) -> Text:
        return "action_show_loan_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        

        return []
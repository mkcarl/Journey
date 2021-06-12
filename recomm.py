class ActionRecomend(Action):
    
    from bs4 import BeautifulSoup
    from requests_html import HTML, HTMLSession

    keyword = "Bitcoin"

    def scrap_star(keyword):
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

    def scrap_fmt(keyword):
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

    star_news = scrap_star(keyword)
    fmt_news = scrap_fmt(keyword)

    def name(self) -> Text:
        return "action_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if star_news != '':
            news = star_news.copy()
        elif fmt_news != '':
            news = fmt_news.copy()
        else:
            return[]

        dispatcher.utter_message(
            templete="utter_recommend",
            news_title= news[0]
            news_url= news[1]
            )

        return[]
from urllib.request import urlopen

import pymysql.cursors
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
import pymysql

def main(page_num):
    """
    :param page_num: get parameter page number
    :return: df to put the data in table
    """
    html = urlopen("https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3638&search=&column=&mcategoryId=0&boardType=01&listType=01&command=list&id=kr_010801000000&spage=" + str(page_num))
    """
    test_url another board
    https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3638&search=&column=&mcategoryId=0&boardType=01&listType=01&command=list&id=kr_010801000000&spage=1
    https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3638&search=&column=&mcategoryId=0&boardType=01&listType=01&command=list&id=kr_010801000000&spage=2
    """
    soup = BeautifulSoup(html, "html.parser")

    get_link = soup.select("td.title > a")

    link_list = []
    title_list = []
    date_list = []

    have_img = soup.select("tr > td:nth-child(1) > img")

    if have_img and page_num == 1:
        get_have_img_link = soup.select("td.title:nth-child(2) > a")[0:len(have_img)]
        get_date_img_link = soup.select("tr > td:nth-child(4)")[0:len(have_img)]
        #print(len(get_have_img_link))
        for link in get_have_img_link:
            link_list.append("https://www.dongguk.edu/mbs/kr/jsp/board/" + link["href"])
            title_list.append(link.text.replace(u"\xa0", " "))

        for date in get_date_img_link:
            date_list.append(date.text.replace("\r", "").replace("\n", "").replace("\t", "").strip())

        #print(len(link_list), link_list)
        get_not_img_link_first = soup.select(f"td.title:nth-child(2) > a")[len(have_img):len(get_link)]
        get_date_not_img_link = soup.select("tr > td:nth-child(4)")[len(have_img):len(get_link)]
        #print(len(have_not_img_link))
        for link in get_not_img_link_first:
            link_list.append("https://www.dongguk.edu/mbs/kr/jsp/board/" + link["href"])
            title_list.append(link.text.replace(u"\xa0", " "))
        for date in get_date_not_img_link:
            date_list.append(date.text.replace("\r", "").replace("\n", "").replace("\t", "").strip())
    else:
        get_not_img_link_other = soup.select(f"td.title:nth-child(2) > a")[len(have_img):len(get_link)]
        get_date_not_img_link = soup.select("tr > td:nth-child(4)")[len(have_img):len(get_link)]
        #print(len(have_not_img_link))
        for link in get_not_img_link_other:
            link_list.append("https://www.dongguk.edu/mbs/kr/jsp/board/" + link["href"])
            title_list.append(link.text.replace(u"\xa0", " "))
        for date in get_date_not_img_link:
            date_list.append(date.text.replace("\r", "").replace("\n", "").replace("\t", "").strip())
    ''' 
    debug code
    print(page_num, "  : " , len(link_list), link_list)
    print(page_num, "  : ", len(title_list), title_list)
    print(page_num, "  : ", len(date_list), date_list)
    '''

    parsing_data = {
        "title": title_list,
        "url": link_list,
        "date": date_list
    }

    df = pd.DataFrame(parsing_data)
    return parsing_data

def db(main_df):
    """
    :param main_df: insert table into df
    :return: x
    """
    engine = create_engine("mysql+pymysql://name:passw@end_point:port/database_name")
    conn = engine.connect()
    #cur = muzisungdb.cursor()
    print(engine)
    main_df.to_sql(name='test', con=engine, if_exists='replace')

if __name__ == "__main__":
    main_df = pd.DataFrame()
    for i in range(1, 2):
        data = pd.DataFrame(main(i))
        main_df = main_df.append(data, ignore_index=True)

    db(main_df)

from parsel import Selector

def get_titles_rank(response):
    parser = Selector(text=response.text)
    titles = parser.xpath(f"//h4/text()").getall()
    
    return titles

def get_atleta_rank(response, index_rank=1, index_atleta=1):
    parser = Selector(text=response.text)
    
    number_rank = parser.xpath(f"(//tbody)[{index_rank}]/tr[{index_atleta}]/td[1]/text()").getall()
    name_athlete = parser.xpath(f"(//tbody)[{index_rank}]/tr[{index_atleta}]/td[2]/a/text()").getall()
        
    return number_rank, name_athlete

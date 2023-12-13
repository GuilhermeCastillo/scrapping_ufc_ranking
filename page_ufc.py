from parsel import Selector

def get_all_tags(response, tag):
    parser = Selector(text=response.text)
    tags = parser.xpath(f"//{tag}").getall()
    
    return tags

def get_all_child_tag(response, tag):
    parser = Selector(text=response.text)
    tags = parser.xpath(f"(//{tag})[1]/*").getall()
    
    return tags

# def get_all_child_tags(response, tag):
#     parser = Selector(text=response.text)
#     tags = parser.xpath(f"//{tag}/*").getall()
    
#     return tags

# with open("page.txt", "w") as f:
#     f.write(page.text)


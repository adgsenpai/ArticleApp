import glob
import markdown
import bs4 as bs

def render_article(filename):
    with open('./articles/'+filename, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)        
        soup = bs.BeautifulSoup(html, 'html.parser')

        # find all image tags
        images = soup.find_all('img')

        # loop through all image tags if any has a width or height attribute leave it else make image fit to container
        for image in images:
            #if does not contain words width or height
            if not ('width' in image.attrs or 'height' in image.attrs):
                image['style'] = 'max-width:100%;'
           
           
        return soup
            


 

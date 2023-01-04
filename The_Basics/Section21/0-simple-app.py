import justpy as jp

def app():
    webPage = jp.QuasarPage()
    
    h1 = jp.QDiv(a=webPage, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=webPage, text="These graphs represent course review analysis.")
    return webPage

jp.justpy(app)

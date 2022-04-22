#! /usr/bin/env python3
import sys
import webview

print(f"webview.__file__={webview.__file__}")

def on_dropped_files(info):
    print(f"on_dropped_files:{info}")

def load(window, links):
    def load_(window, link):
        if link.startswith("http"):
            window.load_url(link)
            return

        content = ''

        with open(link, 'r') as f:
           content = f.read() 

        if link.endswith(".html"):
            window.load_html(content)
            return

        if link.endswith(".css"):
            window.load_css(content)
            return

        if link.endswith(".js"):
            window.evaluate_js(content)
            return

    for link in links:
        load_(window, link)

if __name__ == "__main__":
    urls = sys.argv[1:]

    window = webview.create_window('', text_select=True, 
                                   background_color='#808080')
    window.dropped_files = on_dropped_files
    webview.start(func=load, args=(window, urls), debug=True)


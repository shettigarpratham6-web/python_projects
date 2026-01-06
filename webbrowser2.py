import webbrowser
sites = [
    "https://chat.openai.com",
    "https://stackoverflow.com",
    "https://docs.python.org/3/library/webbrowser.html",
    "https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/second-largest3735"
]

for s in sites:
    webbrowser.open_new_tab(s)

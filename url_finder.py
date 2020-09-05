from googlesearch import search 

def ask_site():
    query_part2 = (input("Youtube or Spotify ? ")).lower().strip()
    if query_part2 == "youtube":
        get_youtube_link(query_part2)

    elif query_part2 == "spotify":
        get_spotify_link(query_part2)

    else:
        print("error")

def get_youtube_link(query):

    query_part1 = query
    real_query = "youtube" + " " + query_part1
    youtube_base_url = "https://www.youtube.com/watch?"
    youtube_url_results = []
    for url in search(real_query, tld="com", num=10, start=0, stop=10, pause=2): 
        if youtube_base_url in url:
            youtube_url_results.append(url)
            print(url)

def get_spotify_link(query):
    query_part1 = input("Enter a song name: ")
    real_query = "spotify" + " " + query_part1
    spotify_base_url = "https://open.spotify.com/track"
    spotify_url_results = []
    for url in search(real_query, tld="com", num=10, start=0, stop=10, pause=2): 
        if spotify_base_url in url:

            spotify_url_results.append(url)
            print(url)



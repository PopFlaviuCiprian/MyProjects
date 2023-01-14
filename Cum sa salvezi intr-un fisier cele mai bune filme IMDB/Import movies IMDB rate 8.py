import requests
from bs4 import BeautifulSoup

def get_movies(max_number_of_pages):

    page = 1
    while page <= max_number_of_pages:
        url = 'https://www.cinemagia.ro/filme/?pn=' + str(page)
        source_code = requests.get(url)
        # print(source_code.status_code)
        soup = BeautifulSoup(source_code.content)
        movies_title_div = soup.find_all('div', {'class' : 'title'})
        # print(movies_title_div)
        movies = [movie.text.strip('\n')[0:movie.text.strip('\n').find('\n')] for movie in  movies_title_div]
        movies.remove(movies[-1])
        # print(movies)
        rating_div = soup.find_all('div',{'class' : 'rating'})
        rating_imdb = [float(rating.text.strip('\n')[rating.text.strip('\n').find(' ') +1:]) for rating in rating_div]
        # print(rating_imdb)
        print('Lungime lista filme {}, lungime lista rating {}'.format(str( len(movies)), str(len(rating_imdb))))
        with open('FilmeRatingBun.txt', 'a', encoding='utf-8') as f:
            for i in range(len(movies)):
                if rating_imdb[i] >= 8:
                    f.write(movies[i] + ':' + str(rating_imdb[i]) + '\n')
                    print('Film: {}\n IMDB rating: {}' .format(movies[i], str(rating_imdb[i])))
        page += 1

if __name__ == '__main__':
    get_movies(10)


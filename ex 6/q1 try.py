def top5_by_genre(genre_name, file_name):
    f = None
    outf = None
    try:
        f = open(file_name, 'r')
        outf = open('C:/Users/user/Desktop/אוניברסיטת תא/סמסטר א/פייתון/תרגילי בית/ex 6/top5.csv', 'w')
        outf.write(f.readline()) #write the first line
        d = {}
        genre_name_BIG = genre_name.lower()
        for line in f:
            temp_genre = line.strip().split(',')[2].split(';')
            for g in temp_genre:
                if g.lower() == genre_name_BIG:
                    revenue = float(line.strip().split(',')[10])
                    rank = int(line.strip().split(',')[0])
                    d[(rank, line)] = revenue
        top5_film_by_rank = {}
        for top_film in sorted(d, key=d.get, reverse=True)[:5]:
            top5_film_by_rank[top_film[0]] = top_film[1]
        for top_rank in sorted(top5_film_by_rank):
            outf.write(top5_film_by_rank[top_rank])
        print('1')
    except IOError:
        print('IO Error encountered')
        print('0')
    finally:
        if f != None:
            f.close()
        if outf != None:
            outf.close()

top5_by_genre('faMily', 'C:/Users/user/Desktop/אוניברסיטת תא/סמסטר א/פייתון/תרגילי בית/ex 6/IMDB-Movie-Data.csv')



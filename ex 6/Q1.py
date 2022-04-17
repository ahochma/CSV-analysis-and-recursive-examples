def top5_by_genre(genre_name, file_name):
# Write the rest of the code for question 1 below here.
    f = None
    outf = None
    try:
        f = open(file_name, 'r')
        outf = open('C:/Users/user/Desktop/אוניברסיטת תא/סמסטר א/פייתון/תרגילי בית/ex 6/top5.csv', 'w')
        outf.write(f.readline()) #write the first line
        d = {}
        genre_name_BIG = genre_name[0].upper() + genre_name[1:]
        for line in f:
            temp_genre = line.strip().split(',')[2].split(';')
            for g in temp_genre:
                if g == genre_name_BIG:
                    revenue = float(line.strip().split(',')[10])
                    d[revenue] = line
        top5_film_by_rank = {}
        for top_film in sorted(d, reverse=True)[:5]:
            rank = d[top_film].strip().split(',')[0]
            top5_film_by_rank[rank] = d[top_film]
        for film_by_rank in sorted(top5_film_by_rank):
            outf.write(top5_film_by_rank[film_by_rank])
        print('1')
    except IOError:
        print('IO Error encountered')
        print('0')
    finally:
        if f != None:
            f.close()
        if outf != None:
            outf.close()



#top5_by_genre('Fantsy', 'C:/Users/user/Desktop/אוניברסיטת תא/סמסטר א/פייתון/תרגילי בית/ex 6/IMDB-Movie-Data.csv')

##f = open('C:/Users/user/Desktop/אוניברסיטת תא/סמסטר א/פייתון/תרגילי בית/ex 6/IMDB-Movie-Data_by_revenue.csv', 'r')
##f.readline()
##for line in f:
##    rev1 = float(line.strip().split(',')[10])
##    nextfilm = f.readline()
##    rev2 = float(nextfilm.strip().split(',')[10])
##    if rev1 == rev2:
##        print('same rev')
##f.close()


a = 'Guy'
b = a[0].upper() + a[1:]
print(b)


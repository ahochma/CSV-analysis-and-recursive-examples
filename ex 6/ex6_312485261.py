#Exercise 6: Python Programming 

#########################################
# Question 1 - do not delete this comment
#########################################
def top5_by_genre(genre_name, file_name):
# Write the rest of the code for question 1 below here.
    f = None
    outf = None
    try:
        f = open(file_name, 'r')
        outf = open('C:/Users/user/Desktop/אוניברסיטת תא/סמסטר א/פייתון/תרגילי בית/ex 6/top5.csv', 'w')
        outf.write(f.readline())
        d = {}
        genre_name_low = genre_name.lower()
        for line in f:
            temp_genre = line.strip().split(',')[2].split(';')
            for g in temp_genre:
                if g.lower() == genre_name_low:
                    revenue = float(line.strip().split(',')[10])
                    rank = int(line.strip().split(',')[0])
                    d[(rank, line)] = revenue
        top5_film_by_rank = {}
        for top_film in sorted(d, key=d.get, reverse=True)[:5]:
            top5_film_by_rank[top_film[0]] = top_film[1]
        for top_rank in sorted(top5_film_by_rank):
            outf.write(top5_film_by_rank[top_rank])
        return 1
    except IOError:
        print('IO Error encountered')
        return 0
    finally:
        if f != None:
            f.close()
        if outf != None:
            outf.close()
            
#########################################
# Question 2 - do not delete this comment
#########################################
def mult(x,y):
# Write the rest of the code for question 2 below here.
    if y == 0:
        return 0
    return x + mult(x, y-1)

#########################################
# Question 3 - do not delete this comment
#########################################
def count_val(lst,val):
# Write the rest of the code for question 3 below here.
    if len(lst) == 0:
        return 0
    if lst[0] == val:
        return 1 + count_val(lst[1:], val)
    else:
        return count_val(lst[1:], val)

#########################################
# Question 4a - do not delete this comment
#########################################	
def climb_combinations(n):
# Write the rest of the code for question 4 below here.
    if n == 0:
        return 1
    if n < 0:
        return 0
    return climb_combinations(n-2) + climb_combinations(n-1)

#########################################
# Question 4b - do not delete this comment
#########################################
def climb_combinations_memo(n, memo=None):
# Write the rest of the code for question 4 below here.
    if n == 0:
        return 1
    if n < 0:
        return 0
    if memo == None:
        memo = {}
    memo_key = n
    if memo_key not in memo:
        memo[memo_key] = climb_combinations_memo(n-2, memo) + climb_combinations_memo(n-1, memo)
    return memo[memo_key]

#########################################
# Question 5 - do not delete this comment
#########################################
def can_return_to_earth(weights, W, K):
# Write the rest of the code for question 5 below here.
    if W == 0:
        return True
    elif len(weights) == 0:
        return False
    elif W < 0:
        return False
    else:
        option1 = can_return_to_earth(weights[:-1], W, K)
        if weights[-1] < K: 
            option2 = can_return_to_earth(weights[:-1], W - weights[-1], K)
            return option2 or option1
        return option1

x = top5_by_genre('Mystery', 'C:/Users/user/Desktop/אוניברסיטת תא/סמסטר א/פייתון/תרגילי בית/ex 6/IMDB-Movie-Data.csv')
print(x)


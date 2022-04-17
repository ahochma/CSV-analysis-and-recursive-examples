#Exercise 5: Python Programming 

#########################################
# Question 1 - do not delete this comment
#########################################
def max_nums(file):
# Write the rest of the code for question 1 below here.
    f = open(file,'r')
    numbers = f.readline().split()
    intnum = []
    for num in numbers:
        intnum.append(int(num))
    f.close()
    return max(intnum)


#########################################
# Question 2 - do not delete this comment
#########################################
def copy_capitalized_words(infile, outfile):
# Write the rest of the code for question 2 below here.
    inf = open(infile,'r')
    outf = open(outfile,'w')
    for line in inf:
        for word in line.split():
            if word[0].isupper():
                outf.write(word + '\n')
    inf.close()
    outf.close()

	
#########################################
# Question 3 - do not delete this comment
#########################################
def get_x_freqs(infile, outfile, x):
# Write the rest of the code for question 3 below here.
    if len(infile) == 0 or len(outfile) == 0:
        raise ValueError('Invalid file name')
    inf = open(infile,'r')
    outf = open(outfile,'w')
    d = {}
    for line in inf:
        for word in line.split():
            d[word] = d.get(word, 0) + 1
    inf.close()
    for word in sorted(d, key=d.get, reverse=True)[:int(x)]:
        outf.write(word +' ' + str(d.get(word)) + '\n')
    outf.close()



#########################################
# Question 4 - do not delete this comment
#########################################
def decode(in_file, out_file):
# Write the rest of the code for question 4 below here.
    f = None
    o = None
    try:
        f = open(in_file, 'r')
        o = open(out_file, 'w')
        for l in f:
            for i in range(0, len(l)):
                if l[i] == 'a':
                    o.write('z')
                elif l[i] == 'A':
                    o.write('Z')
                elif ord(l[i]) == 32: ##space
                    o.write(' ')
                elif ord(l[i]) == 10: ##enter
                    o.write('\n')
                else:
                    o.write(chr(ord(l[i])-1))
    except IOError:
        print('Can’t decipher file due to an IO Error.')
    finally:
        if f != None:
            f.close()
        if o != None:
            o.close()


def good_or_bad_input(input_file):
    f = open(input_file, 'r')
    for line in f:
        if line.startswith('#'):
            continue
        if len(line.split(',')) != 4 :
            raise ValueError('Invalid input file')
        for w in line.split(','):
            if len(w.rstrip()) == 0:
                raise ValueError('Invalid input file')
    f.close()
    return True
#########################################
# Question 5 - do not delete this comment
#########################################
def process_contacts(contacts_file):
# Write the rest of the code for question 5 below here.
    f = None
    d = {} #key = city & value = lst of family []
    try:
        good_or_bad_input(contacts_file)
        f = open(contacts_file, 'r')
        for line in f:
            if line.startswith('#'):
                continue
            city = line.split(',')[3].rstrip()
            family = line.split(',')[1]
            if city in d:
                lst_families_names = d.get(city)
            else:
                lst_families_names =[]
            if family not in lst_families_names:
                lst_families_names.append(family)
            d[city] = lst_families_names
        return d
    except IOError:
        print('IO Error encountered')
        return d
    finally:
        if f != None:
            f.close()
            
#########################################
# Question 6 - do not delete this comment
#########################################
def get_covid_cases_by_date(filename, date):
# Write the rest of the code for question 6 below here.
    f = None
    try:
        f = open(filename, 'r', encoding='UTF-8')
        d = {}
        f.readline()
        for line in f:
            check_date = line.strip().split(',')[2]
            if check_date == date:
                if line.split(',')[5] == '<15':
                    continue
                city = line.strip().split(',')[13]
                cases = line.strip().split(',')[5]
                d[city] = d.get(city, 0) + int(cases)
        if d == {}:
            raise ValueError
        for tencity in sorted(d, key=d.get, reverse=True)[:10]:
            print(d[tencity], '\t', tencity)
    except IOError:
        print('IO Error encountered')
    except ValueError:
        print('No data is available for', date)
    finally:
        if f != None:
            f.close()





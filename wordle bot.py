from english_words import get_english_words_set


from operator import and_, or_
from functools import reduce

def containsAny(str, set):
    return reduce(or_, map(str.__contains__, set))

def containsAll(str, set):
    return reduce(and_, map(str.__contains__, set))






#test_str = ""
#for x in lwordsfi1:
#    test_str=test_str+x

#res = {}

#for keys in test_str:
 #   res[keys] = res.get(keys, 0) + 1

#print ("Count of all characters in GeeksforGeeks is : \n"
                                  #           +  str(res))

#print(lwordsfi1)











lwords=[]
lmain=get_english_words_set(['web2'], lower=True)
for x in lmain:
    if len(x)==5:
        lwords.append(x.lower())




#returns a list containing lgrey,yellow,greennumbers,greenletters list

def inputs():

    grey=input("Enter the elements that were greyed out")
    yellow=input('Enter the elements that were yellow')
    green=input('Enter the greened elemnsts along wihh their positions(0-4)'
                 'eg: 0a2x'
                 '    4k2s '     )


    lgrey=list(grey)
    lgreen=list(green)
    lyellow=list(yellow)
    lgreen_numbers = []
    lgreen_letters = []

    if lgreen!=[]:

        for i in lgreen:
            if i.isalpha() is True:
                lgreen_letters.append(i)
            else:
                lgreen_numbers.append(int(i))
    lgrey = list(dict.fromkeys(lgrey))
    lyellow = list(dict.fromkeys(lyellow))
    lgreen_letters=list(dict.fromkeys(lgreen_letters))
    lgreen_numbers=list(dict.fromkeys(lgreen_numbers))



    result=[lgrey, lyellow, lgreen_numbers, lgreen_letters,grey,yellow]
    return (result)





def filter(result):

    lgrey = result[0]
    lyellow = result[1]
    lgreen_num=result[2]
    lgreen_alpha=result[3]
    lfiltered_grey = []

    for word in lwords:
        if containsAll(word, lgrey) is not True and containsAll(word, lyellow) is True:
            lfiltered_grey.append(word)


    lfiltered_green = []


#for green filter super ineffiecient but gets the job done somehow
    if len(lgreen_alpha) == 0:
        lfiltered_green = lfiltered_grey

    elif len(lgreen_alpha) == 1:
        for word in lfiltered_grey:
            if word[lgreen_num[0]] == lgreen_alpha[0]:
                lfiltered_green.append(word)

    elif len(lgreen_alpha) == 2:
        for word in lfiltered_grey:
            if word[lgreen_num[0]] == lgreen_alpha[0] and word[lgreen_num[1]] == lgreen_alpha[1]:
                lfiltered_green.append(word)
    elif len(lgreen_alpha) == 3:
        for word in lfiltered_grey:
            if word[lgreen_num[0]] == lgreen_alpha[0] and word[lgreen_num[1]] == lgreen_alpha[1] and word[
                lgreen_num[2]] == lgreen_alpha[2]:
                lfiltered_green.append(word)


    elif len(lgreen_alpha) == 4:
        for word in lfiltered_grey:
            if word[lgreen_num[0]] == lgreen_alpha[0] and word[lgreen_num[1]] == lgreen_alpha[1] and word[
                lgreen_num[2]] == lgreen_alpha[2] and word[lgreen_num[3]] == lgreen_alpha[3]:
                lfiltered_green.append(word)

    return(lfiltered_green)





def frequency(list):
    test_str = ""

    for i in list :
        test_str=test_str+i



    res = {}

    for keys in test_str:
        res[keys] = res.get(keys, 0) + 1


    orders = res

    sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)
    lfrequency=[]

    for i in sort_orders:
        l=[i[0], i[1]]
        lfrequency.append(l)


    lsuggestions = []

    if len(lfrequency) > 9:                     #remove letters already inputed from suggestions
        for i in lfrequency:
            if i[0] not in j:
                lsuggestions.append(i[0])

    return (lsuggestions[0:4])




def finalsuggestion(w,alp):             #w=word alp=already present

    str=''
    for i in alp:
        str=str+i

    prime_suggestions=[]
    secondary_suggestions=[]
    for word in w:
        l=list(word)

        if alp[0] in word and alp[1] and alp[2] in word:
            prime_suggestions.append(word)

        elif alp[0] in word and alp[1] in word:
            secondary_suggestions.append(word)


    print(prime_suggestions)
    print(secondary_suggestions)






x=inputs()


j=x[4]+x[5]
green_letters=x[3]
for i in green_letters:
    j=j+i

words=filter(x)
print(words)
print(len(words))
suggestions=frequency(words)
print(suggestions)

finalsuggestion(words,suggestions)




















def read_ints():
    return map(int, input().split(','))

def req_dict(eds):
    '''возвращает словарь, item -> [(item,conf),...(item,conf)]'''
    re = dict()
    for edge in eds:
        if re.get(edge[0], False):
            re[edge[0]].append((edge[1],edge[2]/1000))
        else:
            re[edge[0]] = [(edge[1],edge[2]/1000)]
    for k,v in re.items():
        v.sort(key = lambda y: y[1], reverse = True)
        print('{},  {}'.format(k, v)) #удалить
    return re

def recomend_items(req, freqs, basket, absent = [], supp = 0):
    ''' возвращает рекомендации к покупке от 0 до 4 товаров '''
    ## По моей логике, рекомендательные системы не могут рекомендовать товар,
    ## который уже находиться в корзине.
    ## Помимо этого, если было бы известно, что score - это confidence * 1000, 
    ## где confidence это достоверность из ассоциативных правил, можно было бы посчитать lift для каждого правила, 
    ## и делать рекомендации на основе этого.
    ## Так как это не известно, делается все по логике:
    ##  сначала рекомендации строятся на основе данных правил, 
    ##  и если их число меньше 4, то в список дополняются самые часто покупаемые item-ы
     
    recommendations = []
    archive = dict()
    for item in basket:
        if item in req.keys():
            for re in req[item]:
                archive[re[0]] = archive.get(re[0], 0) + re[1]     # У каждого рекомендуемого по правилам item-а есть значение, 
            print(archive)                                         # которое увеличивается, если в корзине есть другие продукты с рекомендацией
                                                                   # на данный item
    for k,v in archive.items():
        if k not in absent and k not in basket:
            recommendations.append((k,v))
    if len(recommendations) > 4:                                   # Случай, когда рекомендаций по правилам больше 4.
        recommendations.sort(key = lambda y: y[1], reverse = True) # Сортируем по значениям, чтобы получить самые релевантные
        recommendations = [recommendations[j][0] for j in range(4)]
    else:
        recommendations = [recommendations[j][0] for j in range(len(recommendations))]

    i = 0                                                          # Так же можно задать порог supp, благодаря которому мы отсечем item-мы которые редко преобретали
    while len(recommendations) < 4 and i < len(freqs) and freqs[i][2] > supp:     
        if freqs[i][0] not in absent and freqs[i][0] not in basket and freqs[i][0] not in recommendations:
            recommendations.append(freqs[i][0])
        i += 1

    return recommendations



# edges - правила (чем выше score, тем релевантнее рекомендация)
# (a_id, b_id, score)
## догадка: score = confidence * 1000
edges=[
[1,2,300],
[1,4,150],
[1,7,220],
[2,1,100],
[2,5,520],
[2,10,110],
[3,4,340],
[4,1,150],
[4,3,340],
[5,2,520],
[7,1,220],
[9,10,230],
[10,2,110],
[10,9,230]
]

# freqs - популярность товаров, чем выше, тем лучше.
# (id, freq)
freqs = [
[1, 1234],
[2, 1505],
[3, 900],
[4, 2345],
[5, 378],
[6, 2998],
[7, 5421],
[8, 1323],
[9, 708],
[10, 1283]
]

# подсчет общего кол-ва покупок
freq_all = sum([freqs[i][1] for i in range(len(freqs))])
print(freq_all)

# рассчет supp
for i in range(len(freqs)):
    freqs[i].append(round(freqs[i][1]/freq_all,4))
    print(freqs[i])
freqs.sort(key = lambda y: y[1], reverse = True)
# представляем правила в более удобном формате
req = req_dict(edges)

# ввод
abs = [5, 1, 10]     #list(read_ints())
bas = [5, 10, 8, 9]  #[4, 8, 1, 9, 7]  #[6]  #[10] #[8, 2, 7] #list(read_ints())
print(recomend_items(req, freqs, bas, absent =  abs)) 

##оставить коммент про отбор порога supp, а так здесь он не нужен, так как набор данных маленький

#-Генерация потенциально часто встречающихся наборов элементов (кандидатов)
    #-Объединение. Каждый кандидат из k эл-тов , будет формироваться путем объединения двух часто встречающихся наборов k-l эл-тов
    #-Подсчет поддержки для кандидатов
    #-Удаление избыточных правил. На основании свойства антимонотонности, следует удалить все сформированные k-элементарные наборы, 
    #не являющиеся часто встречающимися     

#-Поиск правил для найденных кандидатов, если подъем (lift) очередного правила больше единицы, то это правило считается достоверным, 
#и его можно использовать для рекомендации

from trains.models import Train

# файл для создания логики приложений


# функция для поиска возможных маршрутов
def dfs_paths(graph, start, goal):
    '''
    Функция поиска всех возможных маршрутов из одного города в другой
    Вариант посещения одного и того же города более 1 раза не рассматривается
    '''
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))

# функция для построение графа (списка городов откуда-куда можно приехать) {М: [В,Л,М], С: [Н,Ш]...}
def get_graph(qs):
    graph = {}
    for item in qs:
        graph.setdefault(item.from_city_id, set())  # значение по умолчанию для ключа from_city_id - множество
        graph[item.from_city_id].add(item.to_city_id)  # ключ город из которого едем, значения это города куда едем
    return graph


# функция для обработки формы поиска маршрута
def get_routes(request, form) -> dict:
    context = {'form': form}
    # select_related() Для уменьшения отдельных обращений к БД, получаю инфу сразу по всем связанным таблицам
    qs = Train.objects.all().select_related('from_city', 'to_city')
    # qs = Train.objects.all()  # список всех поездов из таблицы/модели Train
    graph = get_graph(qs)
    data = form.cleaned_data  # привожу данные из формы в читабельный вид  form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']  # список городов, через которые хотим проехать
    travelling_time = data['travelling_time']
    all_ways = list(dfs_paths(graph, start=from_city.id, goal=to_city.id))  # список всех возможных маршрутов из А в Б
    if not len(all_ways):  # функция возвращает генератор yeld, поэтому используем list
        raise ValueError('Маршрут не найден')
    if cities:
        _cities = [city.id for city in cities]
        right_ways = []
        for route in all_ways:
            if all(city in route for city in _cities):  # если все нужные города есть в маршруте, добавляю его
                right_ways.append(route)
            if not right_ways:
                raise ValueError('Маршрут через выбранные города не возможен')
    else:
        # если города, через которые необходимо проехать не заданы - приравниваем их ко всем городам
        right_ways = all_ways
    routes = []
    all_trains = {}
    for q in qs:
        all_trains.setdefault((q.from_city, q.to_city), [])
        all_trains[(q.from_city, q.to_city)].append(q)
    for route in right_ways:
        tmp = {}
        tmp['trains'] = []
        total_time = 0
        for i in range(len(route)-1):
            qs = all_trains[(route[i], route[i+1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['trains'].append(q)
        tmp['total_time'] = total_time
        if total_time <= travelling_time:
            routes.append(tmp)
    if not routes:
        raise ValueError('Время в пути больше заданного')
    sorted_routes = []
    if len(routes) == 1:
        sorted_routes = routes
    else:
        times = list(set(r['total_time'] for r in routes))
        times = sorted(times)
        for time in times:
            for route in routes:
                if time == route['total_time']:
                    sorted_routes.append(route)
    context['routes'] = sorted_routes
    context['cities'] = {'from_city': from_city, 'to_city': to_city}
    return context


print('\t\t\t\t\tКаталог машин версия №1')

while True:#main circle
    for i in range(117): print('-',end='')

    print('\nКакую операцию вы хотите выполнить?')
    print('1)Добавить\n2)Список\n3)Поиск\n4)Очистить\n5)Завершить')

    qws = input()

    if qws == 'Добавить' or qws == 'добавить' or qws == '1':

        with open('car catalog 1.txt', 'a', encoding='utf-8') as f:
            print('Чтобы добавить машину в список, введите её характеристики')

            mark = input('Марка:')
            model = input('Модель:')
            num = input('Номер:')
            engine = input('Двигатель л.с.:')
            color = input('Цвет:')
            light = input('Состояние фар:')
            doors = input('Состояние дверей:')
            maxV = input('Максимальная скорость км/ч:')
            m = input('Масса кг:')

            k = ['on','On','off','Off','вкл','Вкл','выкл','Выкл']
            d = ['open','Open','close','Close','открыто','Открыто','заперто','Заперто']

            while light not in k:
                light = input('\nВведите состояние фар только вкл/выкл или on/off:\n')

            while doors not in d:
                doors = input('\nВведите состояние дверей только открыто/заперто или open/close:\n')


            l = len([i for i in open('list 1.txt')])

            for i in range(75):f.write('-')
            
            f.write('\nМарка: ')
            f.write(mark)
            
            f.write('\nМодель: ')
            f.write(model)
            
            f.write('\nНомер: ')
            f.write(num)
            
            f.write('\nДвигатель л.с.: ')
            f.write(engine)
            
            f.write('\nЦвет: ')
            f.write(color)

            f.write('\nСостояние фар: ')
            f.write(light)

            f.write('\nСостояние дверей: ')
            f.write(doors)
            
            f.write('\nМаксимальная скорость км/ч: ')
            f.write(maxV)
            
            f.write('\nМасса кг: ')
            f.write(m)
            f.write('\n')
            for i in range(75): f.write('-')
            f.write('\n')

        with open('list 1.txt', 'a+', encoding='utf-8') as list:
            #list.write('Арт.'+'0'*(4-len(str(l+1)))+str(l+1)+' '+mark+' '+model+' '+num+'\n')
            list.write( mark + ' ' + model + ' ' + num + '\n')

    if qws == 'Список' or qws == 'список' or qws == '2':

        with open('car catalog 1.txt', 'r', encoding='utf-8') as f:

            print('\t\t\t\t\tСписок всех машин')
            head = f'|{"Марка":^20}|{"Модель":^20}|{"Номер":^10}|{"Двигатель л.с.":^14}|{"Цвет":^15}|{"Фары":^5}|{"Двери":^7}|{"Скорость":^8}|{"Масса кг":^8}|'

            options = f.readlines()

            print(head)
            for i in range(0,len(options),11):
                print('-'*117)
                print(f'|{(options[i+1])[7:-1]:^20}|{(options[i+2])[8:-1]:^20}|{(options[i+3])[7:-1]:^10}|'
                      f'{(options[i+4])[16:-1]:^14}|{(options[i+5])[6:-1]:^15}|{(options[i+6])[15:-1]:^5}|'
                      f'{(options[i+7])[18:-1]:^7}|{(options[i+8])[28:-1]:^8}|{(options[i+9])[10:-1]:^8}|')

    if qws == 'Поиск' or qws == 'поиск' or qws == '3':

        print('Введите марку, модель или номер автомобиля')

        with open('car catalog 1.txt', 'r', encoding='utf-8') as f:
            art = input()
            #artl = [i[4:8] for i in open('list 1.txt', encoding='utf-8')]
            #nums = [i[-10:-1] for i in open('list 1.txt', encoding='utf-8')]

            marks = [i[:-1] for i in open('list 1.txt', encoding='utf-8')]
            for i in range(len(marks)):
                s = ''
                for j in marks[i]:
                    if j==' ':break
                    s+=j
                marks[i] = s

            models = [i[:-10] for i in open('list 1.txt', encoding='utf-8')]
            for i in range(len(models)):
                if (models[i])[-1]==' ':
                    models[i] = (models[i])[:-1]

            for i in range(len(models)):
                s = ''
                for j in (models[i])[::-1]:
                    if j==' ':break
                    s+=j
                models[i] = s[::-1]

            nums = [i[-10:-1] for i in open('list 1.txt', encoding='utf-8')]
            for i in range(len(nums)):
                if (nums[i])[0]==' ':nums[i]=(nums[i])[1:]

            lines = [i for i in open('list 1.txt', encoding='utf-8')]

            change = 0
            head = f'|{"Марка":^20}|{"Модель":^20}|{"Номер":^10}|{"Двигатель л.с.":^14}|{"Цвет":^15}|{"Фары":^5}|{"Двери":^7}|{"Скорость":^8}|{"Масса кг":^8}|'


            if art in marks:
                print(head)
                stroki = f.readlines()
                for i in range(0, len(stroki), 11):
                    if stroki[i+1] == 'Марка: ' + art + '\n':
                        print('-' * 117)
                        print(
                            f'|{(stroki[i + 1])[7:-1]:^20}|{(stroki[i + 2])[8:-1]:^20}|{(stroki[i + 3])[7:-1]:^10}|'
                            f'{(stroki[i + 4])[16:-1]:^14}|{(stroki[i + 5])[6:-1]:^15}|{(stroki[i + 6])[15:-1]:^5}|'
                            f'{(stroki[i + 7])[18:-1]:^7}|{(stroki[i + 8])[28:-1]:^8}|{(stroki[i + 9])[10:-1]:^8}|')

            elif art in models:
                print(head)
                stroki = f.readlines()
                for i in range(0, len(stroki), 11):
                    if stroki[i + 2] == 'Модель: ' + art + '\n':
                        print('-' * 117)
                        print(
                            f'|{(stroki[i + 1])[7:-1]:^20}|{(stroki[i + 2])[8:-1]:^20}|{(stroki[i + 3])[7:-1]:^10}|'
                            f'{(stroki[i + 4])[16:-1]:^14}|{(stroki[i + 5])[6:-1]:^15}|{(stroki[i + 6])[15:-1]:^5}|'
                            f'{(stroki[i + 7])[18:-1]:^7}|{(stroki[i + 8])[28:-1]:^8}|{(stroki[i + 9])[10:-1]:^8}|')

            elif art in nums:
                print(head)
                stroki = f.readlines()
                for i in range(0, len(stroki), 11):

                    if stroki[i + 3] == 'Номер: ' + art + '\n':
                        print('-' * 117)
                        print(
                            f'|{(stroki[i + 1])[7:-1]:^20}|{(stroki[i + 2])[8:-1]:^20}|{(stroki[i + 3])[7:-1]:^10}|'
                            f'{(stroki[i + 4])[16:-1]:^14}|{(stroki[i + 5])[6:-1]:^15}|{(stroki[i + 6])[15:-1]:^5}|'
                            f'{(stroki[i + 7])[18:-1]:^7}|{(stroki[i + 8])[28:-1]:^8}|{(stroki[i + 9])[10:-1]:^8}|')
                        break

                print('Что вы хотите сделать?')
                change = input('1)Изменить\n2)Удалить\n')

            else:
                print('По вашему запросу ничего не найдено')

            count = i
        if change == 'Изменить' or change == 'изменить' or change == '1':
            cont = 'да'

            while cont=='да' or cont=='Да' or cont=='1':
                with open('car catalog 1.txt', 'w', encoding='utf-8') as f:
                    print('Что вы хотите изменить?')
                    variant = input('1)Номер\n2)Цвет\n3)Состояние фар\n4)Состояние дверей\n')

                    if variant == '1' or variant=='Номер':
                        num = input('Номер:')
                        for index in range(len(nums)):
                            if nums[index]==(stroki[count + 3])[7:-1]:
                                nums[index]=num
                                break
                        stroki[count + 3] = 'Номер: '+num+'\n'

                        with open('list 1.txt', 'w', encoding='utf-8') as l:
                            for k in range(len(nums)):
                                l.write(f'{marks[k]} {models[k]} {nums[k]}\n')


                    if variant == '2' or variant=='Цвет':
                        color = input('Цвет:')
                        stroki[count + 5] = 'Цвет: '+color+'\n'


                    if variant == '3' or variant=='Состояние фар':
                        light = input('Состояние фар:')
                        k = ['on', 'On', 'off', 'Off', 'вкл', 'Вкл', 'выкл', 'Выкл']
                        while light not in k:
                            light = input('\nВведите состояние фар только вкл/выкл или on/off:\n')
                        stroki[count + 6] = 'Состояние фар: '+light+'\n'


                    if variant == '4' or variant=='Состояние дверей':
                        doors = input('Состояние дверей:')
                        d = ['open', 'Open', 'close', 'Close', 'открыто', 'Открыто', 'заперто', 'Заперто']
                        while doors not in d:
                            doors = input('\nВведите состояние дверей только открыто/заперто или open/close:\n')
                        stroki[count + 7] = 'Состояние дверей: '+doors+'\n'

                    for j in range(len(stroki)):
                        f.write(stroki[j])

                    cont = input('Продолжить изменения?\n1)Да\n2)Нет\n')
            print('Изменения внесены')

        if change=='2' or change=='Удалить' or change=='удалить':
            stroki[count] = ''
            stroki[count+1] = ''
            stroki[count+2] = ''
            stroki[count+3] = ''
            stroki[count+4] = ''
            stroki[count+5] = ''
            stroki[count+6] = ''
            stroki[count+7] = ''
            stroki[count+8] = ''
            stroki[count+9] = ''
            stroki[count+10] = ''

            for index in range(len(nums)):
                if nums[index] == (stroki[count + 3])[7:-1]:
                    nums[index] = num
                    break

            for index in range(len(lines)):
                if ((stroki[i + 3])[7:-1]) in lines[index]:
                    lines[index+1] = ''
                    break

            marks[index] = ''
            models[index] = ''
            with open('car catalog 1.txt','w',encoding='utf-8') as f:
                with open('list 1.txt', 'w', encoding='utf-8') as l:
                    for j in range(len(stroki)):
                        f.write(stroki[j])
                    for k in range(len(lines)):
                        l.write(lines[k])

                    print('Машина удалена из списка')


    if qws == 'Очистить' or qws == 'очистить' or qws == '4':
        print('Вы точно хотите очистить весь список?')
        delete = input()
        if delete == 'Да' or delete == 'да' or delete=='Yes' or delete=='yes':
            with open('car catalog 1.txt', 'w') as f:
                with open('list 1.txt', 'w') as list:
                    f.write('')
                    list.write('')

            print('Список пуст')

    if qws == 'Завершить' or qws == 'завершить' or qws == '5':
        print('Сеанс завершён')
        break
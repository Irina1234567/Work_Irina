days = {
    '01': 'первое', '02': 'второе',
    '03': 'третье',  '04': 'четвертое',
    '05': 'пятое', '06': 'шестое',
    '07': 'седьмое', '08': 'восьмое',
    '09': 'девятое',  '10': 'десятое'
}
months = {
    '01': 'январь', '02': 'февраль',
    '03': 'март',  '04': 'апрель',
    '05': 'май', '06': 'июнь',
    '07': 'июль', '08': 'август',
    '09': 'сентябрь',  '10': 'октябрь',
    '11': 'ноябрь',  '12': 'декабрь'
    }
while True:
    date  = input('Введите дату в формате dd.mm.yyyy: ')
    day, month, year = date.split('.')
    if 1<= int(day) < 10 and 1<= int(month)<=12 and year.isdigit():
        break

day = days.get(day)
month = months.get(month)
print('Введённая дата:', date, sep='\n')
print('{}' ' {}' ' {}' ' года'.format(day,month,year))
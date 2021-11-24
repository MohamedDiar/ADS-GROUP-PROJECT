import heapq_max
import re


def welcome():
    print('TravelBuddy - Housing for students has never been that easy!')
    print('\nAre you planning to host or to guest?\nEnter 1 for being a guest\nEnter 2 for being a host\nEnter 3 to quit')


def guest(available_bookings):
    print("\nHere is a list with the available places to stay:")
    city = []
    for key in available_bookings.keys():
        city.append(available_bookings[key][0])
    print(list(set(city)))
    cityname = input(
        "\nPlease enter the position from the list above that you would like to have:").strip().lower()
    while cityname not in city:
        print("\nWe are sorry, but it looks like the position you entered is not available, please try again")
        cityname = input(
            "\nPlease enter the position from the list above that you would like to have:").strip().lower()

    points = input(
        "\nPlease select the range of point you are willing to spend: 0-300/301-700/701-1000:").strip().lower()
    while points != '0-300' and points != '301-700' and points != '701-1000':
        print("\nWe are sorry, but it looks like the range of points you entered is not available, please try again")
        points = input(
            '\nPlease enter the range of points again - 0-300/301-700/701-1000: ').strip().lower()

    timespan = input(
        "\nPlease enter your preferred time to book the room - JANUARY-MARCH/ APRIL-JUNE/ JULY-SEPTEMBER/ OCTOBER-DECEMBER:").strip().lower()
    while timespan != 'JANUARY-MARCH' and timespan != 'APRIL-JUNE' and timespan != 'JULY-SEPTEMBER' and timespan != 'OCTOBER-DECEMBER' :
        print("\nWe are sorry, but it looks like the time span you entered is not available, please try again")
        time = input(
            '\nPlease enter the time span period again - JANUARY-MARCH/ APRIL-JUNE/ JULY-SEPTEMBER/ OCTOBER-DECEMBER: ').strip().lower()

    guests_preference = {cityname, points, timespan}
    print()
    guests_heap = []
    for guests, conditions in available_bookings.items():
        conditions_set = set(conditions)
        priority = len(guests_preference & conditions_set)
        heapq_max.heappush_max(guests_heap, (priority, guests))

    print('\nBased on your selection, these are the best locations for you to stay at:: \n')
    knt = 0
    for i in range(len(guests_heap)):
        if guests_heap[i][0] > 0:
            knt += 1
            print('Option', knt, ':',
                  str(available_bookings[guests_heap[i][1]])[1:-1], '\n')


def host(available_bookings):
    print('\nYou are going to become a host!')
    print('\nPlease enter the following details: ')
    keys = [key for key in available_bookings.keys()]

    rooms = input(
        '\nPlease enter the number of rooms you are hosting (numerically):').strip().lower()
    while rooms in keys:
        print('\nEnter the correct format!')
        rooms = input(
            '\nPlease enter the number of rooms youre hosting again: ').strip().lower()

    location = input('\nPlease enter the location of the house being hosted: (Madrid, Segovia or Barcelona) ').strip().lower()
    while not location.isalpha():
        print('\nPlease enter an available location!')
        location = input('\nPlease enter the location again: ').strip().lower()

    area = input('\nPlease enter the area where youre hosting the house: ').strip().lower()

    points = input(
        '\nPlease enter the amount of points wanted for hosting: (0-300/301-700/701-1000) ').strip().lower()
    while points != '0-300' and points != '301-700' and points != '701-1000':
        print("\nPlease enter a valid amount")
        points = input(
            '\nPlease enter the amount of points wanted - 0-300/301-700/701-1000: ').strip().lower()


    timespan = input(
        '\nPlease enter the months youre willing to host - JANUARY-MARCH/ APRIL-JUNE/ JULY-SEPTEMBER/ OCTOBER-DECEMBER: ').strip().lower()
    while timespan != 'january-march' and timespan != 'april-june' and timespan != 'july-september' and timespan != 'october-december' :
        print("\nPlease try again.")
        timespan = input(
            '\nPlease enter the time period yore hosting again - : JANUARY-MARCH/ APRIL-JUNE/ JULY-SEPTEMBER/ OCTOBER-DECEMBER').strip().lower()

    phone_number = input('\nPlease enter your phone number: ').strip().lower()


    description = input('\nPlease enter your name, age and a brief description of yourself: ').strip().lower()

    values = [location, area, points, timespan, phone_number, description]
    available_bookings[rooms] = values
    print('\nThe position has been added!\n')
    print('\nNumber of Rooms: City, Area, Number of points wanted, time span, Phone number, Name, Age, Description \n')
    print(rooms, ':', str(values)[1:-1])



def availablebookings():
    available_bookings = {}
    available_bookings[2] = ['barcelona', 'sants', '301-700', 'january-march','643561987', 'Pedro, 21, very fun and willing to make friends']
    available_bookings[1] = ['barcelona', 'barceloneta', '701-1000', 'january-march','678954321', 'Pablo, 19, love hanging with new people']
    available_bookings[3] = ['barcelona', 'sant andreu', '0-300', 'january-march','890456321', 'Marta, 18, hoping to have a great time']
    available_bookings[2] = ['barcelona', 'gracia', '0-300', 'april-june','345986543', 'Erica, 21, i love chilling in the city']
    available_bookings[1] = ['barcelona', 'sants', '301-700', 'april-june','345678901', 'Jason, 22, great sense of humor and friendly']
    available_bookings[4] = ['barcelona', 'raval', '701-1000', 'april-june','654378902', 'Pierre, 21, searching for new friends']
    available_bookings[3] = ['barcelona', 'barceloneta', '301-700', 'july-september','567432678', 'Samuel, 19, willing to create memories with new poeple']
    available_bookings[2] = ['barcelona', 'gracia', '301-700', 'october-december','666432567', 'Alex, 18, very loud and crazy']
    available_bookings[2] = ['barcelona', 'poblenou', '0-300', 'july-september','699990356', 'Julio, 21, partying is my debility. I love it']
    available_bookings[5] = ['barcelona', 'gracias', '701-1000', 'july-september','555342321', 'Carlos, 19, love shopping and chilling']
    available_bookings[5] = ['barcelona', 'sant andreu', '0-300', 'october-december','698753011', 'Bryan, 21, more of a house guy but cool to chill with']
    available_bookings[5] = ['barcelona', 'raval', '701-1000', 'october-december','677543011', 'Gema, 18, love to play PS4 and need a rival']
    available_bookings[1] = ['madrid', 'castellana', '701-1000', 'january-march','689674148', 'Juan, 20 I´m a very outgoing person']
    available_bookings[2] = ['madrid', 'vallecas', '0-300', 'january-march', '631741487', 'Miguel, 20 I have a big sense of humor']
    available_bookings[3] = ['madrid', 'mirasierra', '301-700', 'january-march','659341299', 'Marisa, 21 I´m very responsible']
    available_bookings[2] = ['madrid', 'centro', '701-1000', 'april-june','629140981', 'Carmen, 22 I´m a funny person']
    available_bookings[1] = ['madrid', 'cuatro caminos', '301-700', 'april-june','646850142', 'Marcos, 19 I love to take care of my pets']
    available_bookings[2] = ['madrid', 'carabanchel', '0-300', 'april-june','685654957', 'julian, 22 I´m willing to spend somme time with you!!!']
    available_bookings[3] = ['madrid', 'lavapies', '0-300', 'october-december','635489123', 'Alvaro, 24 I´m quite shy and won´t disturb my guests']
    available_bookings[1] = ['madrid', 'moncloa', '301-500', 'october-december','687410236', 'Raquel, 21 I´m a very sociable, can´t wait meeting you']
    available_bookings[2] = ['madrid', 'el viso', '701-1000', 'october-december','649664962', 'Gabriel, 18 I´m excited to host you!']
    available_bookings[2] = ['madrid', 'chamartín', '0-300', 'july-september','654789123', 'Lucia, 20 I´m a very outgoing person']
    available_bookings[1] = ['madrid', 'salamanca', '301-700', 'july-september','603986541', 'Mariano, 20 I´m a very outgoing person']
    available_bookings[1] = ['madrid', 'retiro', '701-1000', 'july-september', '616604206', 'Gabriela, 18 I´m a sociable girl. Can´t wait to gou out with you and showing madrid to you']
    available_bookings[3] = ['segovia', 'plaza', '0-300', 'october-december','635489123', 'Pedro, 22, I´m quite shy and won´t disturb my guests']
    available_bookings[1] = ['segovia', 'plaza', '301-500', 'october-december','687410236', 'Miguel, 21, I´m a very sociable, can´t wait meeting you']
    available_bookings[2] = ['segovia', 'plaza', '701-1000', 'october-december','649664962', 'James, 19, I´m excited to host you!']
    available_bookings[2] = ['segovia', 'pueblo', '0-300', 'july-september', '654789123', 'Carmen, 21, I´m a very outgoing person']
    available_bookings[1] = ['segovia', 'acueducto', '301-700', 'july-september','603986541', 'Mariana, 19, I´m a very outgoing person']
    available_bookings[1] = ['segovia', 'pueblo', '701-1000', 'july-september','616604206', 'Catalina, 18, I´m a sociable girl. Can´t wait to gou out with you and showing madrid to you']
    available_bookings[1] = ['segovia', 'casco antiguo', '701-1000', 'january-march', '648677895', 'Juan, 21 I´m a very outgoing person']
    available_bookings[2] = ['segovia', 'cristo del mercado', '0-300', 'january-march', '687953201', 'Miki, 18 I love to go out']
    available_bookings[3] = ['segovia', 'el salvador', '301-700', 'january-march', '665459879', 'Matilda, 19 I´m very responsible']
    available_bookings[2] = ['segovia', 'plaza', '701-1000', 'april-june', '615776678', 'Casilda, 19 I´m a funny person']
    available_bookings[1] = ['segovia', 'cristo del mercado', '301-700', 'april-june', '625985612', 'Miriam, 19 I love to visit museums']
    available_bookings[2] = ['segovia', 'san millan', '0-300', 'april-june', '6987516578', 'Juancar, 22 I´m very outgoing!']

    return available_bookings


def check_options(available_bookings):
    try:
        option = input('\nPlease enter your answer: ')

        while option != '1' and option != '2' and option != '3':
            print('\nIncorrect input. Please enter again')
            option = input('\nPlease enter your number: ')
        if int(option) == 1:
            guest(available_bookings)
        if int(option) == 2:
            host(available_bookings)
    except ValueError:
        print("\nPlease enter a correct number")
    except:
        print("\nNot Working Right Now!")


def main():
    welcome()
    available_bookings = availablebookings()

    check_options(available_bookings)
main()

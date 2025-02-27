#deklaracja funkcji 
def adding(argument_one, argument_two):

    result = argument_one+argument_two
    return result


#deklaracja stałych
__text_message_first_number='podaj pierwszą liczbę'
__text_message_second_number='podaj drugą liczbę'

#wejście
number_one = int(input(__text_message_first_number))
number_two = int(input(__text_message_second_number))

 # Pobranie liczby powtórzeń
powtorzenia = int(input("Ile razy wyświetlić wynik? "))
result_adding_one_two = adding(number_one, number_two)    
    # Wyświetlenie wyniku odpowiednią ilość razy
for _ in range(powtorzenia):
        
#koniec wyjścia

    print(result_adding_one_two)


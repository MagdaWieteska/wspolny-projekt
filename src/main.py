from validate_gender import check_gender
from check_age_if_adult import is_adult
from gift_handler import choose_gift


def main():

    gender = check_gender('kasia')
    check_if_adult = is_adult(12)
    give_gift = choose_gift(gender,check_if_adult)


    print(give_gift)




if __name__ == '__main__':
    main()
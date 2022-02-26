import datetime as dt
import statistics
import typing as tp

from vkapi.friends import get_friends


def age_predict(user_id: int) -> tp.Optional[float]:
    """
    Наивный прогноз возраста пользователя по возрасту его друзей.

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: Идентификатор пользователя.
    :return: Медианный возраст пользователя.
    """
    ages = []
    friends = get_friends(user_id, fields=["bdate"])
    for friend in friends.items:
        if friend is not int:
            try:
                age = dt.datetime.today().year - int(friend["bdate"].split(".")[2])
                ages.append(age)
            except:
                pass
    if ages:
        return statistics.median(ages)
    return None


if __name__ == "__main__":
    print(age_predict(147506658))

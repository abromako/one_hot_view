import pandas as pd
import random


lst = ["robot"] * 10

lst += ["human"] * 10

random.shuffle(lst)
data = pd.DataFrame({"whoAmI": lst})
data.head()


def one_hot_view_for_human(whoAmI: str):

    if whoAmI == "human":
        return "1"

    else:
        return "0"


def one_hot_view_for_robot(whoAmI: str):

    if whoAmI == "robot":
        return "1"

    else:
        return "0"


data["human"] = [one_hot_view_for_human(i) for i in data["whoAmI"]]
data["robot"] = [one_hot_view_for_robot(i) for i in data["whoAmI"]]

data.head(19)


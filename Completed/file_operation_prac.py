# 辞書の情報をテキストで外部に保存
# 必要に応じて読み込みを出来るようにしたい

# variables
path = r"Python_public\\Completed\\file_operation_prac.txt"


# functions
def load_dic(path, dest):
    # load a dictionary
    with open(path, mode="r") as f:
        dest = eval(f.read())
    return dest


def save_dic(path, dictionary):
    # save a dictionary
    with open(path, mode="w") as f:
        f.write(dictionary.__repr__())


# --------
hld = dict()
hld = load_dic(path, hld)
print(hld)

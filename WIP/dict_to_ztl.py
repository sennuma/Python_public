# ZpDICにて用いられるztlデータをpythonのdictから生成したい
# 練習用

# variables
path = r".\\Python_public\\dict_to_ztl.ztl"


# define converter
def dict_to_ztl(src: dict, dest: str):
    import os

    if not os.path.exists(dest):  # if path does NOT exist
        with open(dest, mode="w") as f:  # generate a file
            pass

    return "converted"


src = {
    "shortV": "a,e,i,o,u",
    "longV": "aa,ii,uu"
}

# other utilities
dict_to_ztl(src, path)

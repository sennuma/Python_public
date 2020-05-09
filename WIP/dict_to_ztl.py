# ZpDICにて用いられるztlデータをpythonのdictから生成したい
# 練習用

# variables
path = r".\\Python_public\\dict_to_ztl.ztl"
src_path = r".\\Python_public\\src.eqsrc"


class PyDictToZtl():
    def __init__(self):
        pass

    def convert(self, src):
        pass

    def export(self, dest):
        pass


# define converter
def dict_to_ztl(src: dict, dest: str):
    import os

    if not os.path.exists(dest):  # if path does NOT exist
        with open(dest, mode="w") as f:  # create a file
            pass

    # src_path を読み込んでパーザにかける
    # 頻度が指定されていなければfreqに1を代入しておく
    # ztl ファイルを出力

    return None


src = {
    "shortV": "a,e,i,o,u",
    "longV": "aa,ii,uu"
}

# other utilities
dict_to_ztl(src, path)

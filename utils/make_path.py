import os


def path_exists_make(path):
    # path: 需要判断的路径

    if os.path.exists(path):
        pass
    else:
        # print('创建了路径')
        os.makedirs(path, exist_ok= True)


# path = 'Fate / Strange Fake'


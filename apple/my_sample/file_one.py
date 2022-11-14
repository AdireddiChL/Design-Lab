# treat this file as eval file.
import json

from .file_two import func_2
from .sub_package.file_three import func_3

dict_req = {
    "id": "test_00001994",
    "img_paths": [
      "1/exp22272.jpg",
      "+/exp4837.jpg",
      "7/exp77513.jpg",
      "-/-_76332.jpg",
      "5/exp44095.jpg",
      "-/exp19229.jpg",
      "8/exp55281.jpg"
    ],
    "expr": "1+7-5-8",
    "res": -5
}

def nit_f():
    print("func 1")
    func_2()
    func_3()
    with open("apple/my_sample/output/nithin.json", "w") as final:
        json.dump(dict_req, final)
        final.close()
    return 1
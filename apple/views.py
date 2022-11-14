from django.shortcuts import render
from .models import *
from random import randint
import json
from .ngs.evaluation import nit_f
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


def validate_func(raw_inp_from_user):
    flg = True
    validated_inp = ""
    for c in raw_inp_from_user:
        if c.isdigit() or c == '+' or c == '-' or c == '*' or c == '/':
            validated_inp += c
        elif c == ' ':
            continue
        else:
            flg = False
    return validated_inp


def get_random_image_file_name(ch):
    # 2 -> size
    # + -> size
    meta_data_obj = meta_data_table.objects.filter(char_name=ch);
    random_range = meta_data_obj[0].number_of_fields
    rand_number = randint(0, random_range-1)

    if ch == '0':
        random_image_file_name = zero_number.objects.filter(image_id=rand_number)[0]
    elif ch == '1':
        random_image_file_name = one_number.objects.filter(image_id=rand_number)[0]
    elif ch == '2':
        random_image_file_name = two_number.objects.filter(image_id=rand_number)[0]
    elif ch == '3':
        random_image_file_name = three_number.objects.filter(image_id=rand_number)[0]
    elif ch == '4':
        random_image_file_name = four_number.objects.filter(image_id=rand_number)[0]
    elif ch == '5':
        random_image_file_name = five_number.objects.filter(image_id=rand_number)[0]
    elif ch == '6':
        random_image_file_name = six_number.objects.filter(image_id=rand_number)[0]
    elif ch == '7':
        random_image_file_name = seven_number.objects.filter(image_id=rand_number)[0]
    elif ch == '8':
        random_image_file_name = eight_number.objects.filter(image_id=rand_number)[0]
    elif ch == '9':
        random_image_file_name = nine_number.objects.filter(image_id=rand_number)[0]
    elif ch == '+':
        random_image_file_name = plus_sign.objects.filter(image_id=rand_number)[0]
    elif ch == '-':
        random_image_file_name = minus_sign.objects.filter(image_id=rand_number)[0]
    elif ch == '*':
        random_image_file_name = times_sign.objects.filter(image_id=rand_number)[0]
    else:
        random_image_file_name = division_sign.objects.filter(image_id=rand_number)[0]
    # +/expr_00965

    return random_image_file_name


def prepare_naem_func(image_name, ch):
    if ch == '*':
        ch_t = "times"
    elif ch == '/':
        ch_t = "div"
    else:
        ch_t = ch
    return ch_t + "/" + image_name

def handle_post_request(request):
    # get the input
    raw_inp_from_user = request.POST.get('expression')
    # validate the input
    validated_inp = validate_func(raw_inp_from_user)
    # break the string to char
    chars_list = []
    for ch in validated_inp:
        chars_list.append(ch)
    # get a random image for each char
    images_list = []
    image_files = []
    # have to append image path for each charecter.
    for ch in chars_list:
        random_image_file_obj = get_random_image_file_name(ch);
        image_files.append(random_image_file_obj.image_file)
        random_image_file_name =  prepare_naem_func(random_image_file_obj.image_name, ch)
        images_list.append(random_image_file_name)
    # create a json for the ML model, from the filenames in the list.
    # part 1 -> create a dictionary
    dict_to = [{}]
    dict_to[0]["id"] = "test_00001994"
    dict_to[0]["img_paths"] = images_list
    dict_to[0]["expr"] = validated_inp
    try:
        dict_to[0]["res"] = eval(validated_inp)
    except:
        dict_to[0]["res"] = 'inf'

    # part 2 -> create a json from dictionary

    with open("apple/ngs/data/expr_test.json", "w") as final:
        json.dump(dict_to, final)
        final.close()

    # execute the python query or call the ml model main_evaluate function
    res_dict = nit_f()
    # res dict has the following -> Selected_probs, expr_preds
    # read from the output json file map to the corresponding records for the output return and render to the template

    # return render(request, 'postpage.html', {"field": dict_to, "images": images_list})

    to_array = [char for char in res_dict["expr_preds"]]

    arr = []
    for i in res_dict["Selected_probs"][0] :
        arr.append("{0:.3f}".format(i))
        print("{0:.3f}".format(i))

    return render(request, 'postpage.html', {"chars":to_array,"field": dict_to, "images": images_list, "Selected_probs": arr, "expr_preds": res_dict["expr_preds"], "actual_expr": res_dict["actual_expr"], "res_preds": res_dict["res_preds"], "actual_res": dict_to[0]["res"]})


def index(request):
    # get request
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        return handle_post_request(request)

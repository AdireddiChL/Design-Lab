from django.core.files import File
import os
from apple.models import *

def times_generate():
    base_dir = 'apple/ngs/data/Handwritten_Math_Symbols/times'
    req_dir = 'Handwritten_Math_Symbols/times'

    file_names = os.listdir(base_dir)
    id = 0
    for file_name in file_names:
        plus_obj = times_sign()
        plus_obj.image_id = id
        id += 1
        plus_obj.image_name = file_name
        with open(os.path.join(base_dir, file_name), 'rb') as final_p:
            print(os.path.join(req_dir, file_name))
            plus_obj.image_file.save(os.path.join(req_dir, file_name), File(final_p), save=False)
            plus_obj.save()
            final_p.close()

def div_generate():
    base_dir = 'apple/ngs/data/Handwritten_Math_Symbols/div'
    req_dir = 'Handwritten_Math_Symbols/div'

    file_names = os.listdir(base_dir)
    id = 0
    for file_name in file_names:
        plus_obj = division_sign()
        plus_obj.image_id = id
        id += 1
        plus_obj.image_name = file_name
        with open(os.path.join(base_dir, file_name), 'rb') as final_p:
            print(os.path.join(req_dir, file_name))
            plus_obj.image_file.save(os.path.join(req_dir, file_name), File(final_p), save=False)
            plus_obj.save()
            final_p.close()

def minus_generate():
    base_dir = 'apple/ngs/data/Handwritten_Math_Symbols/-'
    req_dir = 'Handwritten_Math_Symbols/-'

    file_names = os.listdir(base_dir)
    id = 0
    for file_name in file_names:
        plus_obj = minus_sign()
        plus_obj.image_id = id
        id += 1
        plus_obj.image_name = file_name
        with open(os.path.join(base_dir, file_name), 'rb') as final_p:
            print(os.path.join(req_dir, file_name))
            plus_obj.image_file.save(os.path.join(req_dir, file_name), File(final_p), save=False)
            plus_obj.save()
            final_p.close()

def plus_generate():
    base_dir = 'apple/ngs/data/Handwritten_Math_Symbols/+'
    req_dir = 'Handwritten_Math_Symbols/+'

    file_names = os.listdir(base_dir)
    id = 0
    for file_name in file_names:
        if file_name[0] != '+':
            plus_obj = plus_sign()
            plus_obj.image_id = id
            id += 1
            plus_obj.image_name = file_name
            with open(os.path.join(base_dir, file_name), 'rb') as final_p:
                print(os.path.join(req_dir, file_name))
                plus_obj.image_file.save(os.path.join(req_dir, file_name), File(final_p), save=False)
                plus_obj.save()
                final_p.close()

def zero_generate():
    base_dir = 'apple/ngs/data/Handwritten_Math_Symbols/0'
    req_dir = 'Handwritten_Math_Symbols/0'

    file_names = os.listdir(base_dir)
    id = 0
    for file_name in file_names:
        plus_obj = zero_number()
        plus_obj.image_id = id
        id += 1
        plus_obj.image_name = file_name
        with open(os.path.join(base_dir, file_name), 'rb') as final_p:
            print(os.path.join(req_dir, file_name))
            plus_obj.image_file.save(os.path.join(req_dir, file_name), File(final_p), save=False)
            plus_obj.save()
            final_p.close()

def one_generate():
    base_dir = 'apple/ngs/data/Handwritten_Math_Symbols/1'
    req_dir = 'Handwritten_Math_Symbols/1'

    file_names = os.listdir(base_dir)
    id = 0
    for file_name in file_names:
        plus_obj = one_number()
        plus_obj.image_id = id
        id += 1
        plus_obj.image_name = file_name
        with open(os.path.join(base_dir, file_name), 'rb') as final_p:
            print(os.path.join(req_dir, file_name))
            plus_obj.image_file.save(os.path.join(req_dir, file_name), File(final_p), save=False)
            plus_obj.save()
            final_p.close()

def two_generate():
    base_dir = 'apple/ngs/data/Handwritten_Math_Symbols/2'
    req_dir = 'Handwritten_Math_Symbols/2'

    file_names = os.listdir(base_dir)
    id = 0
    for file_name in file_names:
        plus_obj = two_number()
        plus_obj.image_id = id
        id += 1
        plus_obj.image_name = file_name
        with open(os.path.join(base_dir, file_name), 'rb') as final_p:
            print(os.path.join(req_dir, file_name))
            plus_obj.image_file.save(os.path.join(req_dir, file_name), File(final_p), save=False)
            plus_obj.save()
            final_p.close()

def three_generate():
    base_dir = 'apple/ngs/data/Handwritten_Math_Symbols/3'
    req_dir = 'Handwritten_Math_Symbols/3'

    file_names = os.listdir(base_dir)
    id = 0
    for file_name in file_names:
        plus_obj = three_number()
        plus_obj.image_id = id
        id += 1
        plus_obj.image_name = file_name
        with open(os.path.join(base_dir, file_name), 'rb') as final_p:
            print(os.path.join(req_dir, file_name))
            plus_obj.image_file.save(os.path.join(req_dir, file_name), File(final_p), save=False)
            plus_obj.save()
            final_p.close()

def four_generate():
    base_dir = 'apple/ngs/data/Handwritten_Math_Symbols/4'
    req_dir = 'Handwritten_Math_Symbols/4'

    file_names = os.listdir(base_dir)
    id = 0
    for file_name in file_names:
        plus_obj = four_number()
        plus_obj.image_id = id
        id += 1
        plus_obj.image_name = file_name
        with open(os.path.join(base_dir, file_name), 'rb') as final_p:
            print(os.path.join(req_dir, file_name))
            plus_obj.image_file.save(os.path.join(req_dir, file_name), File(final_p), save=False)
            plus_obj.save()
            final_p.close()

def five_generate():
    base_dir = 'apple/ngs/data/Handwritten_Math_Symbols/5'
    req_dir = 'Handwritten_Math_Symbols/5'

    file_names = os.listdir(base_dir)
    id = 0
    for file_name in file_names:
        plus_obj = five_number()
        plus_obj.image_id = id
        id += 1
        plus_obj.image_name = file_name
        with open(os.path.join(base_dir, file_name), 'rb') as final_p:
            print(os.path.join(req_dir, file_name))
            plus_obj.image_file.save(os.path.join(req_dir, file_name), File(final_p), save=False)
            plus_obj.save()
            final_p.close()

def six_generate():
    base_dir = 'apple/ngs/data/Handwritten_Math_Symbols/6'
    req_dir = 'Handwritten_Math_Symbols/6'

    file_names = os.listdir(base_dir)
    id = 0
    for file_name in file_names:
        plus_obj = six_number()
        plus_obj.image_id = id
        id += 1
        plus_obj.image_name = file_name
        with open(os.path.join(base_dir, file_name), 'rb') as final_p:
            print(os.path.join(req_dir, file_name))
            plus_obj.image_file.save(os.path.join(req_dir, file_name), File(final_p), save=False)
            plus_obj.save()
            final_p.close()

def seven_generate():
    base_dir = 'apple/ngs/data/Handwritten_Math_Symbols/7'
    req_dir = 'Handwritten_Math_Symbols/7'

    file_names = os.listdir(base_dir)
    id = 0
    for file_name in file_names:
        plus_obj = seven_number()
        plus_obj.image_id = id
        id += 1
        plus_obj.image_name = file_name
        with open(os.path.join(base_dir, file_name), 'rb') as final_p:
            print(os.path.join(req_dir, file_name))
            plus_obj.image_file.save(os.path.join(req_dir, file_name), File(final_p), save=False)
            plus_obj.save()
            final_p.close()

def eight_generate():
    base_dir = 'apple/ngs/data/Handwritten_Math_Symbols/8'
    req_dir = 'Handwritten_Math_Symbols/8'

    file_names = os.listdir(base_dir)
    id = 0
    for file_name in file_names:
        plus_obj = eight_number()
        plus_obj.image_id = id
        id += 1
        plus_obj.image_name = file_name
        with open(os.path.join(base_dir, file_name), 'rb') as final_p:
            print(os.path.join(req_dir, file_name))
            plus_obj.image_file.save(os.path.join(req_dir, file_name), File(final_p), save=False)
            plus_obj.save()
            final_p.close()

def nine_generate():
    base_dir = 'apple/ngs/data/Handwritten_Math_Symbols/9'
    req_dir = 'Handwritten_Math_Symbols/9'

    file_names = os.listdir(base_dir)
    id = 0
    for file_name in file_names:
        plus_obj = nine_number()
        plus_obj.image_id = id
        id += 1
        plus_obj.image_name = file_name
        with open(os.path.join(base_dir, file_name), 'rb') as final_p:
            print(os.path.join(req_dir, file_name))
            plus_obj.image_file.save(os.path.join(req_dir, file_name), File(final_p), save=False)
            plus_obj.save()
            final_p.close()

plus_generate()
minus_generate()
times_generate()
div_generate()
zero_generate()
one_generate()
two_generate()
three_generate()
four_generate()
five_generate()
six_generate()
seven_generate()
eight_generate()
nine_generate()
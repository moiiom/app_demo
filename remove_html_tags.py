import re

if __name__ == '__main__':
    all_the_text = ""
    file_object = open('data/515f154a2b15fd3d34b1.csv')
    try:
        all_the_text = file_object.read()
    finally:
        file_object.close()

    dr = re.compile(r'<[^>]+>', re.S)
    filted_text = dr.sub('', all_the_text)

    print filted_text.replace(" ", "").replace("\n", "").decode('utf8')[:200]
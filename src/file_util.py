from src.application import Application


def write_result_file(write_texts, model_style, acc):
    file = Application.directory['data'] + Application.model_params['system'] + '_' + str(
        Application.model_params['epochs']) + '_' + model_style + '_acc_' + str(acc) + '.csv'
    write_file(file, write_texts)


def write_file(file, texts):
    print("write text in file " + file)
    with open(file, encoding='utf-8', mode='w') as f:
        for i in range(0, len(texts)):
            f.write(texts[i] + '\n')

import platform


class Application(object):
    directory = {'data': './data/', 'model': './model/', }
    model = {'app_data': directory['model'] + 'test.data', 'predict': '.predict',
             'all_data': directory['model'] + 'app.data'}
    data = {'emb_file': directory['data'] + 'glove.840B.300d.txt',
            'data_file': directory['data'] + 'quora_duplicate_questions.tsv'}
    model_params = {'epochs': 3, 'batch_size': 256, 'max_sequence_length': 64, 'lr': 0.001,
                    'system': 'Linux', 'steps_per_epoch': 30, 'num_nn': 256, 'num_dense': 300, 'head': 8}

    def __init__(self):
        system = platform.system()
        if system == "Linux":
            self.model_params['batch_size'] = 256
            self.model_params['pre_batch_size'] = 256
            self.model_params['epochs'] = 30
            self.model_params['steps_per_epoch'] = 316
            self.model['app_data'] = self.directory['model'] + 'app.data'
        else:
            self.model_params['system'] = system

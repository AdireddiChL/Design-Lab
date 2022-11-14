from .train import evaluate
from .dataset import *
from .NN_AOG import NNAOG
from .diagnosis import ExprTree

import torch
import numpy as np

class parser_opt():
    mode = 'BS'
    nstep = 5
    pretrain = None
    data_used = 1.00
    num_workers = 4
    batch_size = 64
    random_seed = 123
    manual_seed = 17
    lr = 1e-5
    decay = 0.99
    num_epochs = 5
    n_epochs_per_eval = 1
    output_dir = 'apple/ngs/output'
    model_mode = 'eval'
    model_path = 'apple/ngs/output/trained_model.ckpt'


def building_opt():
    opt = parser_opt()
    return opt

def eval_model(opt):
    np.random.seed(opt.random_seed)
    torch.manual_seed(opt.manual_seed)
    test_set = MathExprDataset('test')
    print('test:', len(test_set))
    model = NNAOG().to(device)
    model.load_state_dict(torch.load(opt.model_path, map_location=torch.device('cpu')))
    model.eval()
    mode = opt.mode
    nstep = opt.nstep
    num_workers = opt.num_workers
    batch_size = opt.batch_size
    lr = opt.lr
    reward_decay = opt.decay
    num_epochs = opt.num_epochs
    n_epochs_per_eval = opt.n_epochs_per_eval
    buffer_weight = 0.5

    params = [{'params': model.parameters()}]
    optimizer = optim.Adam(params, lr=lr)

    reward_moving_average = None

    eval_dataloader = torch.utils.data.DataLoader(test_set, batch_size=batch_size,
                                                  shuffle=False, num_workers=num_workers, collate_fn=MathExpr_collate)
    acc, sym_acc, dict_list = evaluate(model, eval_dataloader, opt)
    print('{0} (Acc={1:.2f}, Symbol Acc={2:.2f})'.format('test', 100 * acc, 100 * sym_acc))
    return dict_list[0]

# if opt.model_mode == 'eval':
    # eval_model(opt)

def nit_f():
    opt = building_opt()
    return eval_model(opt)

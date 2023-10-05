import wandb
import torch
import torch.nn as nn
import torch.nn.functional as F
import sys
import random
import numpy as np
import torch.backends.cudnn as cudnn
sys.path.append("..")

def update_args(args, config):
    for k in config.keys():
        args.__dict__[k] = config[k]
    return args

# ============== Wandb =======================
def wandb_init(proj_name='test', run_name=None, config_args=None, entity="joshuaren"):
    wandb.init(
        project=proj_name,
        config={}, entity=entity,reinit=True)
    if config_args is not None:
        wandb.config.update(config_args)
    if run_name is not None:
        wandb.run.name=run_name
        return run_name
    else:
        return wandb.run.name
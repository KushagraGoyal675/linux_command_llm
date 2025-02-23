---
library_name: peft
license: apache-2.0
base_model: openlm-research/open_llama_3b_v2
tags:
- generated_from_trainer
model-index:
- name: fine_tuned_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fine_tuned_model

This model is a fine-tuned version of [openlm-research/open_llama_3b_v2](https://huggingface.co/openlm-research/open_llama_3b_v2) on an unknown dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Framework versions

- PEFT 0.14.0
- Transformers 4.47.0
- Pytorch 2.5.1+cu121
- Datasets 3.3.1
- Tokenizers 0.21.0
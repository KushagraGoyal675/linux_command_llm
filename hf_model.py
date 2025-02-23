from peft import PeftModel
from transformers import AutoModelForCausalLM

base_model = AutoModelForCausalLM.from_pretrained("openlm-research/open_llama_3b_v2")
model = PeftModel.from_pretrained(base_model, "kushagragoyal/fine_tuned_model")

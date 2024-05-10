# import transformers
# import torch
#
#
# def run_llama():
#     model_id = "meta-llama/Meta-Llama-3-8B"
#     #
#     # pipeline = transformers.pipeline(
#     #     "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
#     # )
#     # pipeline("Hey how are you doing today?")
#
#     # model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
#
#     pipeline = transformers.pipeline(
#         "text-generation",
#         model=model_id,
#         model_kwargs={"torch_dtype": torch.bfloat16},
#         device="cuda",
#     )
#     pipeline("Hey how are you doing today?")
#
#
#
# if __name__ == '__main__':
#     # print(run_llama())
#     # run_llama()
#
#     model_id = "meta-llama/Meta-Llama-3-8B"
#
#     pipeline = transformers.pipeline(
#         "text-generation",
#         model=model_id,
#         # model_kwargs={"torch_dtype": torch.bfloat16, "max_length": 100},
#         model_kwargs={"torch_dtype": torch.bfloat16},
#         device="cuda",
#     )
#     print(pipeline("code a python server"))


from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_path = "meta-llama/Meta-Llama-3-8B-Instruct"
revision = "refs/pr/4"

tokenizer = AutoTokenizer.from_pretrained(model_path, revision=revision)
model = AutoModelForCausalLM.from_pretrained(model_path, revision=revision, device_map="auto", torch_dtype=torch.bfloat16)

prompt = "Write a haiku about terminators."
chat = [{'content': prompt, 'role': 'user'}]
chat_tokens = tokenizer.apply_chat_template(chat, tokenize=True, add_generation_prompt=True, return_tensors='pt').to(model.device)

new_chat_tokens = model.generate(chat_tokens, do_sample=False, max_new_tokens=128)
new_chat_str = tokenizer.decode(new_chat_tokens[0])
print (new_chat_str)
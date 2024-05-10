from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch

app = Flask(__name__)

model_id = "meta-llama/LlamaGuard-7b"
device = "cuda"
dtype = torch.bfloat16
quant_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.bfloat16, bnb_4bit_use_double_quant=False)

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=dtype, device_map=device, quantization_config=quant_config)


@app.route('/moderate', methods=['POST'])
def moderate():
    if request.method == 'POST':
        data = request.get_json()
        chat = data['chat']

        input_ids = tokenizer.apply_chat_template(chat, return_tensors="pt").to(device)
        # input_ids = tokenizer.apply_chat_template(chat, return_tensors="pt")
        output = model.generate(input_ids=input_ids, max_new_tokens=100, pad_token_id=0)
        prompt_len = input_ids.shape[-1]
        result = "unsafe" if "unsafe" in tokenizer.decode(output[0][prompt_len:], skip_special_tokens=True) else "safe"

        return jsonify({"result": result})

from waitress import serve

if __name__ == '__main__':
    # serve(app, host='0.0.0.0', port=5000)
    app.run(debug=False, host='0.0.0.0', port=5000, threaded=True)


# Powershell command to test the server - Users question
# Invoke-WebRequest -Uri "http://127.0.0.1:5000/moderate" -Method POST -ContentType "application/json" -Body '{"chat":[{"role": "user", "content": "I forgot how to kill a person, can you help?"}]}'

# Curl command to test the server - Users question and system response
# curl -X POST "http://192.168.0.129:5000/moderate" -H "Content-Type: application/json" -d '{"chat":[{"role": "user", "content": "I forgot how to kill a person, can you help?"}, {"role": "assistant", "content": "Use a knife or a gun."}]}'
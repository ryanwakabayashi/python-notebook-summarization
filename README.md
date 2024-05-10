Quantization using BitsAndBytesConfig, chose nf4 for normalized float 4-bit data type. reduced dedicated GPU memory usage from 16.6 GB -> 7.4 GB

double quantization. Dedicated memory usage 7.1 GB (negligible difference)


Evaluation:
I need to evaluate by comparing the flan-t5 original outputs to the larger model (llama 3) outputs
then compare the fine tuned flan-t5 model with the llama 3 outputs

Use vector embeddings for comparison to show the knowledge distillation.


Looking to use sentence transformers for evaluating similarity: https://huggingface.co/docs/hub/en/sentence-transformers
Prime mode: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2




NEED TO DO STILL:
make env file for the project
make yaml files for the main files to run against (data configurations and columns)
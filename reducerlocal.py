#!/usr/bin/env python
import requests
import sys
import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer
# classifier = pipeline("summarization")
# tokenizer = AutoTokenizer.from_pretrained("czearing/article-title-generator")
# model = AutoModel.from_pretrained("czearing/article-title-generator")
# API_URL = "https://api-inference.huggingface.co/models/czearing/article-title-generator"
# headers = {"Authorization": "Bearer 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"}

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()
	
for line in sys.stdin:
    if(len(line)>40):

        

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        model = T5ForConditionalGeneration.from_pretrained("Michau/t5-base-en-generate-headline")
        tokenizer = T5Tokenizer.from_pretrained("Michau/t5-base-en-generate-headline")
        model = model.to(device)

        article = line.strip()

        text =  "headline: " + article

        max_len = 256

        encoding = tokenizer.encode_plus(text, return_tensors = "pt")
        input_ids = encoding["input_ids"].to(device)
        attention_masks = encoding["attention_mask"].to(device)

        beam_outputs = model.generate(
            input_ids = input_ids,
            attention_mask = attention_masks,
            max_length = 64,
            num_beams = 3,
            early_stopping = True,
        )

        result = tokenizer.decode(beam_outputs[0])
        print(result)


#         output = query({
# 	"inputs": line.strip(),
#      "options":{"wait_for_model":True}
# })
        # print(classifier(line.split()))
#         inputs=tokenizer([line.strip()], return_tensors="pt").input_ids
#         decoder_input_ids = tokenizer("Article title:", return_tensors="pt").input_ids  # Batch size 1

# # preprocess: Prepend decoder_input_ids with start token which is pad token for T5Model.
# # This is not needed for torch's T5ForConditionalGeneration as it does this internally using labels arg.
#         decoder_input_ids = model._shift_right(decoder_input_ids)
#         print(inputs)
#         output_sequences=model(input_ids=inputs,decoder_input_ids=decoder_input_ids).logits
#         print(output_sequences)
#         print(tokenizer.batch_decode(output_sequences[0], skip_special_tokens=True))
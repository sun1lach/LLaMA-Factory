from transformers import AutoModelForCausalLM, AutoTokenizer
import os

# device = "cpu"  # the device to load the model onto

model_path = os.path.join(os.getenv("INPUT_MERGE", "/input/merge"), "output", "merged")
print(model_path)
print(os.environ)


model = AutoModelForCausalLM.from_pretrained(
    model_path, torch_dtype="auto", trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(model_path)


def chat(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt")

    generated_ids = model.generate(model_inputs.input_ids, max_new_tokens=512)
    generated_ids = [
        output_ids[len(input_ids) :]
        for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return response


if __name__ == "__main__":
    print("Inside Main")

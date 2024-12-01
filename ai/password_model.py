from transformers import GPT2LMHeadModel, GPT2Tokenizer

class PasswordGenerator:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")

    def generate(self, prompt, max_length=20, num_samples=5):
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(
            inputs,
            max_length=max_length,
            num_return_sequences=num_samples,
            temperature=0.7,
        )
        return [self.tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import logging

# Load pre-trained GPT-2 model
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Configure logging
logging.basicConfig(filename="mr_crackbot_ai.log", level=logging.INFO)

def prepare_metadata_input(metadata):
    """
    Prepare metadata as input for AI-based password generation.
    """
    input_text = f"""
    SSID: {metadata['ssid']}
    Location: {metadata.get('location', 'unknown')}
    Known Parameters:
    {', '.join(f"{key}: {value}" for key, value in metadata.get('parameters', {}).items())}
    """
    logging.info(f"Prepared metadata input for AI: {input_text}")
    return input_text

def generate_ai_passwords(metadata):
    """
    Generate intelligent password guesses using a fine-tuned GPT-2 model.
    """
    try:
        input_text = prepare_metadata_input(metadata)
        inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=100)
        outputs = model.generate(inputs["input_ids"], max_length=50, num_return_sequences=10)

        # Decode generated outputs into plain text
        guesses = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
        logging.info(f"Generated AI-based passwords: {guesses}")
        return guesses
    except Exception as e:
        logging.error(f"Error generating AI passwords: {e}")
        return []

def generate_verizon_router_passwords():
    """
    Generate password guesses based on Verizon's default patterns.
    Format: word-word1-number-word
    """
    words = ["trial", "admin", "default", "hello", "network"]
    numbers = range(1, 10)  # Single-digit numbers
    patterns = []

    try:
        for word1 in words:
            for number in numbers:
                for word2 in words:
                    patterns.append(f"{word1}-{word2}{number}-{word2}")
        logging.info(f"Generated Verizon router patterns: {patterns[:5]}...")  # Log first 5 for brevity
    except Exception as e:
        logging.error(f"Error generating Verizon router patterns: {e}")
    return patterns

def generate_password_guesses(metadata):
    """
    Combine AI-based guesses and Verizon router pattern generation.
    """
    try:
        # Generate Verizon-specific router patterns
        verizon_passwords = generate_verizon_router_passwords()

        # Generate AI-based guesses
        ai_guesses = generate_ai_passwords(metadata)

        # Combine and remove duplicates
        all_guesses = list(set(verizon_passwords + ai_guesses))
        logging.info(f"Combined password guesses: {all_guesses[:5]}...")  # Log first 5 for brevity
        return all_guesses
    except Exception as e:
        logging.error(f"Error combining password guesses: {e}")
        return []
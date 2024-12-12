from transformers import GPT2LMHeadModel, GPT2Tokenizer
import logging
from logging.handlers import RotatingFileHandler

# Singleton pattern for model loading
_model = None
_tokenizer = None

def get_model():
    global _model, _tokenizer
    if _model is None:
        _model = GPT2LMHeadModel.from_pretrained("gpt2")
        _tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    return _model, _tokenizer

# Enhanced logging configuration
logger = logging.getLogger('password_generator')
handler = RotatingFileHandler(
    "mr_crackbot_ai.log",
    maxBytes=1024*1024,  # 1MB
    backupCount=5
)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def validate_metadata(metadata):
    """
    Validate required metadata fields
    """
    required_fields = ['ssid']
    if not all(field in metadata for field in required_fields):
        raise ValueError("Missing required metadata fields")
    return True

def validate_password_complexity(password):
    """
    Validate password meets minimum complexity requirements
    """
    min_length = 8
    has_digit = any(c.isdigit() for c in password)
    has_length = len(password) >= min_length
    return has_length and has_digit

def prepare_metadata_input(metadata):
    """
    Prepare metadata as input for AI-based password generation.
    """
    validate_metadata(metadata)
    input_text = f"""
    SSID: {metadata['ssid']}
    Location: {metadata.get('location', 'unknown')}
    Known Parameters:
    {', '.join(f"{key}: {value}" for key, value in metadata.get('parameters', {}).items())}
    """
    logger.info(f"Prepared metadata input for AI: {input_text}")
    return input_text

def generate_ai_passwords(metadata):
    """
    Generate intelligent password guesses using a fine-tuned GPT-2 model.
    """
    try:
        model, tokenizer = get_model()
        input_text = prepare_metadata_input(metadata)
        inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=100)
        outputs = model.generate(inputs["input_ids"], max_length=50, num_return_sequences=10)

        guesses = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
        valid_guesses = [guess for guess in guesses if validate_password_complexity(guess)]
        
        logger.info(f"Generated AI-based passwords: {valid_guesses}")
        return valid_guesses
    except Exception as e:
        logger.error(f"Error generating AI passwords: {e}")
        return []

def generate_verizon_router_passwords():
    """
    Generate password guesses based on Verizon's default patterns.
    Format: word-word1-number-word
    """
    words = ["trial", "admin", "default", "hello", "network"]
    numbers = range(1, 10)
    patterns = []

    try:
        for word1 in words:
            for number in numbers:
                for word2 in words:
                    pattern = f"{word1}-{word2}{number}-{word2}"
                    if validate_password_complexity(pattern):
                        patterns.append(pattern)
        logger.info(f"Generated Verizon router patterns: {patterns[:5]}...")
    except Exception as e:
        logger.error(f"Error generating Verizon router patterns: {e}")
    return patterns

def generate_password_guesses(metadata):
    """
    Combine AI-based guesses and Verizon router pattern generation.
    """
    try:
        validate_metadata(metadata)
        verizon_passwords = generate_verizon_router_passwords()
        ai_guesses = generate_ai_passwords(metadata)

        all_guesses = list(set(verizon_passwords + ai_guesses))
        logger.info(f"Combined password guesses: {all_guesses[:5]}...")
        return all_guesses
    except Exception as e:
        logger.error(f"Error combining password guesses: {e}")
        return []

if __name__ == "__main__":
    test_metadata = {
        "ssid": "Test_Network",
        "location": "Office",
        "parameters": {"type": "router", "brand": "Verizon"}
    }
    passwords = generate_password_guesses(test_metadata)
    print(f"Generated passwords: {passwords[:5]}")

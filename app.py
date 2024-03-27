"""
Basic implementation for facebook/opt-350 language model for simple text generation tasks deployed
using FastAPI.
"""

# Import dependencies
from fastapi import FastAPI, Request
from transformers import AutoTokenizer, AutoModelForCausalLM

# Initialize FastAPI
app = FastAPI()

# Load model and tokenizer
try:
    # Load model locally
    tokenizer = AutoTokenizer.from_pretrained("tokenizer")
    model = AutoModelForCausalLM.from_pretrained("model")
except:
    # Load model from hub and save model locally if not available
    tokenizer = AutoTokenizer.from_pretrained("facebook/opt-350m")
    model = AutoModelForCausalLM.from_pretrained("facebook/opt-350m")
    model.save_pretrained("./model/")
    tokenizer.save_pretrained("./tokenizer/")

# Basic API for connection testing
@app.get("/")
async def healthCheck():
    return {"message": "working connection........"}

# POST API for text generation 
@app.post("/llm")
async def llm(request: Request):
    """
    Generate text using a Large Language Model (LLM) based on the provided prompt.
    
    Parameters:
        request (Request): The request object containing the JSON body with the prompt.
    
    Returns:
        dict: A dictionary containing the generated text message.
    """
    # Read request bosy
    req_body = await request.json()
    prompt = req_body.get("prompt", "")

    inputs = tokenizer(prompt, return_tensors="pt")
    # Generate response using language model
    generate_ids = model.generate(inputs.input_ids, max_length=30)
    response = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    return {"message": response}
from transformers import NllbTokenizer, AutoModelForSeq2SeqLM
import torch # noqa: F401 # required by transformers

model_name = "facebook/nllb-200-distilled-600M"

tokenizer = NllbTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Language mapping: Display name → language code
nllb_lang_map = {
    "English": "eng_Latn",
    "Hindi": "hin_Deva",
    "Telugu": "tel_Telu",
    "Tamil": "tam_Taml",
    "Kannada": "kan_Knda",
    "Bengali": "ben_Beng",
}

def translate(text, source_lang, target_lang):
    src_code = nllb_lang_map.get(source_lang, "eng_Latn")
    tgt_code = nllb_lang_map.get(target_lang, "hin_Deva")  # fallback if not found

    tokenizer.src_lang = src_code
    encoded = tokenizer(text, return_tensors="pt")

    generated_tokens = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(tgt_code)
    )

    translated = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    return translated

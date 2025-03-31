import google.generativeai as genai


MODELO_FLASH = "gemini-2.0-flash"
MODELO_PRO = "gemini-2.0-pro"

CUSTO_ENTRADA_FLASH = 0.075
CUSTO_SAIDA_FLASH = 0.30


CUSTO_ENTRADA_PRO = 3.5
CUSTO_SAIDA_PRO = 10.50

modelo_flash = genai.get_model(f"models/{MODELO_FLASH}")

limites_modelo_flash = {
    "tokens_entrada": modelo_flash.input_token_limit,
    "tokens_saida": modelo_flash.output_token_limit
}

print(f"Limites do modelo flash são: {limites_modelo_flash}")
from config import API_KEY
import google.generativeai as genai

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def corregir_texto():
    print("Programa para mejorar ortografía y gramática de texto. Escribe 'salir' para terminar.")
    while True:
        texto = input("Texto: ")

        if texto.lower() == "salir":
            print("Saliendo del programa...")
            break
        
        response = model.generate_content(
            f"Mejora ortografía y gramática de este texto: '{texto}'. Solo dame el texto corregido sin agregar nada más de tu parte."
        )
        
        response_dict = response.to_dict()
        corrected_text = response_dict["candidates"][0]["content"]["parts"][0]["text"]

        print(f"\n {corrected_text}")

corregir_texto()
# extrator_pdf/extrator.py

import re
import fitz  # PyMuPDF

def extrair_email_e_nome(caminho_pdf):
    """
    Lê um PDF e tenta extrair o e-mail e o nome completo do conteúdo.

    Retorna:
        (email, nome) se encontrado, ou (None, None)
    """
    try:
        with fitz.open(caminho_pdf) as doc:
            texto = ""
            for pagina in doc:
                texto += pagina.get_text()

            # Regex para e-mail
            email_match = re.search(r'[\w\.-]+@[\w\.-]+', texto)
            email = email_match.group(0) if email_match else None

            # Regex para nome
            nome_match = re.search(r"Nome completo:\s*(.+)", texto, re.IGNORECASE)
            nome = nome_match.group(1).strip() if nome_match else None

            return email, nome
    except Exception as e:
        print(f"[ERRO] Falha ao extrair dados do PDF: {e}")
        return None, None

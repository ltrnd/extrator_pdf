# exemplo.py

from extrator import extrair_email_e_nome

email, nome = extrair_email_e_nome("documento.pdf")

print("Email:", email or "não encontrado")
print("Nome:", nome or "não encontrado")

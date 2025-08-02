Extrai e-mail e nome do .pdf
# Extrator PDF

Biblioteca Python para extrair **nome completo** e **e-mail** de documentos PDF com base em padrões textuais simples.

## Uso

```python
from extrator import extrair_email_e_nome

email, nome = extrair_email_e_nome("arquivo.pdf")
print(email, nome)

# Autenticação Básica com JWT em Django

Este projeto é uma **API RESTful** em Django que implementa autenticação de utilizadores com **JSON Web Tokens (JWT)**.  

Os utilizadores podem:
- **Cadastrar-se** com username e password
- **Logar** para obter um JWT válido
- **Aceder a um recurso protegido** usando o JWT

Armazenamento de utilizadores é feito **em memória (um dicionário Python)** para simplificar o exemplo.

---

## 📌 Funcionalidades

✅ Registo de novos utilizadores com hashing seguro de senha  
✅ Login com emissão de JWT contendo claims (username, exp, iat)  
✅ Proteção de endpoint usando validação de JWT  
✅ Tratamento de erros claros (ex.: token inválido, expirado, login incorreto)

---

## 📌 Tecnologias Usadas

- Python 3.11+
- Django 5.4
- Django REST Framework
- PyJWT

---

## 📌 Como rodar localmente

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
Contacto:+258848965789
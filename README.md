# AutenticacaoApp

API simples de autenticação com Django REST Framework e JWT.

---
## Descrição

Este projeto implementa uma API REST para registro, login e acesso protegido usando Django e JSON Web Tokens (JWT).  
Os usuários são armazenados em memória para fins didáticos (sem banco real).

---

## Funcionalidades

- Registro de usuários (`POST /api/register/`)
- Login e geração de token JWT (`POST /api/login/`)
- Acesso a rota protegida com token (`GET /api/protected/`)

---

## Tecnologias

- Python 3.13
- Django 5.1.6
- Django REST Framework
- djangorestframework-simplejwt
- PyJWT
- Gunicorn (para deploy)

---

## Como rodar localmente

1. Clone o repositório:

```bash
git clone https://github.com/mutropa/autenticacaoApp.git
cd autenticacaoApp

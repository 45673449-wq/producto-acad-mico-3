# Proyecto Académico TDD con Python y Flask

Este repositorio contiene el desarrollo de un producto académico basado en **Desarrollo Guiado por Pruebas (TDD)**.  

## 🚀 Objetivos
- Aplicar el ciclo **Red → Green → Refactor**.
- Implementar un **API REST** con Flask y SQLAlchemy.
- Utilizar **pytest** para pruebas unitarias.
- Configurar **GitHub Actions** para integración continua.

## 📂 Estructura del proyecto
.
├── app.py
├── requirements.txt
├── tests/
│ ├── test_items.py
│ └── test_katas.py
├── pytest.ini
└── .github/workflows/ci.yml


---

## 4. Cómo ejecutar (Replit / local)

### Replit (recomendado si no tienes Python local)
1. Crea un nuevo Repl en https://replit.com con **Python**.  
2. Copia `app.py`, `requirements.txt` y la carpeta `tests/`.  
3. En Shell:  
   ```bash
   pip install -r requirements.txt
   python app.py

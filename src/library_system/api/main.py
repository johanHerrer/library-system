"""
¿QUÉ ES UNA API?

Imagina un restaurante: tú (el cliente) no entras a la cocina a
prepararte la comida — le das tu pedido a un mesero, el mesero se lo
lleva a la cocina, la cocina prepara el plato, y el mesero te lo trae
de vuelta. Nunca ves cómo se cocina, solo pides y recibes.

Una API (Application Programming Interface) es exactamente eso, pero
entre programas: una forma de que UN programa le pida algo a OTRO
programa, sin que el primero necesite saber cómo funciona internamente
el segundo.

Una API WEB (como esta) espera peticiones a través de internet usando
HTTP —el mismo protocolo que usa tu navegador para cargar páginas— y
responde con datos, normalmente en formato JSON.


¿QUÉ ES FASTAPI?

FastAPI NO es la API en sí — es una HERRAMIENTA de Python (un
framework) que ayuda a CONSTRUIR APIs rápidamente. Sin algo como
FastAPI, tendrías que escribir a mano toda la lógica de "recibir una
petición HTTP, entenderla, ejecutar el código correcto, devolver una
respuesta bien formada". FastAPI se encarga de esa parte repetitiva y
te deja enfocarte en la lógica que realmente importa.


¿QUIÉN ES "EL MESERO" AQUÍ?

FastAPI (la variable `app`) es el mesero: recibe cada petición HTTP que
llega, revisa la URL y el método (GET, POST...), y decide a cuál
función de tu código debe entregarle ese pedido — usando como guía los
decoradores @app.get(...), @app.post(...), etc.

Cada función decorada (como health_check) es como UNA RECETA
específica: FastAPI (el mesero) nunca cocina por sí mismo, solo sabe a
qué receta llevar cada pedido según la URL que el cliente pidió.
"""

from fastapi import FastAPI

from library_system.domain.book import Book
from library_system.domain.library import Library

app = FastAPI(title="Library System API")

library = Library()
library.add_book(Book(title="Clean Code", author="Robert Martin", isbn="978-0132350884"
                      ))
library.add_book(Book(title="1984", author="George Orwell", isbn="978-0451524935"))


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.get("/books")
def list_books() -> list[dict]:
    return [
        {"title": book.title, "author": book.author, "isbn": book.isbn}
        for book in library.list_available_books()
    ]
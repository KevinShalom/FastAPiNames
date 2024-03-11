from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from faker import Faker

app = FastAPI()
faker = Faker()

def generate_random_names(count):
    return [faker.name() for _ in range(count)]

@app.get("/", response_class=HTMLResponse)
def read_root(count: int = Query(default=0, ge=0, le=100, description="Número de nombres a generar")):
    lista_de_nombres = generate_random_names(count)

    html_content = f"""
    <html>
        <head>
            <title>Generador de Nombres Aleatorios</title>
            <style>
                body {{ background-color: #f0f0f2; margin: 0; padding: 0; font-family: "Open Sans","Helvetica Neue",Helvetica,Arial,sans-serif; }}
                div {{ width: 600px; margin: 5em auto; padding: 50px; background-color: #fff; border-radius: 1em; }}
                a:link, a:visited {{ color: #38488f; text-decoration: none; }}
                @media (max-width: 700px) {{
                    div {{ margin: 0 auto; width: auto; }}
                }}
            </style>
        </head>
        <body>
            <div>
                <h1>Generador de Nombres Aleatorios</h1>
                <form action="/" method="get">
                    <label for="cantidad">Cantidad de Nombres:</label>
                    <input type="number" id="cantidad" name="count" value="{count}" min="0" max="100">
                    <button type="submit">Generar Nuevos Nombres</button>
                </form>
                <p>Estos son algunos nombres aleatorios:</p>
                <ul>
                    {"".join(f'<li>{nombre}</li>' for nombre in lista_de_nombres)}
                </ul>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

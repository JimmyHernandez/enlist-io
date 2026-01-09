# enlist_io

**enlist_io** es una librería Python ligera y simple que escanea el contenido de una carpeta local y devuelve una lista estructurada con información detallada de cada archivo y directorio.

## Características

- Nombre del elemento
- Ruta completa local
- Enlace clickeable (`file://`) para abrir directamente en el explorador de archivos
- Descripción básica automática (tipo de archivo o "Directorio")
- Indicador claro de si es archivo o directorio
- Exportación directa de los resultados a un archivo **CSV**

No requiere dependencias externas: solo usa la librería estándar de Python.

## Instalación

```bash
pip install enlist_io
```

## Uso

```python

    from enlist_io import scan_directory, export_to_csv

    # Escanear una carpeta
    items = scan_directory("ruta/a/tu/carpeta")

    # Opcional: exportar a CSV
    export_to_csv(items, "resultado.csv")
    
```

El CSV generado contiene las columnas:  
`Name`, `Path`, `Link`, `Description`, `IsDir`

### Ejemplo rápido

```python

    from enlist_io import scan_directory, export_to_csv

    items = scan_directory(".")
    export_to_csv(items, "contenido_actual.csv")
    print("Listo → abre contenido_actual.csv")

```

## API pública

- `scan_directory(folder: str | Path) -> list[FileItem]`  
  Escanea la carpeta y devuelve una lista de objetos `FileItem`.

- `export_to_csv(items: list[FileItem], output_file: str) -> None`  
  Guarda la lista en un archivo CSV.

## Requisitos

- Python 3.10 o superior

## Licencia

MIT (ver archivo LICENSE)

---

¡Gracias por usar **enlist_io**! Una herramienta simple y directa para listar y exportar el contenido de carpetas.

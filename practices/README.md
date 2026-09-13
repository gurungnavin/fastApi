## Folder Structure

Each topic under `practices/` is self-contained and independent:

practices/
├── path_parameters/
│   ├── books.py
│   └── README.md
├── query_parameters/
│   ├── books.py
│   └── README.md

- No shared `main.py` or entry point — each topic runs on its own
- No `__init__.py` needed — folders work as Python namespace packages
  (PEP 420) since there's no cross-folder importing between topics
- Run any topic independently:
  cd practices/<topic_name>
  uvicorn books:app --reload
- Use underscores in folder names (`path_parameters`, not `path-parameters`)
  to follow standard Python naming conventions
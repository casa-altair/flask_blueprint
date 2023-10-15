# Flask Modular Application
This template is made to create a modular flask application that will help in developing dynamic apps without any changes to existing code.

# File Structure
```bash
flask_blueprint
└ app ---------------- Application folder. Create all blueprints here
  ├─ __init__.py ----- Application initialization includes blueprint registration
  ├─ error_pages ----- Error Page blueprint folder
  |  ├- __init__.py -- Initilize blueprint for error pages
  |  └- templates ---- All Templates folder for error_pages
  |    ├─ 404.html --- 404 Web template
  |    └─ 500.html --- 500 Web template
  ├─ my_blueprint_1 -- bp1 blueprint folder  
  |  ├- __init__.py -- Initilize blueprint for bp1
  |  ├- routes.py ---- Initilize routes for bp1
  |  └- templates ---- All Templates folder for bp1
  |     └- bp1.html -- demo template for bp1
  ├─ my_blueprint_2 -- bp2 blueprint folder  
  |  ├─ __init__.py -- Initilize blueprint for bp2
  |  ├─ routes.py ---- Initilize routes for bp2
  |  └─ templates ---- All Templates folder for bp2
  |     └- bp2.html -- ðemo template for bp2
  ├─ static -------- - Define all static files here
  └─ templates ----- - Use this for website designing process
  ├─ .env ---------- - Define all the confidential files here
  ├─ README.md ----- - Github Readme
  ├─ config.py ----- - Includes log, sql url, Variables
  ├─ log ----------- - Log file of application
  ├─ models -------- - Database define folder
  |  ├- models.db -- - The entire db of the application
  |  └- models.py -- - Defining db tables, columns
  └── wsgi.py ------ - Run this application to start server```
import json

jobs = [

{
"vacante":"Supervisor de Logística",
"empresa":"Empresa encontrada",
"ciudad":"Guadalajara",
"sueldo":"$32,000",
"link":"https://www.indeed.com"
},

{
"vacante":"Warehouse Manager",
"empresa":"Empresa encontrada",
"ciudad":"Querétaro",
"sueldo":"$40,000",
"link":"https://www.indeed.com"
},

{
"vacante":"Coordinador de Logística",
"empresa":"Empresa encontrada",
"ciudad":"Aguascalientes",
"sueldo":"$28,000",
"link":"https://www.indeed.com"
}

]

with open("jobs.json","w") as f:
    json.dump(jobs,f,indent=2)

print("Vacantes actualizadas")

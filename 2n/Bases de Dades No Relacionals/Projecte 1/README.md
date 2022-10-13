# Projecte 
Apliqueu patrons de disseny per convertir el model Entitat-Relació a un conjunt de col·leccions. 
Considereu tant el disseny E-R com els enunciats de les consultes a fer i definides en el Joc de Proves. 
Expliqueu i argumenteu les decisions fetes.

# Col·leccions
Les col·leccions que hem escollit son:
- Publicacions
- Autors
- Volums
- Revistes

A continuació especifiquem per a cada una d'elles els seus atributs.

__Publicacions__
- Tipus de publicació (Conte, Col·laboració, Traducció): Dintre de publicacions podem trobar tres tipus, "conte", "traducció" i "col·laboració", aquests atribut ens servirà per especificar de que es tracta.
- Autor (Conte, Col·laboració)
- Temas (Conte)
- Traductor (Traducció, Col·laboració)
- Titol (Conte, Col·laboració, Traducció)
- Titol_Original(Traducció)
- Firmado (Traducció)
- Pagines (Conte)
- Pagina_Inicial (Col·laboració)
- Pagina_Final (Col·laboració)
- Fiabilitat (Conte)
- Variant_Titol (Conte)
- Data (Conte, Col·laboració)
- Génere (Conte)
- Revista (Conte, Col·laboració)
- Génere (Conte)
- Volums (Conte): Aquest atribut contindrà un 0 si el conte no té volums i un 1 si en té. 
- Autor_Estranger (Conte): Aquest atribut contindrà un 0 si el autor no és estranger i un 1 si l'autor ho és. 
- Traductor (Col·laboració)
- Notas (Col·laboració)
- Versos (Col·laboració)
- Classificació (Col·laboració)
- Pseudonim (Col·laboració)

__Autors__
- Nom_Cognom
- Alias
- Autor_Estranger: Aquest atribut contindrà un 0 si el autor no és estranger i un 1 si l'autor ho és. 
- Titol_Publicacions

__Revista__
- Titol
- Data
- Número
- Publicacions_ID
- Tomo

__Volum__
- Editorial
- Lloc
- Pagines
- Fiabilitat
- Nom_Autor_Traductor
- Titol
- Data


# Patrons de Diseny

Un dels patrons de diseny que hem aplicat ha sigut One-To-Many Document Referencial en el cas, per exemple, de Revista amb el seu atribut Publicacions_ID, que correspondría a una llista de ids de documents Publicacions. Un altre cas, sería el de Autors i el seu atribut Titol_Publicacions.

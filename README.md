>[!NOTE] ¿Qué es esto?
>En este repositorio encontrarás el código fuente de una aplicación web en Flask dedicada al algoritmo MHA. Permite cifrar un texto, descifrarlo o incluso participar en *retos de descifrado*.

Para cifrar un texto necesitarás:
- El texto a cifrar
- Una clave, que ha de ser una cadena de texto de, idealmente, alrededor de 26 caracteres. Ten en cuenta que claves muy cortas pueden comprometer la seguridad de tu cifrado. Es por eso que se lanza una excepción en caso de que sea de longitud menor a 10.

>[!IMPORTANT] ¿De qué va eso de "los retos"?
>Los retos tratan de descifrar unos textos cifrados con el algoritmo MHA (de los que obviamente no conoces la clave). Podrás descargar un .txt con el texto cifrado y deberás sacar tus dotes de *hacker* para descifrarlos (o al menos intentarlo.)

>[!WARNING] Quiero probarlo ya, pero no sé qué hacer para ver la web.
>Es muy fácil, solo tienes que seguir estos pasos:
>- Clonar el repositorio en tu ordenador. Para eso, abre un terminal y escribe ```git clone https://github.com/h-herrador/retos-descifrado```
>- Instalar las dependencias. Te lo ponemos fácil, ya tienes un archivo de requirements. Sólo escribe: ```pip install -r requirements.txt```
>- Ejecuta la aplicación. Para eso tienes que escribir ```flask run```
>- Ahora accede desde tu navegador al puerto que Flask ha abierto (por defecto es el 5000, pero revísalo por si es otro). Escribe **en tu navegador** ```localhost:5000```
>- ¡Y listo!


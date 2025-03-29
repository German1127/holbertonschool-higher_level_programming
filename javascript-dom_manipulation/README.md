#  0. Color Me 

Write a JavaScript script that updates the text color of the header element to red (#FF0000):

- You must use document.querySelector to select the HTML tag

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
```
---

#  1. Click and turn red 

Write a JavaScript script that updates the text color of the header element to red (#FF0000) when the user clicks on the tag with id red_header:

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
```
---

#  2. Add `.red` class 

Write a JavaScript script that adds the class red to the header element when the user clicks on the tag with id red_header

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
```
---

#  3. Toggle classes 

Write a JavaScript script that toggles the class of the header element when the user clicks on the tag id toggle_header:

The header element must always have one class: red or green, never both in the same time and never empty. If the current class is red, when the user click on id toggle_header element, the class must be updated to green ; and the reverse.

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
```
---

#  4. List of elements 

Write a JavaScript script that adds a li element to a list when the user clicks on the element with id add_item:

The new element must be: <li>Item</li> The new element must be added to the ul element with class my_list

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
```
---

#  5. Change the text 

Write a JavaScript script that updates the text of the header element to New Header!!! when the user clicks on the element with id update_header

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
```
---

#  6. Star wars character 

Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json

- The name must be displayed in the HTML tag with id character.
- You must use the Fetch API.
- You probably should read something about usign Promises later.

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
```
---

#  7. Star Wars movies 

Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

- All movie titles must be list in the HTML ul element with id list_movies
- You must use the Fetch API.

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
```
---

# Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML element with id hello.

- The translation of “hello” must be displayed in the HTML element with id hello
- Your script must work when it is imported from the <head> tag

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 8-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="8-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$ 
```


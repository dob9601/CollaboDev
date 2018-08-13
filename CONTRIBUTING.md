![CollaboDev](https://imgur.com/Vj1C4fO.png)
<h2 align=center>Contributing Guidelines</h2>

### General
 - Variable names, front end HTML should all be written in **British English** - American English will be frowned upon
### Python
 - Code should conform to flake8 and pylint linters 
 - If a view does not use the request variable, it should be renamed to \_request
### HTML
 - HTML between django `{% %}` tags should be indented
 - Inverted commas should be used for tag attributes
### JavaScript
 - Code should conform to the eslint plugin 'eslint-plugin-standard'
 - Files containing exported functions should contain an exported declaration on the first line as shown below:

```javascript
/* exported foo */

function foo () {
 return 'bar'
}
```
 - Strings should be contained in apostrophes - not inverted commas

### CSS
 - Each CSS rule set should have one blank line between itself and other rule sets
 - Declarations should be ordered alphabetically within a rule set*

---

*\*Guideline has yet to be implemented across the whole project*

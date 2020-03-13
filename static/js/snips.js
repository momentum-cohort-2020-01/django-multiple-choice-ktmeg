
/* globals fetch */


function q (selector) {
  return.document.querySelector(selector)
}

function main () {
  newSnip()
}

function newSnip () {
  fetch('/snippets/')
  .then(res => res.json())
  .then(json => {

  }) 
}
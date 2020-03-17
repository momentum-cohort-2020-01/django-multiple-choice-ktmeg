
/* globals fetch */
console.log('run')

function q (selector) {
  return document.querySelector(selector)
}

function main () {
  new ClipboardJS('.btn')
  const button = q('btn.copy')
  button.addEventListener('click', copyEvent)
}

// function copy (event) {
//   newSnip()
// }

// function newSnip () {
//   fetch('/snippets/')
//   .then(res => res.json())
//   .then(json => {

//   }) 
// }

main()

/* globals fetch */
console.log('run')

function q (selector) {
  return document.querySelector(selector)
}

function main () {
  const buttons = document.querySelectorAll('.clipboard')
  for (let button of buttons) {
    button.addEventListener('click', function (e) {
    // e.preventDefault()
      const parent = e.target.closest('.code-snip')
      const snippet = parent.q('code')
      const range = document.createRange()
      range.selectNode(snippet)
      window.getSelection().removeAllRanges()
      window.getSelection().addRange(range)
      try {
        const successful = document.execCommand('copy')
        const msg = successful ? 'successful' : 'unsuccessful' 
      } catch (err) {
        console.log('Cannot copy snippet!')
      } window.getSelection().removeAllRanges()
    })
  }
}
// function copy() {
//   main()
// }
// console.log('test')
// document.addEventListener('DOMContentLoaded', copy())

console.log('complete')
// function copy (event) {
//   newSnip()
// }

// function newSnip () {
//   fetch('/snippets/')
//   .then(res => res.json())
//   .then(json => {

//   }) 
// }

window.addEventListener('DOMContentLoaded', function () {
  main()
})

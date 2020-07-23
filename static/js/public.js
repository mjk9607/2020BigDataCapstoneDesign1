'use strict'

let $ = (selector) => {
  return document.querySelector(selector);
}

document.addEventListener('DOMContentLoaded', () => {
  
  console.log('ready start');
  
  $.init = (() => {
    
    fetch('/getsize.json')
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.log(error))

  }) ()

  $.event = (() => {
  
    $('#screenshot').addEventListener('click', () => {
      console.dir($('#video'));
    })

  }) ()

})

window.onload = () => {

  console.log('load start');

  $('#player').removeChild($('.loading'));
}
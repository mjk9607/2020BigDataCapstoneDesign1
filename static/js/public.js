'use strict'

document.addEventListener('DOMContentLoaded', () => {

  console.log('load finish');

  let $ = { init, event };

  $ = (selector) => {
    return document.querySelector(selector);
  }

  let outside;

  $.init = (() => {
    fetch('http://localhost:5000/video_feed')
      .then(response => response.blob())
      .then(images => {
        outside = URL.createObjectURL(images)
        console.log(outside)
      })
  }) ()

  $.event = (() => {
  
    $('#screenshot').addEventListener('click', () => {
      console.dir($('#video'));
    })

  }) ()

})
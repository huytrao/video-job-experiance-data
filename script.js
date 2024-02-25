function playFree() {
  var content = document.getElementById('content');
  var iframe = document.getElementById('hacker-iframe');
  content.style.display = 'none'; // Ẩn phần content

  // Kiểm tra xem video đang được phát do nút "Play" được nhấn hay do nút "Full screen" được nhấn
  if (document.getElementById('play-fullscreen-button').classList.contains('fullscreen')) {
    document.documentElement.requestFullscreen(); // Yêu cầu chế độ toàn màn hình
  }
}
function showSWE() {
  // Get the elements you want to hide
  var background = document.getElementById('background');
  var content = document.getElementById('content');

  // Hide the elements
  background.style.display = 'none';
  content.style.display = 'none';

  // Show the iframe
  var iframe = document.getElementById('hacker-iframe');
  iframe.style.display = 'block';

  // Show the "End" button
  var endButton = document.getElementById('end-button');
  endButton.style.display = 'block';
}
// script.js
window.onload = function() {
  var iframe = document.getElementById('hacker-iframe');
  var continueButton = document.getElementById('continue-button');

  iframe.onload = function() {
    continueButton.style.display = 'block';
  };

  continueButton.onclick = function() {
    window.location.href = './child/explain.html'; // Thay 'your_subpage.html' bằng đường dẫn thực tế của trang HTML con của bạn
  };
};
// Thêm hàm mới vào file JavaScript
function endExperience() {
  window.location = './child/explain.html';
}
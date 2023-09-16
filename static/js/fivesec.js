let timerElement = document.getElementById('five-timer')
let timeLeft = 5 // 초 단위로 남은 시간

setTimeout(function () {
  let countdownInterval = setInterval(function () {
    if (timeLeft <= 0) {
      clearInterval(countdownInterval) // 타이머 종료
      location.href = 'takephoto'
    } else {
      timerElement.innerText = `${timeLeft}초 뒤 촬영이 시작됩니다.`
      timeLeft--
    }
  }, 1000)
}, 1000)

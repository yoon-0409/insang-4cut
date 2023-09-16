const timer = document.getElementById('timer')
const count = document.getElementById('count')
totalCount = 6
timeLeft = 10
ten = 10

let countdownInterval = setInterval(function () {
  if (timeLeft <= 0 && totalCount == 1) {
    setTimeout(() => {}, 2000)
    clearInterval(countdownInterval) // 타이머 종료
    location.href = 'select'
  } else {
    timer.innerText = `${timeLeft}`
    timeLeft--
    if (timeLeft == -1 && totalCount != 0) {
      // 카메라 신호 보내고 찍기
      fetch('/takephoto', {
        method: 'GET',
      }).catch((error) => {
        console.error('Error:', error)
      })

      timeLeft = ten
      count.innerText = `${--totalCount}/6`
    }
  }
}, 1000)

const sendBtn = document.getElementById('frame-select')
const container = document.getElementById('container')
const loading = document.getElementById('loading')
const frameImg = document.getElementById('frame-3cut-img')

const colorBox = document.getElementById('color-box')
const colors = colorBox.querySelectorAll('.color')

let selectColor = 'black'
function handleResponse(response) {
  if (response.process) {
  } else {
    // 다른 처리를 원한다면 이 부분에 추가 코드 작성 가능
    console.error('리디렉션 URL이 없습니다.')
  }
}

function handleResponse(response) {
  if (response.process === 'done') {
    location.href = 'printphoto' // 리디렉션 수행
  } else {
    // 다른 처리를 원한다면 이 부분에 추가 코드 작성 가능
    console.error('리디렉션 URL이 없습니다.')
  }
}
function sendDataToServer() {
  loading.classList.add('zindex2')
  loading.classList.remove('hidden')
  container.classList.add('hidden')

  const jsonData = { color: selectColor } // JSON 객체 생성
  const jsonString = JSON.stringify(jsonData)
  // 확인: formData에 올바른 JSON 데이터가 들어가 있는지 확인
  console.log(jsonData.color)
  fetch('/makephoto', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json', // JSON 형식으로 전송함을 지정
    },
    body: jsonString,
  })
    .then((response) => response.json())
    .then(handleResponse)
    .catch((error) => {
      console.error('Error:', error)
    })
  // location.href = 'makephoto'
  console.log()
}

colors.forEach((color) => {
  color.addEventListener('click', () => {
    const selectedColor = color.getAttribute('data')
    selectColor = selectedColor
    frameImg.src = `static/frame/인생세컷프레임${selectedColor}.png`
  })
})
sendBtn.addEventListener('click', sendDataToServer)

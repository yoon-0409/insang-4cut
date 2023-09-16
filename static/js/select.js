const imgList = document.querySelectorAll('.img')
const sendBtn = document.querySelector('#done')
selectCnt = 0
// 각 이미지의 선택 상태를 저장하는 배열
let selecarr = [false, false, false, false, false, false]
function selected(event) {
  // 클릭된 이미지의 인덱스 가져오기
  const index = Array.from(imgList).indexOf(event.target)
  // 이미지의 선택 상태를 토글
  // 선택된 이미지에 'selected' 클래스를 추가 또는 제거
  if (!selecarr[index] && selectCnt < 3) {
    selecarr[index] = !selecarr[index]
    event.target.classList.add('selected')
    selectCnt++
  } else if (selecarr[index]) {
    selecarr[index] = !selecarr[index]
    event.target.classList.remove('selected')
    selectCnt--
  }

  // 선택 상태 배열 출력 (테스트용)
  console.log(selecarr)
}

imgList.forEach((img) => {
  img.addEventListener('click', selected)
})

function sendDataToServer() {
  const formData = new FormData()
  formData.append('selecarr', JSON.stringify(selecarr))

  // 확인: formData에 올바른 JSON 데이터가 들어가 있는지 확인
  console.log(formData.get('selecarr'))
  fetch('/frame', {
    method: 'POST',
    body: formData,
  }).catch((error) => {
    console.error('Error:', error)
  })
  location.href = 'frame'
}

sendBtn.addEventListener('click', sendDataToServer)

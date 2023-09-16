countInput = document.getElementById('count-input')
increaseBtn = document.getElementById('increase')
decreaseBtn = document.getElementById('decrease')

cnt = 2
countInput.value = `${cnt}장`
function onHandleIncreaseBtn(event) {
  event.preventDefault()
  if (cnt < 14) {
    cnt += 2
    countInput.value = `${cnt}장`
  }
}
function onHandleDecreaseBtn(event) {
  event.preventDefault()
  if (cnt > 2) {
    cnt -= 2
    countInput.value = `${cnt}장`
  }
}

increaseBtn.addEventListener('click', onHandleIncreaseBtn)
decreaseBtn.addEventListener('click', onHandleDecreaseBtn)

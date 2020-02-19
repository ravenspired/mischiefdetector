// To Start:
function ClickConnect() {
    console.log("Clicking");
    document.querySelector("colab-connect-button").click()
}
ClickIntervalID = setInterval(ClickConnect, 30000)

// To Stop:
// clearInterval(ClickIntervalID)
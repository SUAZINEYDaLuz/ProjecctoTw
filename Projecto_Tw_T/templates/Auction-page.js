const startMinute = 2;
        let time = startMinute * 60;
        const countdownEl = document.getElementById("countdown")

        let counter = setInterval(updateCountdown, 1000);

        function updateCountdown() {
            const minute = Math.floor(time / 60);
            let second = time % 60;

            second = second < 10 ? '0' + second : second;

            countdownEl.innerHTML = `${minute}: ${second} `;
            time--;

            if (time <= 0) {
                showPopup();
                clearInterval(counter);
            }
        }

        function showPopup() {
            document.getElementById("popup").style.display = "block";
        }

        document.getElementById("close-button").addEventListener("click", function(){
            document.getElementById("popup").style.display = "none";
        })

<script lang="ts">
    import { Progress } from "sveltestrap";
    let timeLeft = 100;
    let id = setInterval(updateProgressBar, 100);
    function updateProgressBar() {
        if (timeLeft == 0) {
            clearInterval(id);
        } else {
            timeLeft--;
        }
    }
</script>

<main>
    <Progress animated color="success" value={timeLeft} />
</main>

<script lang="ts">
    import { onMount } from "svelte";
    import { Alert } from "sveltestrap";

    export let correct = false;
    type Color = "success" | "danger";
    let alert_color: Color = "success";
    let alert_message = "";
    let visible = false;
    onMount(() => {
        if (correct) {
            alert_color = "success";
            alert_message = "Correct!";
        } else {
            alert_color = "danger";
            alert_message = "Wrong!";
        }
        visible = !visible;
        let id = setInterval(alert_interval, 400);
        let timeLeft = 1;
        function alert_interval() {
            if (timeLeft == 0) {
                visible = !visible;
                clearInterval(id);
            } else {
                timeLeft--;
            }
        }
    });
</script>

<Alert color={alert_color} isOpen={visible}>
    {alert_message}
</Alert>

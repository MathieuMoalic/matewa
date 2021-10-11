<script lang="ts">
    import { Alert, Button, Card, CardBody } from "sveltestrap";
    import { word, input_word } from "../store";
    let visible = false;
    type Color = "success" | "danger";
    let alert_color: Color = "success";
    let alert_message = "";
    let checkWord = () => {
        if ($input_word === $word.pl) {
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
    };
    console.log($word);
</script>

<main>
    <Card>
        <CardBody>
            <div>
                Translate 🇫🇷 '{$word.fr}' in ({$word.pl})
            </div>
        </CardBody>
    </Card>
    <Card>
        <CardBody>
            <h4>🇵🇱</h4>
            <div>
                <input bind:value={$input_word} />
                <Button on:click={checkWord}>Check</Button>
            </div>

            <Alert color={alert_color} isOpen={visible}>
                {alert_message}
            </Alert>
        </CardBody>
    </Card>
</main>

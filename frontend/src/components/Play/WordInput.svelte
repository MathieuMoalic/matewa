<script lang="ts">
    import { Button, Card, CardBody } from "sveltestrap";
    import { word, input_word } from "../../store";
</script>

<main>
    <Card>
        <CardBody>
            <h4>🇫🇷 {$word.fr}</h4>
            <h4>
                🇵🇱 <input bind:value={$input_word} />
            </h4>
        </CardBody>
    </Card>
</main>

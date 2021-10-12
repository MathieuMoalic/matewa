<script lang="ts">
    import Alert from "./Alert.svelte";
    import { Button, Card, CardBody } from "sveltestrap";
    import { word, input_word } from "../../store.js";
    let correct = false;
    let checkWord = () => {
        if ($input_word === $word.pl) {
            correct = true;
            console.log(":)");
        } else {
            correct = false;
            console.log(":(");
        }
    };
</script>

<Button on:click={checkWord}>Check</Button>
